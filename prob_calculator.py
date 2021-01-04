import random
import copy


class Hat:

    def __init__(self, **colors):
        self.contents = list()
        for color in colors:
            for i in range(colors[color]):
                self.contents.append(color)
        pass

    def draw(self, num):
        returnList = list()
        if num >= len(self.contents):
            returnList = list(self.contents)
            self.contents.clear()
        else:
            for i in range(num):
                x = random.randint(0, len(self.contents) - 1)
                returnList.append(self.contents.pop(x))
        return returnList


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_experiment_correct = 0
    #convert expected_balls to list, same with the return of Hat.draw()
    listBallsExpected = list()
    for ball in expected_balls:
        for i in range(expected_balls[ball]):
            listBallsExpected.append(ball)
    
    for i in range(num_experiments):
        hatCoppy = copy.deepcopy(hat)
        listBallsDrawn = hatCoppy.draw(num_balls_drawn)
        lenBefore = len(listBallsDrawn)
        for j in range(len(listBallsExpected)):
            try:
                listBallsDrawn.remove(listBallsExpected[j])
            except:
                break
        if len(listBallsDrawn) == lenBefore - len(listBallsExpected):
            num_experiment_correct += 1
            
    return num_experiment_correct/num_experiments
