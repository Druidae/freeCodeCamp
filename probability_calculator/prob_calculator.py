import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, num):
        if num >= len(self.contents):
            return self.contents
        else:
            balls = []
            for i in range(num):
                ball = random.choice(self.contents)
                balls.append(ball)
                self.contents.remove(ball)
            return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        expected_balls_copy = copy.deepcopy(expected_balls)
        success = True
        for ball in balls_drawn:
            if ball in expected_balls_copy:
                expected_balls_copy[ball] -= 1
                if expected_balls_copy[ball] == 0:
                    del expected_balls_copy[ball]
            if not expected_balls_copy:
                break
        if expected_balls_copy:
            success = False
        if success:
            count += 1
    return count/num_experiments
