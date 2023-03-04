import time
from list_gen import gen

new_list = gen(10000)


# Function to measure the time taken by a function to execute
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} seconds to execute")
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


@time_it
def bubble_sort():
    for i in range(len(input_list)-1):
        for j in range(len(input_list)-i-1):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]


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


@time_it
def build_in_sort():
    input_list.sort()


# # Call the functions
input_list = new_list.copy()
insertion_sort()
input_list = new_list.copy()
selection_sort()
input_list = new_list.copy()
bubble_sort()
input_list = new_list.copy()
merge_sort()
input_list = new_list.copy()
build_in_sort()
