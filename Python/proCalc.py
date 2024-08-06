import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)
    
    def draw(self, num_to_draw):
        drawn_balls = []
        if num_to_draw > len(self.contents):
            return self.contents
        for _ in range(num_to_draw):
            index = random.randrange(len(self.contents))
            drawn_balls.append(self.contents.pop(index))
        return drawn_balls

def toDict(ball_array):
    ret_dict = {}
    for item in ball_array:
        if item in ret_dict:
            ret_dict[item] +=1
        else:
            ret_dict[item] = 1
    return ret_dict

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    success_exp = 0
    for _ in range(num_experiments):
        temp_hat = copy.deepcopy(hat)
        drawn_balls = temp_hat.draw(num_balls_drawn)

        exp_dict = toDict(drawn_balls)

        is_success = True
        
        for key in expected_balls:
            value = expected_balls[key]
            if key in exp_dict:
                if exp_dict[key] >= value:
                    pass
                else:
                    is_success = False
            else:
                is_success = False
        if is_success:
            success_exp +=1
    return success_exp / num_experiments
        
    
    
    