A = {'a': 0.2, 'b': 0.3, 'c': 0.4, 'd': 0.5}
B = {'a': 0.1, 'b': 0.2, 'c': 0.2, 'd': 0.0}


def fuzzyComplement(a, b):
    complementResultA = {}
    complementResultB = {}
    for key in set(a) and set(b):
        complementResultA[key] = 1 - a[key]
        complementResultB[key] = 1 - b[key]
    print("Complement of Fuzzy Set A: {}\nComplement of Fuzzy Set B: {}".format(
        complementResultA, complementResultB))


fuzzyComplement(A, B)
