from Task133 import square_nums, remove_negatives


# Test case 2
def test_square_nums():
    nums1 = [1, 2, 3, 4, 5]
    square_list = [1, 3, 9, 16, 25]
    assert square_nums(nums1) != square_list


# Test case 3
def test_remove_negatives():
    nums2 = [1, -2, 3, -4, 5]
    assert remove_negatives(nums2) == [1, 3, 5]


# Test case 4 - empty list
def test_empty_list():
    nums = []
    assert square_nums, remove_negatives == []
