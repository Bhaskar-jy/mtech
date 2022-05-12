import time
from matplotlib import pyplot as plt


def linearSearch(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i
        else:
            pass
    return -1


# lst = [randint(0, 100000) for i in range(0, 3000)]
lst = [11, 22, 222, 44, 24, 5, 76, 34, 23, 12, 4, 3]

# print(lst)
# element = randint(0, 100000)
element = 76
# index = linearSearch(lst, element)
# print("Element = {}".format(element))
# if index == -1:
#     print("Element is not present")
# else:
#     print("Element is in index {}".format(index))

# Time Calculation
times = []
# index = 0
# elementAt = ()
for x in range(0, len(lst), 5):
    start_time = time.time()
    index = linearSearch(lst[:x], element)
    end_time = time.time()
    execution_time = end_time - start_time
    times.append(execution_time)
print("Index = {}".format(index))
# print("Index type = {}".format(type(index)))
# elementAt = (0, index)
# print("Element at = ({})".format(elementAt))

numOfInputs = [i for i in range(0, len(lst), 5)]
plt.title("Linear Search Algorithm")
plt.xlabel("No. Of Inputs")
plt.ylabel("Time Required")
plt.grid(True)
plt.plot(numOfInputs, times, label='linear search',
         color='g', linewidth=1, marker='o')
plt.legend(loc='best')
plt.show()
