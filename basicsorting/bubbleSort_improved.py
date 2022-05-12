def impv_bubblesort(lst):
    for i in range(1, len(lst)):
        # a flag for imporoving the program
        flag = False
        for j in range(0, len(lst) - 1):
            # print("Inside Loop 2 of impv bbs::::")
            if lst[j] > lst[j+1]:
                # print("Inside if block of impv bbs::::")
                # if this if block gets a true value then make the flag as True
                flag = True
                lst[j], lst[j+1] = lst[j+1], lst[j]
        # and if the flag value is not True then break out of the loop.
        # This will break the loop at 0th index.
        # Improving the best case runtime to run in linear order time.
        if flag != True:
            break

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Ordinary Bubble Sort:::::::::::::\n")
# bbs_start = time.time()
# bubbleSort(lst)
# bbs_end = time.time()
# print("Running time: {}".format(bbs_end - bbs_start))
# print("{}\n".format(lst))

# print("Improved Bubble Sort:::::::::::::\n")
# impv_start = time.time()
# impv_bblesort(lst)
# impv_end = time.time()
# print("Running time: {}".format(impv_end - impv_start))
# print(lst)
