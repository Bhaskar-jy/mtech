from bubbleSort import bubbleSort
import time
from matplotlib import pyplot as plt
from matplotlib import style
from random import randint
# This program will plot the time complexity nature of bubble sort algorithm
# generate a list of random integers from 0 to 1000
# below list will have a list of 20001 random integers from 0 - 999
inputs = [randint(0, 1000) for i in range(2000)]

# create an empty list to put all our time values for different inuts.
times = []

"""
Then we run a for-loop, each iteration has a different number of inputs. 
For each iteration, we first save the time before the execution of the algorithm. 
Then we run the quicksort algorithm by increasing the number of elements in each iteration. 
After the algorithm finishes its execution, we save the end time and subtract it with the start time to get the time elapsed. 
We then append the elapsed time to our list of times.
"""
for x in range(0, 2001, 100):
    start_time = time.time()
    # execution time increases with the increased inputs
    sorted_list = bubbleSort(inputs[:x])
    end_time = time.time()
    run_time = end_time - start_time
    times.append(run_time)
# print(times)

# we also need no. of inputs to plot the graph
numOfInputs = [i for i in range(0, 2001, 100)]
# print(numOfInputs)

# plotting
style.use("ggplot")
plt.title("Bubble Sort Algorithm Running Time")
plt.xlabel("No. of elements")
plt.ylabel("Time required")
plt.legend(loc='best')
plt.grid(True)
plt.plot(numOfInputs, times, color='g',
         label='Bubble Sort Algorithm', marker='o', linewidth=1)
plt.show()
