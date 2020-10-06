import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym.spaces import Discrete, Box
from gym.envs.classic_control import rendering
import pygame
from time import sleep
from random import randint
import sys
import numpy as np

class SnakeEnv(gym.Env):

    metadata = {'render.modes': ['human', 'rgb_array']}
    def __init__(self):

        self.size = 500
        self.numcell = 50
        self.gamespeed = 0.05
        pygame.init()
        self.done = False
        self.screen = pygame.display.set_mode((self.size, self.size))
        self.carl = [(1, 1)]
        self.direc = (0, 0)
        self.foodp = False
        self.ap = False
        self.food = None
        self.reward = 0
        self.state = []
        self.add = []
        self.viewer = None
        self.discrete_actions = [0, 1, 2, 3]
        self.action_space = Discrete(len(self.discrete_actions))
        self.observation_space = Box(low=0, high=255, dtype=np.uint8 ,shape=(
            self.size, self.size, 3))
    def getpos(self, pos):
        return (pos - 1) * (self.size / self.numcell)

    def step(self, action):

        self.screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Over")
                return [self.get_state(), self.reward, self.done]
        # set direction

        if action == 0:
            self.direc = (-1, 0)
        elif action == 1:
            self.direc = (1, 0)
        elif action == 2:
            self.direc = (0, -1)
        elif action == 3:
            self.direc = (0, 1)
        # check presence of food ans spawn food if needed
        if not self.foodp:
            self.food = (randint(0, self.numcell), randint(0, self.numcell))
            self.foodp = True
        # draw food
        pygame.draw.rect(self.screen, (255, 0, 0), (self.getpos(self.food[0]), self.getpos(self.food[1]), self.size / self.numcell, self.size / self.numcell))
        # run snake updates
        self.carl.insert(0, tuple(map(sum, zip(self.carl[0], self.direc))))
        if not self.ap:
            self.carl.pop()
        ap = False
        # draw carl
        for i in self.carl:
            pygame.draw.rect(self.screen, (255, 255, 255), (self.getpos(i[0]), self.getpos(i[1]), self.size / self.numcell, self.size / self.numcell))
        # check death
        if self.getpos(self.carl[0][1]) < 0 or self.getpos(self.carl[0][0]) < 0 or self.getpos(self.carl[0][1]) > self.size or self.getpos(self.carl[0][0]) > self.size or \
            self.carl[0] in self.carl[1:len(self.carl)]:
            self.done = True
            self.reward -= 100
            print("Over")
            self.reset()
              # check food after position update
        if self.carl[0] == self.food:
            self.reward += 100
            self.ap = True
            self.foodp = False
        sleep(self.gamespeed)

        pygame.display.update()
        return [self.get_state(), self.reward, self.done]
    def get_state(self):
        state = np.fliplr(np.flip(np.rot90(pygame.surfarray.array3d(pygame.display.get_surface()).astype(np.uint8)),axis=0))
        return state

    def reset(self):
        self.screen.fill((0, 0, 0))
        self.done = False
        self.carl = [(1, 1)]
        self.direc = (0, 0)
        self.foodp = False
        self.ap = False
        self.food = None

        for i in self.carl:
            pygame.draw.rect(self.screen, (255, 255, 255), (self.getpos(i[0]), self.getpos(i[1]), self.size / self.numcell, self.size / self.numcell))
        pygame.display.update()
        return self.get_state()
    def render(self, mode='human', close=False):
        img = self.get_state()
        if mode == 'human':
            if self.viewer is None:
                self.viewer = rendering.SimpleImageViewer()
            self.viewer.imshow(img)
        elif mode == 'rgb_array':
            return img
    def sample(self):
        return np.random.choice(self.discrete_actions)