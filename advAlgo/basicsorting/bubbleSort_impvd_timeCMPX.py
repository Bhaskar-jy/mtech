from matplotlib import pyplot as plt
# from matplotlib import style
import time
from random import randint
from bubbleSort_improved import impv_bubblesort
# This program will show the running time of the imporoved bubble sort algorithm

# Generate random integers
inputs = [randint(0, 1000) for i in range(0, 2000)]
# print(inputs)

# run the algorithm and count the execution time for every inputs
# and store the calculated execution time in a list
times = []

for x in range(0, 2001, 100):
    start_time = time.time()
    sorted_list = impv_bubblesort(inputs[:x])
    end_time = time.time()
    execution_time = end_time - start_time
    # append the execution time value to times = []
    times.append(execution_time)

# Now for the number of inputs
numOfInpus = [x for x in range(0, 2001, 100)]
# Finally plot the graph
# style.use("ggplot")
plt.title("Improved Bubble Sort Algorithm Running Time")
plt.xlabel("No. of Elements")
plt.ylabel("Time required")
plt.legend(loc='best')
plt.grid(True)
plt.plot(numOfInpus, times, label='Improved Bubble Sort Algorithm',
         color='r', marker='o', linewidth=1)
plt.show()
