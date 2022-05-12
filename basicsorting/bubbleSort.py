def bubbleSort(lst):
    for i in range(1, len(lst)):
        for j in range(0, len(lst) - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


# # lst = [1, 2, 3, 4, 5, 6]
# lst = [6, 5, 4, 3, 2, 1]
# bubbleSort(lst)
# print(lst)
