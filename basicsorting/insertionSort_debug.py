def insertionsort(lst):
    for i in range(1, len(lst)):  # from 1 to n-1
        #  since i is starting from index 1
        # that means j should start from i -1 index i.i., from 0
        print("For i = {}".format(i))
        j = i - 1
        print("j = i - 1 is {}".format(j))
        key = lst[i]  # the element at 1st index for i = 1
        print("Key = lst[i] is {}".format(key))
        while j >= 0 and lst[j] >= key:
            print()
            print("Current lst = {}".format(lst))
            print(
                "Checking condition while j>=0 and lst[{}] = {} >= {}".format(j, lst[j], key))
            print("lst[j+1] is {}".format(lst[j+1]))
            print("lst[j] is {}".format(lst[j]))
            lst[j+1] = lst[j]
            print("After lst[j+1 = {}] = lst[j = {}]".format(j+1, j))
            print("lst[j+1] is {}".format(lst[j+1]))
            j = j - 1  # decrementing j
            print("Decrementing j as j = j - 1: {}".format(j))
            print()
        lst[j+1] = key
        print()
        print("Out of while loop::::::")
        print("lst[j+1 = {}]:{} = key:{}".format(j+1, lst[j+1], key))
        print()


print(":::::::::::Insertion Sort Debugging::::::::::")
lst = [10, 9, 8]
print("Before sorting the array: {}".format(lst))
insertionsort(lst)
print("After sorting the array: {}".format(lst))
