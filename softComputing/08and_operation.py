import numpy as np
# AND Gate input table
inputTable = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

print("Input Table: \n{}".format(inputTable))


def thresholdFunction(dotProductValue, thresholdValue):
    if dotProductValue >= thresholdValue:
        return 1
    else:
        return 0


def andFunction(dotProduct):
    theta = 2
    y_in = np.empty(dtype=int, shape=0)
    for i in range(0, 4):
        activation = thresholdFunction(dotProduct[i], theta)
        y_in = np.append(y_in, activation)
    return np.reshape(y_in, (4, 1))


weights = np.array([1, 1])
dot_product = inputTable @ weights
print("Dot Product: {}".format(dot_product))

print("Values: \n{}".format(andFunction(dot_product)))
