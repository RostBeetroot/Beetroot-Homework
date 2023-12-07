class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def get_from_stack(self, element):
        temp_stack = Stack()
        found = False
        while not self.is_empty():
            current_element = self.pop()
            if current_element == element:
                found = True
                break
            temp_stack.push(current_element)

        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        if found:
            return element
        else:
            raise ValueError(f"Element {element} not found in the stack")


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def get_from_queue(self, element):
        temp_queue = Queue()
        found = False
        while not self.is_empty():
            current_element = self.dequeue()
            if current_element == element:
                found = True
                break
            temp_queue.enqueue(current_element)

        while not temp_queue.is_empty():
            self.enqueue(temp_queue.dequeue())

        if found:
            return element
        else:
            raise ValueError(f"Element {element} not found in the queue")


# Example:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

try:
    result = stack.get_from_stack(2)
    print(f"Element found in stack: {result}")
except ValueError as e:
    print(e)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

try:
    result = queue.get_from_queue(2)
    print(f"Element found in queue: {result}")
except ValueError as e:
    print(e)
