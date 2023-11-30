from math import gcd


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        another = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator // another, new_denominator // another)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        new_func = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator // new_func, new_denominator // new_func)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        new_func = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator // new_func, new_denominator // new_func)

    def __truediv__(self, other):
        assert other.numerator != 0
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        new_func = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator // new_func, new_denominator // new_func)

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    x + y == Fraction(3, 4)
