'''
Problem:
Two robots find two power stations. Each station produces 10 units. If both robots 
go to the same station, they each receive only 5 units. After several attempts, 
the robots learn that obtaining 10 units is better than obtaining 5, so they end up 
splitting the stations. This behavior is rational because each robot selects the 
actions that maximize its expected utility.
'''

import random

# Probability of exploring instead of using prior knowledge											
EPSILON = 0.20
# Number of training sessions
EPOCHS = 100

# Actual value of the zones
ZONE_VALUE = {
    "NORTH" : 10,
    "SOUTH" : 8
}

class Robot:
    def __init__(self, name):
        self.name = name
        self.estimated_value = {
            "NORTH" : 0,
            "SOUTH" : 0
        }
        self.visits = {
            "NORTH" : 0,
            "SOUTH" : 0
        }

    def choose_zone(self):
       if random.random() < EPSILON:
           return random.choice(["NORTH", "SOUTH"])
       
       return max(self.estimated_value, key=self.estimated_value.get)
    
    def learn(self, zone, reward):
        self.visits[zone] += 1
        n = self.visits[zone]
        current_estimate = self.estimated_value[zone]

        new_estimate = (current_estimate + (reward - current_estimate)) / n

        self.estimated_value[zone] = new_estimate


if __name__ == "__main__":
    robot1 = Robot("R1")
    robot2 = Robot("R2")

    for step in range(EPOCHS):
        z1 = robot1.choose_zone()
        z2 = robot2.choose_zone()

        if z1 == z2:
            reward1 = ZONE_VALUE[z1] / 2
            reward2 = ZONE_VALUE[z2] / 2
        else:
            reward1 = ZONE_VALUE[z1]
            reward2 = ZONE_VALUE[z2]

        robot1.learn(z1, reward1)
        robot2.learn(z2, reward2)

        print(
            f"Step {step +1}: "
            f"R1->{z1}, "
            f"R2->{z2}, "
            f"Recompensas=({reward1}, {reward2})"
        )
        