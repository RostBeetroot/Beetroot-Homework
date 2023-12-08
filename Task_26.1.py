# Binary search using recursion

def binary_search_recursive(array, low, high, target):
    if low <= high:
        mid = low + (high - low) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            return binary_search_recursive(array, mid + 1, high, target)
        else:
            return binary_search_recursive(array, low, mid - 1, target)
    else:
        return -1


# Example:
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search_recursive(array, 0, len(array) - 1, target)

if result != -1:
    print(f"element {target} found in position {result}.")
else:
    print(f"element {target} missing from the array.")


# Fibonacci search algorithm

def fibonacci_search(array, target):
    n = len(array)
    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib = fib_m_minus_1 + fib_m_minus_2

    while fib < n:
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib
        fib = fib_m_minus_1 + fib_m_minus_2

    offset = -1

    while fib > 1:
        i = min(offset + fib_m_minus_2, n - 1)

        if array[i] < target:
            fib = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib - fib_m_minus_1
            offset = i

        elif array[i] > target:
            fib = fib_m_minus_2
            fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
            fib_m_minus_2 = fib - fib_m_minus_1

        else:
            return i

    if fib_m_minus_1 and array[offset + 1] == target:
        return offset + 1

    return -1


# Example:
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = fibonacci_search(array, target)

if result != -1:
    print(f"element {target} found in position {result}.")
else:
    print(f"element {target} missing from the array.")
