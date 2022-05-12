A = {'a': 0.2, 'b': 0.3, 'c': 0.4, 'd': 0.5}
B = {'a': 0.1, 'b': 0.2, 'c': 0.2, 'd': 0.0}


def algebraicSum(a, b):
    result = {}
    for key in set(a) and set(b):
        result[key] = a[key] + b[key] - (a[key] * b[key])
    return result


result = algebraicSum(A, B)
print("\nAlgebraic Sum: {}\n".format(result))


def algebraicProduct(a, b):
    result = {}
    for key in set(a) and set(b):
        result[key] = round(a[key] * b[key], 2)
    return result


result = algebraicProduct(A, B)
print("Algebraic Product: {}\n".format(result))
