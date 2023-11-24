class Mathematician:
    @staticmethod
    def square_nums(nums):
        return [i ** 2 for i in nums]

    @staticmethod
    def remove_positives(nums):
        return [i for i in nums if i <= 0]

    @staticmethod
    def filter_leaps(year):
        return [i for i in year if i % 4 == 0]


m = Mathematician()

# Test cases
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
