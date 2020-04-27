import gym
import pybulletgym

def main():
    env = gym.make("HopperPyBulletEnv-v0")
    env.render("human")
    env.reset()
    while True:
        action = env.action_space.sample()
        o,r,d,i = env.step(action)
        if d:
            env.reset()


    

if __name__ == '__main__':
    print('test')
    main()