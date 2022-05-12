def betterLinearSearch(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return "{} is present at index {}.".format(element, i)
    return "not found"


lst = [11, 22, 111, 4, 3, 5, 6, 7, 6]
element = 1
print(betterLinearSearch(lst, element))
