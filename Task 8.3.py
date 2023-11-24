arithmetic_parameter = input("Choose: '+', '-' or '*': ")
arbitrary_number = input("Enter integer numbers separated ',': ").split(',')

integer_arbitrary_number = []

for i in arbitrary_number:
    integer_arbitrary_number.append(int(i))


def make_operation(arithmetic_parameter1, integer_arbitrary_number1):
    if arithmetic_parameter1 == "+":
        result_plus = 0
        for a in integer_arbitrary_number1:
            result_plus += a
        return result_plus
    elif arithmetic_parameter1 == "-":
        result_minus = 0
        for a in integer_arbitrary_number1:
            result_minus -= a
        return result_minus
    elif arithmetic_parameter1 == "*":
        result_multiplication = 1
        for a in integer_arbitrary_number1:
            result_multiplication *= a
        return result_multiplication


print(make_operation(arithmetic_parameter, integer_arbitrary_number))
