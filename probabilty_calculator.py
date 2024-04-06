import copy
import random

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)

    def draw(self,numballs):
        if numballs > len(self.contents):
            return self.contents
        balls = []
        for i in range(numballs):
            ball = random.choice(self.contents)
            balls.append(ball)
            self.contents.remove(ball)
        return balls                    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0

    for _ in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        drawn_balls = new_hat.draw(num_balls_drawn)

        want_balls = []
        for key, value in expected_balls.items():
            for i in range(value):
                want_balls.append(key)

        match = 0

        for ball in want_balls:
            if ball in drawn_balls:
                match+=1
                drawn_balls.remove(ball)

        if match == len(want_balls):
            successes+=1

    if successes == 0:
        return 0
    else:
        return successes / num_experiments                            
            
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000) 
print(probability)                         