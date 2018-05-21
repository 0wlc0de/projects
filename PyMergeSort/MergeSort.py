x_array = [8, 7, 6, 5, 4, 3, 2, 1]


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)

        index_left = 0
        index_right = 0
        index_return_array = 0

        while index_left < len(left) and index_right < len(right):
            if left[index_left] > right[index_right]:
                array[index_return_array] = right[index_right]
                index_right += 1
            elif left[index_left] < right[index_right]:
                array[index_return_array] = left[index_left]
                index_left += 1

            index_return_array += 1

        while index_right < len(right):
            array[index_return_array] = right[index_right]
            index_right += 1
            index_return_array += 1

        while index_left < len(left):
            array[index_return_array] = left[index_left]
            index_left += 1
            index_return_array += 1

        print("Merging", array)


# merge_sort(x_array)
merge_sort(x_array)
