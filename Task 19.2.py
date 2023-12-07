def in_range(*args):
    num_args = len(args)

    if num_args == 1:
        start, end, step = 0, args[0], 1
    elif num_args == 2:
        start, end, step = args[0], args[1], 1
    elif num_args == 3:
        start, end, step = args
    else:
        raise TypeError

    while (step > 0 and start < end) or (step < 0 and start > end):
        yield start
        start += step


print(list(in_range(10, 0, -1)))
print(list(in_range(0, 10, 1)))
