import time
from list_gen import intgen


def test_loop(list_len: int = 1000):
    new_list = intgen(list_len)
    input_list = new_list.copy()
    test_result_list = []

    # Function to measure the time taken by a function to execute
    def time_it(func):
        def wrapper(*args, **kwargs):
            nonlocal input_list
            input_list = new_list.copy()
            # print(new_list)
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{func.__name__} took {end - start:.6f} seconds to execute")
            test_result_list.append(end - start)
            # print(new_list)
            return result
        return wrapper


    # Functions to measure performance
    @time_it
    def insertion_sort():
        for i in range(1, len(input_list)):
            key = input_list[i]
            j = i - 1
            while j >= 0 and input_list[j] > key:
                input_list[j + 1] = input_list[j]
                j -= 1
            input_list[j + 1] = key


    @time_it
    def selection_sort():
        for j in range(len(input_list) - 1):
            minimal = j
            for i in range(j + 1, len(input_list)):
                if input_list[i] < input_list[minimal]:
                    minimal = i

            input_list[j], input_list[minimal] = input_list[minimal], input_list[j]


    # @time_it
    # def bubble_sort():
    #     for i in range(len(input_list)-1):
    #         for j in range(len(input_list)-i-1):
    #             if input_list[j] > input_list[j+1]:
    #                 input_list[j], input_list[j+1] = input_list[j+1], input_list[j]


    @time_it
    def merge_sort():
        def merge(input_list, l, m, r):
            n1 = m - l + 1
            n2 = r - m

            # create temp input_listays
            L = [0] * (n1)
            R = [0] * (n2)

            # Copy data to temp input_listays L[] and R[]
            for i in range(0, n1):
                L[i] = input_list[l + i]

            for j in range(0, n2):
                R[j] = input_list[m + 1 + j]

            # Merge the temp input_listays back into input_list[l..r]
            i = 0  # Initial index of first subinput_listay
            j = 0  # Initial index of second subinput_listay
            k = l  # Initial index of merged subinput_listay

            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    input_list[k] = L[i]
                    i += 1
                else:
                    input_list[k] = R[j]
                    j += 1
                k += 1

            # Copy the remaining elements of L[], if there
            # are any
            while i < n1:
                input_list[k] = L[i]
                i += 1
                k += 1

            # Copy the remaining elements of R[], if there
            # are any
            while j < n2:
                input_list[k] = R[j]
                j += 1
                k += 1

        # l is for left index and r is right index of the
        # sub-input_listay of input_list to be sorted

        def mergeSort(input_list, l, r):
            if l < r:
                # Same as (l+r)//2, but avoids overflow for
                # large l and h
                m = l + (r - l) // 2

                # Sort first and second halves
                mergeSort(input_list, l, m)
                mergeSort(input_list, m + 1, r)
                merge(input_list, l, m, r)

        mergeSort(input_list, 0, len(input_list)-1)


    # @time_it
    # def build_in_sort():
    #     input_list.sort()


    # @time_it
    # def quick_sort():
    #     def qsort(A, p, r):
    #         if p < r:
    #             q = partition(A, p, r)
    #             print(p, q, r)
    #             qsort(A, p, q)
    #             qsort(A, q+1, r)
    #
    #     def partition(A, p, r):
    #         pivot_val = A[r]
    #         i = p
    #         j = r
    #         while True:
    #             while A[i] < pivot_val:
    #                 i += 1
    #             while A[j] > pivot_val:
    #                 j -= 1
    #             if i < j:
    #                 A[i], A[j] = A[j], A[i]
    #                 i += 1
    #                 j -= 1
    #             else:
    #                 return j
    #
    #     qsort(input_list, 0, len(input_list)-1)


    @time_it
    def heap_sort():
        def heapify(arr, n, i):
            largest = i  # Initialize largest as root
            l = 2 * i + 1  # left = 2*i + 1
            r = 2 * i + 2  # right = 2*i + 2

            # See if left child of root exists and is
            # greater than root

            if l < n and arr[i] < arr[l]:
                largest = l

            # See if right child of root exists and is
            # greater than root

            if r < n and arr[largest] < arr[r]:
                largest = r

            # Change root, if needed

            if largest != i:
                (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap

                # Heapify the root.

                heapify(arr, n, largest)

        # The main function to sort an array of given size

        def heapSort(arr):
            n = len(arr)

            # Build a maxheap.
            # Since last parent will be at ((n//2)-1) we can start at that location.

            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, n, i)

            # One by one extract elements

            for i in range(n - 1, 0, -1):
                (arr[i], arr[0]) = (arr[0], arr[i])  # swap
                heapify(arr, i, 0)

        # Driver code to test above

        heapSort(input_list)


    # # Call the functions
    insertion_sort()
    selection_sort()
    # bubble_sort()
    merge_sort()
    heap_sort()
    # build_in_sort()
    # print(test_result_list)
    return test_result_list

result_list = []
for i in range(100):
    print(10+i*30)
    result = [10+i*30] + test_loop(10+i*30)
    result_list.append(result)


with open("results.txt", "w") as f:
    for line in result_list:
        f.write(" ".join(list(map(str, line)) + ["\n"]))