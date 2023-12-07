class UnsortedList:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            raise ValueError(f"{item} not found in the list")

    def display(self):
        print(self.items)

    def append(self, item):
        self.items.append(item)

    def index(self, item):
        if item in self.items:
            return self.items.index(item)
        else:
            raise ValueError(f"{item} not found in the list")

    def pop(self, index=None):
        if index is None:
            return self.items.pop()
        else:
            return self.items.pop(index)

    def insert(self, index, item):
        self.items.insert(index, item)

    def slice(self, start, stop):
        return self.items[start:stop]


# Example usage:
my_list = UnsortedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.display()  # Output: [1, 2, 3]

print("Index of 2:", my_list.index(2))  # Output: Index of 2: 1

my_list.pop()
my_list.display()  # Output: [1, 2]

my_list.insert(1, 4)
my_list.display()  # Output: [1, 4, 2]

sliced_list = my_list.slice(0, 2)
print("Sliced List:", sliced_list)  # Output: Sliced List: [1, 4]
