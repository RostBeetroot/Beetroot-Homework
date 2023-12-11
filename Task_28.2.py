list_a = [10, 20, 15, 30, 5]


# function to merge two sorted lists
def merge_list(x, y):
    c = []
    N = len(x)
    M = len(y)

    i = 0
    j = 0
    while i < N and j < M:
        if x[i] <= y[j]:
            c.append(x[i])
            i += 1
        else:
            c.append(y[j])
            j += 1

    c += x[i:] + y[j:]
    return c


# function of splitting a list and merging lists into a common sorted list
def split_and_merge_list(a):
    N1 = len(a) // 2
    a1 = a[:N1]
    a2 = a[N1:]

    if len(a1) > 1:
        a1 = split_and_merge_list(a1)
    if len(a2) > 1:
        a2 = split_and_merge_list(a2)

    return merge_list(a1, a2)


list_a = split_and_merge_list(list_a)

print(f'Result Task 2: {list_a}')
