def first_function():
    def second_function(y, z):
        return y * z

    return second_function


print(first_function()(3, 4))
