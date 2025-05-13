import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn_balls = self.contents[:]
            self.contents = []
            return drawn_balls

        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        drawn_count = {}
        for color in drawn_balls:
            drawn_count[color] = drawn_count.get(color, 0) + 1

        success = True
        for color, count in expected_balls.items():
            if drawn_count.get(color, 0) < count:
                success = False
                break

        if success:
            successful_experiments += 1

    return successful_experiments / num_experiments
