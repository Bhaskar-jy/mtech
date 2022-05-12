import numpy as np
# OR gate input table
input_table = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
print("Input Table: \n{}".format(input_table))


def thresholFunction(dotProduct, thresholdValue):
    if dotProduct >= thresholdValue:
        return 1
    else:
        return 0


weights = np.array([1, 1])
dot_product = input_table @ weights
print("Dot Product: {}".format(dot_product))


def orFunction(dotProduct):
    theta = 1
    y_in = np.empty(dtype=int, shape=0)
    for i in range(0, 4):
        activation = thresholFunction(dotProduct[i], theta)
        y_in = np.append(y_in, activation)
    return np.reshape(y_in, (4, 1))


print("Values: \n{}".format(orFunction(dot_product)))
