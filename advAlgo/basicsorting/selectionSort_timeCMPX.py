from matplotlib import pyplot as plt
from selectionSort import selectionSort
from random import randint
import time

inputs = [randint(0, 1000) for i in range(0, 2000)]
timesSelection = []
for x in range(0, 2001, 100):
    start_time = time.time()
    sorted_list = selectionSort(inputs[:x])
    end_time = time.time()
    execution_time = end_time - start_time
    timesSelection.append(execution_time)

numOfInputs = [i for i in range(0, 2001, 100)]
plt.title("Selection Sort Algorithm")
plt.xlabel("No. of Inputs")
plt.ylabel("Time Required")
plt.grid(True)
plt.plot(numOfInputs, timesSelection, color='c', marker='o',
         linewidth=1, label='Selection Sort Algorithm')
plt.show()
