import random
import numpy as np

# SETTING GLOBAL PARAMETERS
ALPHA = 0.9 													# LEARNING RATE
GAMMA = 0.9														# DISCOUNT FACTOR
EPSILON = 0.20													# USING PREVIOUS KNOWLEDGE
TOTAL_GAMES = 2000 												# TOTAL GAMES TO BE PLAYED
MOVEMENT_OPTIONS = [-20, -10, 10, 20] 							# MOVEMENT OPTIONS, X AND Y
MAX_MOVEMENTS = len(MOVEMENT_OPTIONS) * len(MOVEMENT_OPTIONS)	# POSSIBLE MOVEMENTS TO MAKE
HEIGHT = 640 													# WINDOW HEIGHT
WIDTH = 480														# WINDOW WIDTH
HEIGHT = 640 													# WINDOW HEIGHT
WIDTH = 480														# WINDOW WIDTH
INITIAL_Y = 80													# INIITAL POSITION IN Y
INITIAL_X = 50													# INIITAL POSITION IN X
FINALL_Y = 320													# INIITAL POSITION IN Y
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

q_table = np.zeros( (MAX_STATES, MAX_MOVEMENTS) )

random.seed(12345)

def training():
	steps = 0
	posX = INITIAL_X
	posY = INITIAL_Y
	games = 1
	win_counter = 0
	finished = False

	while not finished:
		steps += 1
		current_state = list(state_space.values()).index( (posY, posX) )
		current_reward = 0

		if games == TOTAL_GAMES:
			finished = True
			print("Total games won: ", win_counter, "(", round((win_counter * REWARD) / TOTAL_GAMES, 2), "% )")
			np.savetxt("qtable.csv", q_table, delimiter=",")
			print("saved qtable")
			continue
			
		if steps == MAX_STEPS:
			print("Game : "+str(games) + " lost")
			games += 1
			step = 0
			posX = INITIAL_X
			posY = INITIAL_Y
			continue

		
		if games < (TOTAL_GAMES / 2):
			x = random.choice(MOVEMENT_OPTIONS)
			y = random.choice(MOVEMENT_OPTIONS)
			action = list(actions_space.values()).index( (y, x) )
		else:
			if random.random() < EPSILON:
				x = random.choice(MOVEMENT_OPTIONS)
				y = random.choice(MOVEMENT_OPTIONS)
				action = list(actions_space.values()).index( (y, x) )
			else:
				action = np.argmax(q_table[current_state])
				y, x = actions_space[action]

		#print("x =", x, " posY =", y)

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

		if posX == FINAL_X and posY == FINALL_Y:
			print("Game : "+str(games) + " won")
			current_reward = REWARD
			games += 1
			win_counter += 1
			steps = 0
			posX = INITIAL_X
			posY = INITIAL_Y

		next_state = list(state_space.values()).index( (posY, posX) )
		q_table[current_state, action] =  \
			((1 - ALPHA) * q_table[current_state, action]) + \
			(ALPHA * (current_reward + \
			 (GAMMA* np.max(q_table[next_state]))))


training()	