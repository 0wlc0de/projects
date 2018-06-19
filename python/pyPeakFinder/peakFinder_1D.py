
# This is a peak finder algorithm in One Dimensional Data (Array)
# The mission is NOT TO FIND ALL the peaks in the data but TO FIND A peak on a data.


x_array = [1, 3, 4, 3, 5, 1, 3]


# Complexity : O(n)
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


# Complexity: O(logN) or base 2 logarithmic
x_half = x_array
while len(x_half) != 1:
    if x_half[int(len(x_half) / 2)] <= x_half[int(len(x_half) / 2) - 1]:
        x_half = x_half[:int(len(x_half) / 2)]
    else:
        x_half = x_half[int(len(x_half) / 2):]

print("There is a peak found in this data using Divide and Conquer: ", x_half[0])
