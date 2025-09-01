import random
import time
import numpy as np

class Agent:
    SCISSORS = 0
    PAPER = 1
    STONE = 2
    MAXIMUM = 3

    def __init__(self):
        self.__beliefs = [random.randint(1, 3) for _ in range(3)]
        self.__answer = [2, 0, 1]
        print("initial beliefs of the agent: " + str(self.__beliefs))

    def make_move(self):
        index = np.argmax(self.__beliefs) % self.MAXIMUM
        return self.__answer[index]
    
    def update_move(self, move):
        self.__beliefs[move] += 1
        print("new beliefs of the agent: " + str(self.__beliefs))


def translate_move(move):
    if move == Agent.SCISSORS:
        return "scissors"
    elif move == Agent.PAPER:
        return "paper"
    else:
        return "stone"
    
def who_won(move_a, move_b):
    diff = move_a - move_b
    if move_a == 0:
        return 0 if move_a == move_b else (-1 if move_b == 1 else 1)
    elif move_a == 1:
        return 0 if move_a == move_b else (-1 if move_b == 2 else 1)
    else:
        return 0 if move_a == move_b else (-1 if move_b == 0 else 1)