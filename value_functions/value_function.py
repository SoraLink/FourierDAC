import tensorflow as tf

class NNVFunction(MLPFunction):

    def __init__(self, env_spec, hidden_layer_sizes=(100, 100), name='vf'):
        self._od = env_spec.observation_space.flat_dim
        self._obs_input = tf.keras.Input(shape=(None, self._od), dtype=tf.float32, name=name+'/observation')
        super().__init__(name,(self._obs_input,), hidden_layer_sizes)

class NNQFunction(MLPFunction):
    def __init__(self, env_spec, hidden_layer_sizes=(100,100), name='qf'):
        self._ad = env_spec.action_space.flat_dim
        self._od = env_spec.observation_space.flat_dim

        self._obs_input = tf.keras.Input(shape=(None, self._od),dtype=tf.float32, name=name+'/observation')

        self._action_input = tf.keras.Input(shape=(None,self._ad), dtype=tf.float32, name=name+'/action')

        super().__init__(name,(self._obs_input,self._action_input), hidden_layer_sizes)

class NNDiscriminatorFunction(MLPFunction):
    NotImplemented