
# This is a peak finder algorithm in One Dimensional Data (Array)
# The mission is NOT TO FIND ALL the peaks in the data but TO FIND A peak on a data.

# Complexity : O(n)

x_array = [1, 2, 3, 3, 1, 5]

for x in range(0, len(x_array)):
    if x == 0 or x == len(x_array):
        if x == 0:
            if x_array[x] >= x_array[x + 1]:
                print("There is a peak found on this data: ", x_array[x])
                break
        elif x == len(x_array):
            if x_array[x] >= x_array[x - 1]:
                print("There is a peak found on this data: ", x_array[x])
                break
        else:
            continue
    else:
        if x_array[x] >= x_array[x - 1] and x_array[x] >= x_array[x + 1]:
            print("There is a peak found on this data: ", x_array[x])
            break
        else:
            continue
