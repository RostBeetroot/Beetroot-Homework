def squared_divided():
    a = float(input("Enter number for a: "))
    b = float(input("Enter number for b: "))
    result = (a ** 2) / b
    return print(result)


try:
    squared_divided()
except ValueError:
    print("Input must be a number")
except ZeroDivisionError:
    print("Can't be zero!")
