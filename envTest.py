import gym
import pybulletgym
import tensorflow as tf

def main():
    env = gym.make("HopperPyBulletEnv-v0")
    env.render("human")
    env.reset()
    while True:
        action = env.action_space.sample()
        o,r,d,i = env.step(action)
        if d:
            env.reset()

def name_scope_test():
    with tf.name_scope('test'):
        inputs = tf.keras.layers.Input([1,], name='ob') 
        net = tf.keras.layers.Dense(units=64, name='fc1')(inputs)
        G = tf.keras.Model(inputs=inputs, outputs=net)
        layers = G.get_layer(name='fc1')
        print(layers[0].name)
        

    

if __name__ == '__main__':
    # print('test')
    name_scope_test()