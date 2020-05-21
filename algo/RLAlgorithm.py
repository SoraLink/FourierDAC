import abc
import tensorflow as tf

class RLAlgorithm:

    def __init__(self,
                sampler,
                n_epochs=1000,
                n_train_repeat=1,
                n_initial_exploration_steps=10000,
                epoch_length=1000,
                eval_n_episodes=10,
                eval_deterministic=True,
                eval_render=False,
                control_interval=1
                ):
        self._n_epochs = n_epochs
        self._n_epochs = int(n_epochs)
        self._n_train_repeat = n_train_repeat
        self._epoch_length = epoch_length
        self._n_initial_exploration_steps = n_initial_exploration_steps
        self._control_interval = control_interval

        self._eval_n_episodes = eval_n_episodes
        self._eval_deterministic = eval_deterministic
        self._eval_render = eval_render
        
        self._sess = tf.compat.v1.get_default_session()

        self._env = None
        self._policy = None
        self._pool = None

    @abc.abstractmethod
    def _train(self, env, policy, initial_exploration_policy, pool):
        raise NotImplementedError
    
    @abc.abstractmethod
    def _evaluate(self, epoch):
        raise NotImplementedError

    @abc.abstractmethod
    def _do_training(self, iteration, batch):
        raise NotImplementedError
    
    @abc.abstractmethod
    def _init_training(self, env, policy, pool):
        raise NotImplementedError