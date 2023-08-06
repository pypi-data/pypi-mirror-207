# Copyright 2023 OmniSafe Team. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Model-based Adapter for OmniSafe."""
from __future__ import annotations

import time
from typing import Any, Callable

import torch

from omnisafe.adapter.online_adapter import OnlineAdapter
from omnisafe.common.logger import Logger
from omnisafe.envs.core import make, support_envs
from omnisafe.envs.wrapper import (
    ActionRepeat,
    ActionScale,
    AutoReset,
    CostNormalize,
    ObsNormalize,
    RewardNormalize,
    TimeLimit,
    Unsqueeze,
)
from omnisafe.utils.config import Config


class ModelBasedAdapter(
    OnlineAdapter,
):  # pylint: disable=too-many-instance-attributes,super-init-not-called
    """Model Based Adapter for OmniSafe.

    :class:`ModelBasedAdapter` is used to adapt the environment to the model-based training.


    Args:
        env_id (str): The environment id.
        num_envs (int): The number of environments.
        seed (int): The random seed.
        cfgs (Config): The configuration.
        kwargs(dict): The other keyword arguments.

    Attributes:
        _env_id (str): The environment id.
        _device (torch.device): The device.
        _env (CMDP): The environment.
        _cfgs (Config): The configuration.
        _ep_ret (torch.Tensor): The episode return.
        _ep_cost (torch.Tensor): The episode cost.
        _ep_len (torch.Tensor): The episode length.
        _last_dynamics_update (float): The last time of dynamics update.
        _last_policy_update (float): The last time of policy update.
        _last_eval (float): The last time of evaluation.
        coordinate_observation_space (OmnisafeSpace): The coordinate observation space.
        lidar_observation_space (OmnisafeSpace): The lidar observation space.
        task (str): The task. eg. The task of SafetyPointGoal-v0 is 'goal'
    """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        env_id: str,
        num_envs: int,
        seed: int,
        cfgs: Config,
        **kwargs: Any,
    ) -> None:
        """Initialize the model-based adapter."""
        assert env_id in support_envs(), f'Env {env_id} is not supported.'

        self._env_id = env_id
        self._device = cfgs.train_cfgs.device

        self._env = make(env_id, num_envs=num_envs, device=cfgs.train_cfgs.device, **kwargs)

        # wrap the environment, use the action repeat in model-based setting.
        self._wrapper(
            obs_normalize=cfgs.algo_cfgs.obs_normalize,
            reward_normalize=cfgs.algo_cfgs.reward_normalize,
            cost_normalize=cfgs.algo_cfgs.cost_normalize,
            action_repeat=cfgs.algo_cfgs.action_repeat,
        )
        self._env.set_seed(seed)
        self._cfgs = cfgs
        if hasattr(self._env, 'coordinate_observation_space') and hasattr(
            self._env,
            'lidar_observation_space',
        ):
            self.coordinate_observation_space = self._env.coordinate_observation_space
            self.lidar_observation_space = self._env.lidar_observation_space
        else:
            self.coordinate_observation_space = None
            self.lidar_observation_space = None
        if hasattr(self._env, 'task'):
            self.task = self._env.task
        else:
            self.task = None

        self._ep_ret: torch.Tensor
        self._ep_cost: torch.Tensor
        self._ep_len: torch.Tensor
        self._current_obs, _ = self.reset()
        self._max_ep_len = 1000
        self._reset_log()
        self._last_dynamics_update = 0
        self._last_policy_update = 0
        self._last_eval = 0
        self._first_log = False

    def get_goal_flag_from_obs_tensor(self, obs: torch.Tensor) -> torch.Tensor | None:
        """Get goal flag from tensor observation.

        Args:
            obs (torch.Tensor): The observation.
        """
        return (
            self._env.get_goal_flag_from_obs_tensor(obs)
            if hasattr(self._env, 'get_goal_flag_from_obs_tensor')
            else None
        )

    def get_cost_from_obs_tensor(self, obs: torch.Tensor) -> torch.Tensor | None:
        """Get cost from tensor observation.

        Args:
            obs (torch.Tensor): The observation.
        """
        return (
            self._env.get_cost_from_obs_tensor(obs)
            if hasattr(self._env, 'get_cost_from_obs_tensor')
            else None
        )

    def get_lidar_from_coordinate(self, obs: torch.Tensor) -> torch.Tensor | None:
        """Get lidar from numpy coordinate.

        Args:
            obs (np.ndarray): The observation.
        """
        return (
            self._env.get_lidar_from_coordinate(obs)
            if hasattr(self._env, 'get_lidar_from_coordinate')
            else None
        )

    def render(self, *args: str, **kwargs: int) -> Any:
        """Render the environment.

        Args:
            args (str): The arguments.
            kwargs (int): The keyword arguments.
        """
        return self._env.render(*args, **kwargs)

    def _wrapper(
        self,
        obs_normalize: bool = True,
        reward_normalize: bool = True,
        cost_normalize: bool = True,
        action_repeat: int = 1,
    ) -> None:
        """Wrapper the environment.

        .. hint::

            OmniSafe supports the following wrappers:

            .. list-table::

                *   -   Wrapper
                    -   Description
                *   -   TimeLimit
                    -   Limit the time steps of the environment.
                *   -   AutoReset
                    -   Reset the environment when the episode is done.
                *   -   ObsNormalize
                    -   Normalize the observation.
                *   -   RewardNormalize
                    -   Normalize the reward.
                *   -   CostNormalize
                    -   Normalize the cost.
                *   -   ActionScale
                    -   Scale the action.
                *   -   ActionRepeat
                    -   Repeat the action.
                *   -   Unsqueeze
                    -   Unsqueeze the step result for single environment case.

        Args:
            obs_normalize (bool): Whether to normalize the observation.
            reward_normalize (bool): Whether to normalize the reward.
            cost_normalize (bool): Whether to normalize the cost.
            action_repeat (int): The action repeat times.
        """
        if self._env.need_time_limit_wrapper:
            self._env = TimeLimit(self._env, device=self._device, time_limit=1000)
        if self._env.need_auto_reset_wrapper:
            self._env = AutoReset(self._env, device=self._device)
        if obs_normalize:
            self._env = ObsNormalize(self._env, device=self._device)
        if reward_normalize:
            self._env = RewardNormalize(self._env, device=self._device)
        if cost_normalize:
            self._env = CostNormalize(self._env, device=self._device)
        self._env = ActionScale(self._env, device=self._device, low=-1.0, high=1.0)
        self._env = ActionRepeat(self._env, times=action_repeat, device=self._device)

        if self._env.num_envs == 1:
            self._env = Unsqueeze(self._env, device=self._device)

    def roll_out(  # pylint: disable=too-many-arguments,too-many-locals
        self,
        current_step: int,
        roll_out_step: int,
        use_actor_critic: bool,
        act_func: Callable,
        store_data_func: Callable,
        update_dynamics_func: Callable,
        logger: Logger,
        use_eval: bool,
        eval_func: Callable,
        algo_reset_func: Callable,
        update_actor_func: Callable,
    ) -> int:
        """Roll out the environment and store the data in the buffer.

        Args:
            current_step (int): Current training step.
            roll_out_step (int): Number of steps to roll out.
            use_actor_critic (bool): Whether to use actor-critic.
            act_func (Callable): Function to get action.
            store_data_func (Callable): Function to store data.
            update_dynamics_func (Callable): Function to update dynamics.
            logger (Logger): Logger.
            use_eval (bool): Whether to use evaluation.
            eval_func (Callable): Function to evaluate the agent.
            algo_reset_func (Callable): Function to reset the algorithm.
            update_actor_func (Callable): Function to update the actor.
        """
        epoch_start_time = time.time()

        update_actor_critic_time = 0.0
        update_dynamics_time = 0.0
        if use_eval:
            eval_time = 0.0

        epoch_steps = 0

        while epoch_steps < roll_out_step and current_step < self._cfgs.train_cfgs.total_steps:
            action, action_info = act_func(current_step, self._current_obs, self._env)
            next_state, reward, cost, terminated, truncated, info = self.step(action)
            epoch_steps += info['num_step']
            current_step += info['num_step']
            self._log_value(reward=reward, cost=cost, info=info)

            store_data_func(
                current_step,
                self._ep_len,
                self._current_obs,
                action,
                reward,
                cost,
                terminated,
                truncated,
                next_state,
                info,
                action_info,
            )
            self._current_obs = next_state
            if terminated or truncated:
                self._log_metrics(logger)
                self._reset_log()
                self._current_obs, _ = self.reset()
                if algo_reset_func is not None:
                    algo_reset_func(current_step)
            if (
                current_step % self._cfgs.algo_cfgs.update_dynamics_cycle
                < self._cfgs.algo_cfgs.action_repeat
                and current_step - self._last_dynamics_update
                >= self._cfgs.algo_cfgs.update_dynamics_cycle
            ):
                update_dynamics_start = time.time()
                update_dynamics_func(current_step)
                self._last_dynamics_update = current_step
                update_dynamics_time += time.time() - update_dynamics_start

            if (
                use_actor_critic
                and current_step % self._cfgs.algo_cfgs.update_policy_cycle
                < self._cfgs.algo_cfgs.action_repeat
                and current_step - self._last_policy_update
                >= self._cfgs.algo_cfgs.update_policy_cycle
            ):
                update_actor_critic_start = time.time()
                update_actor_func(current_step)
                self._last_policy_update = current_step
                update_actor_critic_time += time.time() - update_actor_critic_start

            if (
                use_eval
                and current_step % self._cfgs.evaluation_cfgs.eval_cycle
                < self._cfgs.algo_cfgs.action_repeat
                and current_step - self._last_eval >= self._cfgs.evaluation_cfgs.eval_cycle
            ):
                eval_start = time.time()
                eval_func(current_step)
                self._last_eval = current_step
                eval_time += time.time() - eval_start

        if not self._first_log or current_step >= self._cfgs.train_cfgs.total_steps:
            self._log_metrics(logger)

        epoch_time = time.time() - epoch_start_time
        logger.store(**{'Time/Epoch': epoch_time})
        logger.store(**{'Time/UpdateDynamics': update_dynamics_time})
        roll_out_time = epoch_time - update_dynamics_time

        if use_eval:
            logger.store(**{'Time/Eval': eval_time})
            roll_out_time -= eval_time

        if use_actor_critic:
            logger.store(**{'Time/UpdateActorCritic': update_actor_critic_time})
            roll_out_time -= update_actor_critic_time
        logger.store(**{'Time/Rollout': roll_out_time})
        return current_step

    def _log_value(
        self,
        reward: torch.Tensor,
        cost: torch.Tensor,
        info: dict,
    ) -> None:
        """Log value.

        .. note::
            OmniSafe uses :class:`RewardNormalizer` wrapper, so the original reward and cost will
            be stored in ``info['original_reward']`` and ``info['original_cost']``.

        Args:
            reward (torch.Tensor): The reward.
            cost (torch.Tensor): The cost.
            info (dict): Information.
        """
        self._ep_ret += info.get('original_reward', reward).cpu()
        self._ep_cost += info.get('original_cost', cost).cpu()
        self._ep_len += info.get('num_step', 1)

    def _log_metrics(self, logger: Logger) -> None:
        """Log metrics.

        Args:
            logger (Logger): Logger.
        """
        self._first_log = True
        logger.store(
            **{
                'Metrics/EpRet': self._ep_ret,
                'Metrics/EpCost': self._ep_cost,
                'Metrics/EpLen': self._ep_len,
            },
        )

    def _reset_log(self, idx: int | None = None) -> None:  # pylint: disable=unused-argument
        """Reset log.

        Args:
            idx (int | None): The index of the environment.
        """
        self._ep_ret = torch.zeros(1)
        self._ep_cost = torch.zeros(1)
        self._ep_len = torch.zeros(1)
