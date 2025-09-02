import random
import numpy as np
from utils import actions

class Agent:
    __MAXIMUM = 3
    __answer = [2, 0, 1]

    def __init__(self):
        self.__beliefs = [0, 0, 0]
        print("Initial beliefs of the agent: " + str(self.__beliefs) + "\n")

    def choose_move(self):
        index = np.argmax(self.__beliefs) % self.__MAXIMUM
        return self.__answer[index]
    
    def update_move(self, move):
        self.__beliefs[move] += 1
        print("New beliefs of the agent: " + str(self.__beliefs) + "\n")


