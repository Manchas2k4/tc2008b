'''
Problem:
Two robots find two power stations. Each station produces 10 units. If both robots 
go to the same station, they each receive only 5 units. After several attempts, 
the robots learn that obtaining 10 units is better than obtaining 5, so they end up 
splitting the stations. This behavior is rational because each robot selects the 
actions that maximize its expected utility.

Payoff Matrix
|          | R2 NORTH | R2 SOUTH |
| -------- | -------- | -------- |
| R1 NORTH | 5        | 10       |
| R1 SOUTH | 8        | 4        |

In a fictional game, each agent:
* Observes what actions the other agents take.
* Calculates the frequency with which each action has been chosen.
* Assumes that these frequencies represent the opponent's future strategy.
* Chooses the best possible response to that estimated strategy.

'''
import random

# Number of training sessions
EPOCHS = 100

class Robot:
    def __init__(self, name):
        self.name = name
        self.opponent_history = {
            "NORTH" : 1,
            "SOUTH" : 1
        }
        self.visits = {
            "NORTH" : 0,
            "SOUTH" : 0
        }

    def best_answer(self):
        total = sum(self.opponent_history.values())
        
        north_probability = self.opponent_history["NORTH"] / total
        south_probability = self.opponent_history["SOUTH"] / total

        north_utility = (north_probability * 5) + (south_probability * 10)
        south_utility = (north_probability * 8) + (south_probability * 4)

        if north_utility > south_utility:
            return "NORTH"
        else:
            return "SOUTH"
        
    def observe(self, opponent_action):
        self.opponent_history[opponent_action] += 1


if __name__ == "__main__":
    robot1 = Robot("R1")
    robot2 = Robot("R2")

    action1 = random.choice(["NORTH", "SOUTH"])
    action2 = random.choice(["NORTH", "SOUTH"])

    for step in range(EPOCHS):
        print(
            f"Step {step + 1}: "
            f"R1={action1}, "
            f"R2={action2}"
        )

        robot1.observe(action2)
        robot2.observe(action1)

        action1 = robot1.best_answer()
        action2 = robot2.best_answer()
        