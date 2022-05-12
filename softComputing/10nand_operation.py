import numpy as np

input_table = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])


def thresholdFunction(dotProduct, threshold):
    if dotProduct <= threshold:
        return 1
    else:
        return 0


def nandFunction(dotProd):
    theta = 1
    y_in = np.empty(dtype=int, shape=0)
    for i in range(0, 4):
        activation = thresholdFunction(dotProd[i], theta)
        y_in = np.append(y_in, activation)
    return np.reshape(y_in, (4, 1))


weights = np.array([1, 1])
print(f"Weights: {weights}")
dotProduct = input_table @ weights
print(f"dot product: {dotProduct}")


print("y_in: \n{}".format(nandFunction(dotProd=dotProduct)))
  