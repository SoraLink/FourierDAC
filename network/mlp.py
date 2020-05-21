import tensorflow as tf

def mlp(inputs, layer_sizes, name, nonlinearity=tf.nn.relu,
        output_nonlinearity=tf.nn.tanh, squeeze=True):

    net = None
    for i, input in enumerate(inputs):
        if net is None:
            net = tf.keras.layers.Dense(units=layer_sizes[0], name=name+'/fc1/%d'%i)(input)
        else:
            net += tf.keras.layers.Dense(units=layer_sizes[0], name=name+'/fc1/%d'%i)(input)
    
    net = nonlinearity(net)

    for i, size in enumerate(layer_sizes[1:]):
        if i < len(layer_sizes)-1:
            net = tf.keras.layers.Dense(units=size, activation=nonlinearity,name=name+'fc%d'%i)(net)
        else:
            net = tf.keras.layers.Dense(units=size, activation=output_nonlinearity,name=name+'fc%d'%i)(net)
    if squeeze:
        net = tf.squeeze(net, axis=-1)
    
    model = tf.keras.Model(inputs=inputs, outputs=net)
    return model
    
class MLPFunction:
    def __init__(self, name, mlp_input, hidden_layer_sizes, output_nonlinearity=None):
        self._name = name
        self._input = mlp_input
        self._layer_sizes = list(hidden_layer_sizes) + [None]
        self._output_nonlinearity = output_nonlinearity

        self._model = self.get_model_for(self._input)

    def get_model_for(self, inputs):
        model = mlp(inputs, 
                    self._layer_sizes, 
                    self._name, 
                    output_nonlinearity= self._output_nonlinearity
                )
        return model
    
    def eval(self, *inputs):
        predict = self._model.predict(inputs)
        return predict

    def get_params_internal(self, **tags):
        return self._model.get_weights()
    
    #TODO: Train method