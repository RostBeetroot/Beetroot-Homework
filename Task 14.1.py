def logger(func):  # takes function add()
    def wrapper(*args, **kwargs):  # replace wrapper(*args, **kwargs) -> add(x, y)
        print(*args)
        return func(*args, **kwargs)  # return result add()

    return wrapper  # return replaced function


@logger
def add(x, y):
    return x + y


add(1, 2)


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


square_all(3, 4)
