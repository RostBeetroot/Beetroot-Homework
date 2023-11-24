class MyIter:
    def __init__(self, iteration):
        self.iteration = list(iteration)

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):

        if self.current < len(self.iteration):
            self.current += 1
            return self.iteration[self.current - 1]
        else:
            raise StopIteration


my_iterable_list = MyIter([1, 2, 3, 4, 5])
my_dict = MyIter({"one": 1, "two": 2, "tree": 3}.items())
my_tuple = MyIter((1, 2, 3, 4, 5,))

for item in my_iterable_list:
    print(item)

# for key, value in my_dict:
#     print(key, value)
#
# for item in my_tuple:
#     print(item)
