import time
from list_gen import intgen, increasing, decreasing, constant, v_shape
from list_gen import intgen


# Function to measure the time taken by a function to execute
def time_it(func):
    def wrapper(*args, **kwargs):
        global input_list, new_list, list_len
        input_list = tested_list.copy()
        list_len = len(input_list)
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} seconds to execute")
        output_list.append(end - start)
        return result

    return wrapper


# Functions to measure performance
@time_it
def insertion_sort():
    for i in range(1, list_len):
        key = input_list[i]
        j = i - 1
        while j >= 0 and input_list[j] > key:
            input_list[j + 1] = input_list[j]
            j -= 1
        input_list[j + 1] = key


@time_it
def selection_sort():
    for j in range(list_len - 1):
        minimal = j
        for i in range(j + 1, list_len):
            if input_list[i] < input_list[minimal]:
                minimal = i

        input_list[j], input_list[minimal] = input_list[minimal], input_list[j]


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

    mergeSort(input_list, 0, list_len - 1)


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
result_list = [['Len', 'Type', 'IS', 'SS', 'HS', 'MS']]
list_gen_types = ['rand', 'inc', 'dec', 'const', 'v-shape']
input_list = []
new_list = []
output_list = [0]
tested_list = []
list_len = 0
end = 100
for i in range(1, end):
    input_list_len = i * 5
    generated_list = intgen(input_list_len)
    print(f"\n{i}/{end-1}")
    new_list = [generated_list,
                increasing(generated_list),
                decreasing(generated_list),
                constant(generated_list),
                v_shape(generated_list)]

    for j in range(5):
        output_list = [input_list_len, list_gen_types[j]]
        tested_list = new_list[j]
        print(f"\n{list_gen_types[j]}")
        insertion_sort()
        selection_sort()
        heap_sort()
        merge_sort()
        result_list.append(output_list)


with open("results.txt", "w") as f:
    for line in result_list:
        f.writelines(" ".join(list(map(str, line))) + "\n")

# @time_it
# def bubble_sort():
#     for i in range(list_len-1):
#         for j in range(list_len-i-1):
#             if input_list[j] > input_list[j+1]:
#                 input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
