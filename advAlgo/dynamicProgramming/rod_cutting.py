def cutRod(price, n):
    int_min = -32767
    val = [0 for x in range(n+1)]
    val[0] = 0
    for i in range(1, n+1):
        max_val = int_min
        for j in range(i):
            max_val = max(max_val, price[j]+val[i - j - i])
            val[i] = max_val
    return val[n]


arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum obtaining value is: {}".format(cutRod(arr, size)))
