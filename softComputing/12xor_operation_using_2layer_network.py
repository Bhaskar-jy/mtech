import numpy as np
input_table = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])


def result(y_in, t):
    if y_in >= t:
        return 1
    else:
        return 0


# first layer
weight1 = np.array([1, -1])
weight2 = np.array([-1, 1])

y_in1 = input_table @ weight1
y_in2 = input_table @ weight2

t = 1
activation1 = []
activation2 = []
for i in range(0, 4):
    activation_result1 = result(y_in1[i], t)
    activation_result2 = result(y_in2[i], t)
    activation1.append(activation_result1)
    activation2.append(activation_result2)
activation1 = np.array(activation1)
activation2 = np.array(activation2)

input3 = np.concatenate(activation1.reshape(
    4, 1), activation2.reshape(4, 1))

# second layer
weight3 = np.array([1, 1])
y_in3 = input3 @ weight3

t = 1
for i in range(0, 4):
    activation = result(y_in3[i], t)
    print("activation: {}".format(activation))
