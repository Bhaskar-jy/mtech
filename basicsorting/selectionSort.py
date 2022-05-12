def selectionSort(lst):
    for i in range(0, len(lst)):
        smallestIndex = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[smallestIndex]:
                smallestIndex = j
            # swap(lst[j], lst[smallestIndex])
            lst[j], lst[smallestIndex] = lst[smallestIndex], lst[j]


# lst = [1, 6, 4, 2, 3]
# selectionSort(lst)
# print(lst)
