from matplotlib import pyplot as plt
# from matplotlib import style
from random import randint
import time
from insertionSort import insertionSort

# This code will plot the running time of insertion sort algorithm

# run the algorithm
inputs = [randint(0, 1000) for i in range(0, 2000)]
# inputs.sort()
# print(inputs)

# make an empty time list. This will hold the list of execution time
timesInsertion = []
for x in range(0, 2001, 100):
    start_time = time.time()
    sorted_list = insertionSort(inputs[:x])
    end_time = time.time()
    execution_time = end_time - start_time
    # append the execution time for each iteration to
    timesInsertion.append(execution_time)


# now the number of inputs
numOfInputs = [i for i in range(0, 2001, 100)]


# finally plot the graph
# plt.title("Insertion Sort Algorithm Running Time(Best-Case Scenerio)")
# style.use('ggplot')
plt.title("Sorting Algorithms Running Time Comparasion")
plt.xlabel("No. of Inputs")
plt.ylabel("Time Required")
plt.grid(True)
plt.plot(numOfInputs, timesInsertion, color='g',
         label='InsertionSort', linewidth=1, marker='o')
plt.show()
