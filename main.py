import prob_calculator

hat = prob_calculator.Hat(blue=4, red=2, green=6)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"red": 2,
                    "blue": 1},
    num_balls_drawn=5,
    num_experiments=3000)
print("Probability:", probability)



