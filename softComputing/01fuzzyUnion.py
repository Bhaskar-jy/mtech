A = {'a': 0.2, 'b': 0.3, 'c': 0.4, 'd': 0.5}
B = {'a': 0.1, 'b': 0.2, 'c': 0.2, 'd': 0.0}
# print("Set A:{}\nSet B: {}".format(A, B))


# Fuzzy UNION
def fuzzyUnion(a, b):
    unionResult = {}
    for key in set(a) and set(b):
        unionResult[key] = max(a[key], b[key])
    return unionResult


print("Union Result: {}".format(fuzzyUnion(A, B)))
