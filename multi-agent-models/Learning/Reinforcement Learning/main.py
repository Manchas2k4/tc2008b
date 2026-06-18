'''
Problem:
Two robots find two power stations. Each station produces 10 units. If both robots 
go to the same station, they each receive only 5 units. After several attempts, 
the robots learn that obtaining 10 units is better than obtaining 5, so they end up 
splitting the stations. This behavior is rational because each robot selects the 
actions that maximize its expected utility.

States
    0 = No congestion (no robots).
    1 = Moderate congestion (few robots).
    2 = High congestion (many robots).

    | State | Meaning             | Northern Reward | Southern Reward |
| ----- | ------------------- | --------------- | --------------- |
| 0     | No Congestion       | 10              | 8               |
| 1     | Moderate Congestion | 8               | 7               |
| 2     | Heavy Congestion    | 5               | 6               |

'''
import random

 # Learning parameters
ALPHA = 0.1 # learning rate
GAMMA = 0.9 # discount factor
EPSILON = 0.2 # exploration

# Number of training sessions
EPOCHS = 5000

class Robot:
    def __init__(self, name):
        self.name = name
        self.states = [0, 1, 2]
        self.actions = ["NORTH", "SOUTH"]

        self.q_table = {
            state: {
                action : 0.0
                for action in self.actions
            }
            for state in self.states
        }

    def choose_action(self, state):
        if random.random() < EPSILON:
            return random.choice(self.actions)
        
        return max(self.q_table[state], key=self.q_table[state].get)
    
    def learn(self, state, action, reward, next_state):
        best_future_value = max(self.q_table[next_state].values())

        current_value = self.q_table[state][action]

        #Qt+1[st, at] ← (1 − α) · Q(st, at) + α · (r(st, at) + γ · m´axa Q(st+1, at))
        self.q_table[state][action] = ((1 - ALPHA) * current_value) + (ALPHA * (reward + (GAMMA * best_future_value)))


def get_rewards(state, action_r1, action_r2):
    if state == 0:
        north = 10
        south = 8
    elif state == 1:
        north = 8
        south = 7
    else:
        north = 5
        south = 6

    if action_r1 == action_r2:
        if action_r1 == "NORTH":
            return (north / 2, north / 2)
        else:
            return (south / 2, south / 2)
        
    reward_r1 = north if action_r1 == "NORTH" else south
    reward_r2 = north if action_r2 == "NORTH" else south
    return (reward_r1, reward_r2)
    

if __name__ == "__main__":
    robot1 = Robot("R1")
    robot2 = Robot("R2")

    for step in range(EPOCHS):
        # Current state
        state = random.choice([0, 1, 2])

        action1 = robot1.choose_action(state)
        action2 = robot2.choose_action(state)

        (reward1, reward2) = get_rewards(state, action1,action2)

        next_state = random.choice([0, 1, 2])

        robot1.learn(state, action1, reward1, next_state)
        robot2.learn(state, action2, reward2, next_state)

        print("\n=== Q TABLE ROBOT 1 ===")
        for state in robot1.states:
            print(
                f"state {state}: "
                f"{robot1.q_table[state]}"
            )

        print("\n=== Q TABLE ROBOT 2 ===")
        for state in robot2.states:
            print(
                f"state {state}: "
                f"{robot2.q_table[state]}"
            )

        print("\n=== POLICY LEARNED ===")
        for state in robot1.states:
            best_action_r1 = max(robot1.q_table[state], key=robot1.q_table[state].get)
            best_action_r2 = max(robot2.q_table[state], key=robot2.q_table[state].get)

            print(
                f"State {state}: "
                f"R1 -> {best_action_r1}, "
                f"R2 -> {best_action_r2}"
            )