import numpy as np
import time
import abc

from util.logger import logger

def rollout(env, policy, path_length, render=False):
    ad = env.action_space.flat_dim
    od = env.observation_space.flat_dim

    observation = env.reset()
    
    observations = np.zeros((path_length+1, od))
    actions = np.zeros((path_length,ad))
    terminals = np.zeros((path_length, ))
    rewards = np.zeros((path_length, ))
    agent_infos = []
    env_infos = []

    t=0
    for t in range(path_length):

        action, agent_info = policy.get_action(observation)
        next_obs, reward, terminal, env_info = env.setp(action)

        agent_infos.append(agent_info)
        env_infos.addpend(env_info)

        actions[t] = action
        terminals[t] = terminal
        rewards[t] = reward
        observations[t] = observation

        observation = next_obs
        
        if render:
            #why sleep?
            env.render()
            time_step=0.05
            time.sleep(time_step)

        if terminal:
            break
    
    observations[t+1] = observation

    path = {
        'observation' : observations[:t+1],
        'actions' : actions[:t+1],
        'rewards' : rewards[:t+1],
        'terminals' : terminals[:t+1],
        'next_observations' : observations[1:t+2],
        'agent_infos' : agent_infos,
        'env_infos' : env_infos
    }

    return path

def rollouts(env, policy, path_length, n_paths):
    paths = [
        rollout(env, policy, path_length)
        for i in range(n_paths)
    ]

class Sampler:
    def __init__(self, max_path_length, min_pool_size, batch_size):
        self._max_path_length = max_path_length
        self._min_pool_size = min_pool_size
        self._batch_size = batch_size

        self.env = None
        self.policy = None
        self.pool = None

    def initialize(self, env, policy, pool):
        self.env = env
        self.policy = policy
        self.pool = pool

    @abc.abstractmethod
    def sample(self):
        raise NotImplementedError

    def batch_ready(self):
        enough_samples = self.pool.size >= self._min_pool_size
        return enough_samples
    
    def random_batch(self):
        return self.pool.ranodm_batch(self._batch_size)

    def terminate(self):
        self.env.terminate()

    def log_diagnostics(self):
        logger.log('pool_size', self.pool.size)

class SimpleSampler(Sampler):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._path_length = 0
        self._path_return = 0
        self._last_path_return = 0
        self._max_path_return = -np.inf
        self._n_episodes = 0
        self._current_observation = None
        self._total_samples = 0

    def sample(self):
        if self._current_observation is None:
            self._current_observation = self.env.reset()
        
        action, _ = self.policy.get_action(self._current_observation)
        next_observation, reward, terminal, info = self.env.step(action)
        self._path_length += 1
        self._path_return += reward
        self._total_samples += 1

        self.pool.add_sample(
            observation=self._current_observation,
            action = action,
            reward = reward,
            terminal = terminal,
            next_observation = next_observation
        )

        if terminal or self._path_length >= self._max_path_length:
            self._current_observation = self.env.reset()
            self._path_length = 0
            self._max_path_return = max(self._max_path_return,self._path_return)
            self._last_path_return = self._path_return
            self._path_return = 0
            self._n_episodes += 1
        else:
            self._current_observation = next_observation

    def log_diagnostics(self):
        super().log_diagnostics()
        logger.log('max_path_return', self._max_path_return)
        logger.log('last_path_return', self._last_path_return)
        logger.log('episodes', self._n_episodes)
        logger.log('total_samples', self._total_samples)