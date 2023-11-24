def with_index(iterable, start=0):
    count = start
    for item in iterable:
        yield count, item
        count += 1


print(list(with_index([1, 2, 3])))
