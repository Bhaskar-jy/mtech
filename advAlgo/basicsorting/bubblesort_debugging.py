def bubblesorting(lst):
    print("Bubble Sorting Debugging:::::::::::::::")
    print("List before sorting = {}".format(lst))
    for i in range(len(lst)):
        print("Inside 1st for loop:::::")
        print("Value of ith iteration = {}".format(i))
        print()
        for j in range(len(lst) - 1):
            print("Inside nested for loop:::::")
            print("Value of jth iteration = {}".format(j))
            print()
            if lst[j] < lst[j+1]:
                print("If lst[{}]: {} < lst[{}+1]: {}".format(j,
                      lst[j], j, lst[j+1]))
                print()
                # swap
                print("Before Swapping:::::")
                print("Value of lst[j] = {}".format(lst[j]))
                print("And")
                print("Value of lst[j+1] = {}".format(lst[j+1]))
                print()
                lst[j], lst[j+1] = lst[j+1], lst[j]
                print("After Swapping:::::")
                print("Value of lst[j] = {}".format(lst[j]))
                print("And")
                print("Value of lst[j+1] = {}".format(lst[j+1]))
        print("Out of Nested for loop::::\n")
    print("Out of 1st for loop::::\n")


lst = [2, 1, 4]
bubblesorting(lst)
print("The sorted list is: {}".format(lst))
