'''
=================================================================
File: testing.py
Author: Pedro Perez
Date: 12-ago-2024
Description: This file implements the use of learning example for 
the following scenario:

In a two-dimensional array, an agent is placed at a (defined) 
starting point and must reach a destination cell in as few steps 
as possible. The agent can move between 1 or 2 cells in four 
possible directions: up, down, left, and right.

Copyright (c) 2024 by Tecnologico de Monterrey.
All Rights Reserved. May be reproduced for any non-commercial purpose.
=================================================================
'''
import random
import numpy as np

# SETTING GLOBAL PARAMETERS
ALPHA = 0.9 													# LEARNING RATE
GAMMA = 0.9														# DISCOUNT FACTOR
EPSILON = 0.10													# USING PREVIOUS KNOWLEDGE
TOTAL_GAMES = 2000 												# TOTAL GAMES TO BE PLAYED
MOVEMENT_OPTIONS = [-20, -10, 10, 20] 							# MOVEMENT OPTIONS, X AND Y
MAX_MOVEMENTS = len(MOVEMENT_OPTIONS) * len(MOVEMENT_OPTIONS)	# POSSIBLE MOVEMENTS TO MAKE
HEIGHT = 640 													# WINDOW HEIGHT
WIDTH = 480														# WINDOW WIDTH
HEIGHT = 640 													# WINDOW HEIGHT
WIDTH = 480														# WINDOW WIDTH
INITIAL_Y = 80													# INIITAL POSITION IN Y
INITIAL_X = 50													# INIITAL POSITION IN X
FINAL_Y = 320													# INIITAL POSITION IN Y
FINAL_X = 240													# INIITAL POSITION IN X
INCREMENT_X = 10												# INCREMENTS IN THE POSITION IN X
INCREMENT_Y = 10												# INCREMENTS IN THE POSITION IN Y
MAX_STATES = (WIDTH // INCREMENT_X) * (HEIGHT // INCREMENT_Y)	# ALL POSIBLE STATES (POSITIONS)
REWARD = 100													# REWARD AWARDED
MAX_STEPS = 2000												# EXPLORATION LIMIT

MAX_INCREMENT_X = 21											# CHECKING THE LIMIT IN X
MAX_INCREMENT_Y = 21											# CHECKING THE LIMIT IN Y

# SETTING THE Q TABLE
state_space = {}
possible_positions = []
for y in range (0, HEIGHT, INCREMENT_Y):
	for x in range(0, WIDTH, INCREMENT_X):
		possible_positions.append((y, x))
for i in range(MAX_STATES):
	state_space[i] = possible_positions[i]

# SETTING ALL POSSIBLE MOVEMENTES
actions_space = {}
possible_movements = []
for y in MOVEMENT_OPTIONS:
	for x in MOVEMENT_OPTIONS:
		possible_movements.append((y, x))
for i in range(MAX_MOVEMENTS):
	actions_space[i] = possible_movements[i]

q_table = np.loadtxt("qtable.csv", delimiter=",")

random.seed(12345)

def testing(posX, posY):
	steps = 0
	games = 1
	finished = False

	while not finished:
		steps += 1
		current_state = list(state_space.values()).index( (posY, posX) )
		current_reward = 0

		if steps == MAX_STEPS:
			print("Game : "+str(games) + " lost")
			games += 1
			posX = INITIAL_X
			posY = INITIAL_Y
			finished = True
			continue
		
		if random.random() < EPSILON:
			x = random.choice(MOVEMENT_OPTIONS)
			y = random.choice(MOVEMENT_OPTIONS)
			action = list(actions_space.values()).index( (y, x) )
		else:
			action = np.argmax(q_table[current_state])
			y, x = actions_space[action]

		if posX > (WIDTH - MAX_INCREMENT_X):
			x = -INCREMENT_X
		elif posX < (MAX_INCREMENT_X):
			x = INCREMENT_X
		if posY > (HEIGHT - MAX_INCREMENT_Y):
			y = - INCREMENT_Y
		elif posY < MAX_INCREMENT_Y:
			y = INCREMENT_Y
		posX += x
		posY += y

		print("step =", steps, " posX =", posX, " posY =", posY)

		if posX == FINAL_X and posY == FINAL_Y:
			print("Game : "+str(games) + " won")
			current_reward = REWARD
			finished = True

		next_state = list(state_space.values()).index( (posY, posX) )
		q_table[current_state, action] =  \
			((1 - ALPHA) * q_table[current_state, action]) + \
			(ALPHA * (current_reward + \
			 (GAMMA* np.max(q_table[next_state]))))
	
	np.savetxt("qtable.csv", q_table, delimiter=",")

posX = int(input("X = "))
posY = int(input("Y = "))

posX = posX - (posX % 10)
posY = posY - (posY % 10)
print("step =", 0, " posX =", posX, " posY =", posY)

testing(posX, posY)