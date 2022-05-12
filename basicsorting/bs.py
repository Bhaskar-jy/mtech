"""
  Implements linear search and binary search to analyse time complexity.
"""

import random

from matplotlib import pyplot as plt


def linear_search(value, list):
    """
    Searches the index of the value in the list.
    Returns the number of iterations.
    """

    for index, val in enumerate(list):
        if value == val:
            return index

    return index


def binary_search(value, list):
    """
    Searches the index of the value in the list using binary search.
    Returns the number of iterations.
    """

    iterations = 0
    index = len(list) // 2

    while value != list[index]:

        if value > list[index]:
            list = list[index:]
        else:
            list = list[:index]

        index = len(list) // 2
        iterations += 1

    return iterations


def compare_methods(size, n=100):
    """
    Returns the average number of iterations for each method to find
    a random value in a random list.
    """

    values_linear = []
    values_binary = []

    for _ in range(n):

        # Random list
        list = random.sample(range(size * 2), size)
        list = sorted(list)

        # Random value from list
        value = random.choice(list)

        values_linear.append(linear_search(value, list))
        values_binary.append(binary_search(value, list))

    return (
        sum(values_linear) / len(values_linear),
        sum(values_binary) / len(values_binary)
    )


def plot_time_complexity(a=10, b=100, step=10, n=100):
    """
    Plots time complexity comparison of both search methods for lists with size
    between 'a' and 'b'. Each value is an average of 'n' algorithm runs.
    """

    values = [(size, compare_methods(size, n)) for size in range(a, b, step)]

    steps = [value[0] for value in values]
    values_linear = [value[1][0] for value in values]
    values_binary = [value[1][1] for value in values]

    plt.plot(steps, values_linear, 'b-', label='Linear search')
    plt.plot(steps, values_binary, 'r-', label='Binary search')
    plt.title('Average number of iterations by list size')
    plt.xlabel('List size')
    plt.ylabel('Num. iterations')
    plt.legend(loc='upper left')

    last_value = (steps[-1], values_binary[-1])
    last_position = (
        steps[-1] - 0.2*b,
        values_binary[-1] + 0.1*b
    )
    plt.annotate('~%s' % values_binary[-1], xy=last_value, xytext=last_position,
                 arrowprops=dict(facecolor='black', shrink=0.05))

    plt.show()


if __name__ == '__main__':
    plot_time_complexity(10, 1000, 10)
