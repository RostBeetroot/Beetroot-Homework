def bidirectional_bubble_sort(array):
    n = len(array)
    swapped = True

    while swapped:
        # Move from left to right
        swapped = False
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        # If no swaps occurred, the list is already sorted
        if not swapped:
            break

        # Move from right to left
        swapped = False
        for i in range(n - 1, 0, -1):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                swapped = True

    return array


# Example:
my_list = [64, 34, 25, 12, 22, 11, 90]
bidirectional_bubble_sort(my_list)
print("Sorted array:", my_list)
