def in_range(start, end, step=1):
    while start < end if step > 0 else start > end:
        yield start
        start += step


print(list(in_range(10, 0, -1)))
print(list(in_range(0, 10, 1)))
