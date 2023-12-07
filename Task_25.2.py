class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.top.data

    def display(self):
        current = self.top
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Example:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack after push operations:")
stack.display()

print("Top of the stack:", stack.peek())

popped_element = stack.pop()
print("Popped element:", popped_element)

print("Stack after pop operation:")
stack.display()
