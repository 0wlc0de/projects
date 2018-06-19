x_array = [8, 7, 6, 5, 4, 3, 2, 1]


# Complexity : average and worst case -> O(n^2)
#            : Where n is equals to the number of items
def insertion_sort(x):
    # this is the length of th array - 1
    for i in range(1, len(x)):

        # capture the value of x[i]
        valueToInsert = x[i]

        # capture the value of i
        index = i

        # while the holePosition iss not equal to 0 : which is the first index on the array to avoid IndexRangeException
        while index > 0 and x[index - 1] > valueToInsert:
            x[index] = x[index - 1]
            index = index - 1
        x[index] = valueToInsert
        print(x_array)

    return x


print(insertion_sort(x_array))
