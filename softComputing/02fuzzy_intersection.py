A = {'a': 0.2, 'b': 0.3, 'c': 0.4, 'd': 0.5}
B = {'a': 0.1, 'b': 0.2, 'c': 0.2, 'd': 0.0}


def fuzzyIntersection(a, b):
    intersectionResult = {}
    for key in set(a) and set(b):
        intersectionResult[key] = min(a[key], b[key])
    return intersectionResult


print("Intersection Result: {}".format(fuzzyIntersection(A, B)))
