from algo.RLAlgorithm import RLAlgorithm
import tensorflow as tf

class SACAlgorithm(RLAlgorithm):

    def __init__(self,
                base_kwargs,
                
                env,
                policy,
                initial_exploration_policy,
                qf1,
                qf2,
                vf,
                pool,
                plotter=None,
                lr=3e-3,
                scale_reward=1,
                discount=0.99,
                tau=0.01,
                target_update_interval=1,
                action_prior='uniform',
                reparameterize=False,
                save_full_state=False,
                ):
        super().__init__(**base_kwargs)

        self._env = env
        self._policy = policy
        self._initial_exploration_policy = initial_exploration_policy
        self._qf1 = qf1
        self._qf2 = qf2
        self._vf = vf
        self._pool = pool

        self._policy_lr = lr
        self._qf_lr = lr
        self._vf_lr = lr
        self._scale_reward = scale_reward
        self.discount = discount
        self._tau = tau
        self._target_update_interval = target_update_interval
        self._action_prior = action_prior

        # 不知道干什么 待查
        # Reparameterize parameter must match between the algorithm and the
        # policy actions are sampled from.
        assert reparameterize == self._policy._reparameterize
        self._reparameterize = reparameterize

        self._save_full_state = save_full_state

        self._ad = self._env.action_space.flat_dim
        self._od = self._env.observation_space.flat_dim

        #不知道
        self._training_ops = list()
        
        self._init_placeholders()
        self._init_actor_update()
        self._init_critic_update()
        self._init_target_ops()

        def train(self):
            """Initiate instance."""
            self._init_training(env, policy, pool)

        def _target_ops(self):
            source_params = self._vf_params
            target_params = self._vf_target_params 
            for target, source in zip(target_params, source_params):
                tf.keras.backend.set_value(target, (1-self._tau)*target+self._tau*source)

        @property
        def _vf_params(self):
            self._vf.get_source_params_internal()

        @property
        def _vf_target_params(self):
            self._vf.get_target_params_internal()