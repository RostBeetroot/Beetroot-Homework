import random


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def quicksort(array, partition_limit=10):
    if len(array) <= partition_limit:
        insertion_sort(array)
    else:
        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        array = quicksort(left) + middle + quicksort(right)
    return array


# Example:

# Generate a random list of integers
random_list = [random.randint(1, 100) for _ in range(20)]
print("Original list:", random_list)

# Sort the list using quicksort with different partition limits
for limit in [5, 10, 15]:
    sorted_list = quicksort(random_list.copy(), partition_limit=limit)
    print(f"Sorted list with partition limit {limit}:", sorted_list)
