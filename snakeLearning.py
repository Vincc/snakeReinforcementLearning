

from keras import Input
from keras.models import Model
from keras.layers import Dense, Flatten
from rl.memory import SequentialMemory
from rl.policy import LinearAnnealedPolicy, EpsGreedyQPolicy
from rl.agents.dqn import DQNAgent
from stable_baselines.deepq.policies import MlpPolicy
from stable_baselines.common.vec_env.dummy_vec_env import DummyVecEnv
from stable_baselines.bench import Monitor
from stable_baselines import DQN, A2C, PPO2, ACER
from stable_baselines.results_plotter import load_results, ts2xy



import matplotlib.pyplot as plt
from IPython import display as ipythondisplay

import imageio
import time
import numpy as np
print("keras imported")
import gym
import snake_Env
print("imported")
from gym import spaces
from gym.utils import seeding

##learning hyperparameters
num_actions = 4
state_size = 2500
#Note: Inputs for model: [wall right, wall front, wall left, snake headx, snake heady, food x, food y]

env = gym.make('snakeEnv-v0')

env.reset()
def randomSample():
    for i in range(1000):
        env.render()
        print(env.observation_space)
        print(env.get_state().shape)
        env.step(env.action_space.sample()) # take a random action
    env.close()

randomSample()
# model = DQN(MlpPolicy, env, verbose=1, prioritized_replay=True)
# # Train the agent
# start = time.time()
#
# end = time.time()
# model.save("dqn_snakeml")
# model.learn(total_timesteps=4000)
# eval_model = DQN.load("dqn_snakeml")
# # Evaluate the trained agent
