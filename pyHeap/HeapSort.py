from math import floor


x_array = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1]


# Complexity O(n)
# this method is used to create and validate the leftChilds, rightChilds of the Parent Nodes
# all arrays can be visualize as nearly complete binary tree or HEAP
def build_heap(array):
    mid = int(floor(len(array)/2))

    for x in range(mid, -1, -1):
        print(x, ":", array[x])
        leftChild_index = 2 * x + 1
        rightChild_index = 2 * x + 2
        if leftChild_index > len(array)-1:
            print(array[x], "has no children")
        elif leftChild_index == len(array)-1:
            print("Array PARENT: ", array[x], "CHILDREN: leftChild -", array[leftChild_index], ": rightChild -",
                  "NONE")
        elif leftChild_index <= len(array) and rightChild_index < len(array):
            print("Array PARENT: ", array[x], "CHILDREN: leftChild -", array[leftChild_index], ": rightChild -",
                  array[rightChild_index])



build_heap(x_array)
