# cartesian product of two fuzzy sets
import numpy as np

A = [0.3, 0.7, 1.0]
# A = [0.2, 0.3, 0.4, 0.5]
a = np.array(A)
B = [0.4, 0.9]
# B = [0.1, 0.2, 0.2, 0.0]
b = np.array(B)


def cartesianProduct(a, b):
    a_dim = np.shape(a)
    b_dim = np.shape(b)
    row = a_dim[0]
    col = b_dim[0]
    product = []
    for x1 in a:
        for y1 in b:
            product.append(min(x1, y1))
    return np.reshape(product, (row, col))


result = cartesianProduct(a, b)
print("Cartesian Product of \n{} \nand \n{} \nis : \n{}\n".format(a, b, result))
# print(np.shape(result))
