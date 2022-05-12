import numpy as np

r1 = np.array([
    [0.7, 0.5],
    [0.8, 0.4]
])
r2 = np.array([
    [0.9, 0.6, 0.5],
    [0.1, 0.7, 0.5]
])


def maxMinComposition(x, y):
    x_dim_sum = np.shape(x)
    y_dim_sum = np.shape(y)
    x_shape_sum = x_dim_sum[0] + x_dim_sum[1]
    y_shape_sum = y_dim_sum[0] + y_dim_sum[1]
    z = []
    for x1 in x:
        for y1 in y.T:  # y.T -> y transpose
            z.append(max(np.minimum(x1, y1)))
    if x_shape_sum >= y_shape_sum:
        return np.reshape(z, np.shape(x))
    else:
        return np.reshape(z, np.shape(y))


maxMin_result = maxMinComposition(r1, r2)
print("Max-Min Composition is: \n{}".format(r1, r2, maxMin_result))
