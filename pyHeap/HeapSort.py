"""
    Heap Sort using the Pseudo-code from MIT OpenCourseWare
    Complexity of This Algorithm O(n logN)
"""


class HeapSort:

    # defining an initialization
    # arguments -> Unordered Array
    def __init__(self, A):
        self.A = A
        self.heap_size = len(self.A)

    # Heapify the violated children that are not max heaps
    def Max_Heapify(self, i, heap_size):
        l = 2 * i + 1
        r = 2 * i + 2
        if l < heap_size - 1 and self.A[l] > self.A[i]:
            largest = l
        else:
            largest = i
        if r <= heap_size - 1 and self.A[r] > self.A[largest]:
            largest = r
        if largest != i:
            swapValue = self.A[i]
            self.A[i] = self.A[largest]
            self.A[largest] = swapValue
            self.Max_Heapify(largest, heap_size)

    # Building Max heap in the first step
    def Build_Max_Heap(self):
        for i in range(len(self.A), -1, -1):
            self.Max_Heapify(i, self.heap_size)
            # print("Sorting", self.A)
        print("MaX_HEAP : ", self.A)

    # Sort the Array Using the Build_Max_heap to have a Max Heap first, Then swap the first element which is A[0]
    # to the last element of the Array  ->  A[len(array)-1] then reduce the heap size so that the last element which is
    # the highest element in the Array will never be move again
    def sort(self):

        # Step 1: Build Max Heap from Unordered Array
        self.Build_Max_Heap()

        # Loop the heap size
        while self.heap_size > 0:

            # Store the last element in a temporary variable
            swap = self.A[self.heap_size - 1]

            # Swap the value of the root Array -> A[0] to the last element -> A[len(A) - 1]
            self.A[self.heap_size - 1] = self.A[0]
            self.A[0] = swap

            # Reduce the Heap size so that the last element will be unaffected with any changes
            self.heap_size -= 1

            # Call the Max Heapify at 0 index which is the root because it is likely that after swapping the root and
            # the last element will violate the Max_heap
            self.Max_Heapify(0, self.heap_size)

        print("Sorted Array : ", self.A)


x_array = [11, 23, 42, 45, 6, 12, 7, 100, 1, 23, 42, 45, 6, 12, 7, 10]
heapSort = HeapSort(x_array)
heapSort.sort()
