from matplotlib import pyplot as plt
from matplotlib import style
from random import randint
import time
from selectionSort import selectionSort
from insertionSort import insertionSort
from bubbleSort import bubbleSort
from bubbleSort_improved import impv_bubblesort
from mergeSort import mergeSort
# This code will plot the running time of insertion sort algorithm

input_range = 3000
sampling_size = 100
# run the algorithm
inputs = [randint(0, 1000) for i in range(0, input_range)]
# inputs.sort()
# print(inputs)

# function to calculate the execution time of a sorting algorithms


def findTime(algoName):
    times = []
    for x in range(0, input_range + 1, sampling_size):
        start_time = time.time()
        # call the sorting algorithm
        algoName(inputs[:x])
        end_time = time.time()
        execution_time = end_time - start_time
        times.append(execution_time)
    return times


timesInsertion = findTime(insertionSort)
timesBubble = findTime(bubbleSort)
timesImpvBubble = findTime(impv_bubblesort)
timesSelection = findTime(selectionSort)
timesMerge = findTime(mergeSort)


# now the number of inputs
numOfInputs = [i for i in range(0, input_range + 1, sampling_size)]


# finally plot the graph
# plt.title("Insertion Sort Algorithm Running Time(BEST-CASE)")
# style.use('ggplot')
plt.title("Sorting Algorithms Running Time Comparision(WORST-CASE)")
plt.ylabel("No. of Inputs")
plt.xlabel("Time of Required")
plt.grid(True)
plt.plot(timesInsertion, numOfInputs, color='g',
         label='Insertion Sort', linewidth=1, marker='o')
plt.plot(timesBubble, numOfInputs, color='c',
         label='Bubble Sort', linewidth=1, marker='o')
plt.plot(timesImpvBubble, numOfInputs, color='r',
         label='Improved Bubble Sort', linewidth=1, marker='o')
plt.plot(timesSelection, numOfInputs,  color='y',
         label='Selection Sort', linewidth=1, marker='o')
plt.plot(timesMerge, numOfInputs,  color='b',
         label='Merge Sort', linewidth=1, marker='o')
plt.legend(loc='best')
plt.show()
