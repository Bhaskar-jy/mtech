def insertionSort(lst):
    """" Insertion Sort """
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] >= key:
            lst[j+1] = lst[j]
            j = j - 1
        lst[j+1] = key


def linearSearch(lst, element):
    """ Linear Search """
    for i in range(len(lst)):
        if lst[i] == element:
            # if element found then return the position of the element
            return i
    # otherwise return a negative value.
    return -1


def bubbleSort(lst):
    """ Bubble Sort """
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] < lst[j+1]:
                # then swap
                lst[j], lst[j+1] = lst[j+1], lst[j]


def selectionSort(lst):
    """Selection Sort """
    for i in range(len(lst)):
        smallestIndex = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[smallestIndex]:
                smallestIndex = j
            # swap
            lst[j], lst[smallestIndex] = lst[smallestIndex], lst[j]


lst = [22, 11, 3, 5, 7, 9]
element = 3
# insertionSort(lst)
# print(lst)
# result = linearSearch(lst, element)
# print(result)
# bubbleSort(lst)
# print(lst)
selectionSort(lst)
print(lst)
