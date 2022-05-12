def insertionSort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j+1] = lst[j]
            j -= 1
        lst[j + 1] = key


# lst = [1, 6, 4, 2, 3]
# lst.sort()
# print(lst)
# insertionSort(lst)
# print(lst)
