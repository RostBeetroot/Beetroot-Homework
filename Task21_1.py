import logging


class FileContextManager:
    def __init__(self, file_name, mode='r'):
        self.filename = file_name
        self.mode = mode
        self.file = None
        self.counter = 0

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        self.counter += 1
        logging.info(f'Entered the context, file opened: {self.filename}')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.counter -= 1
        if self.file is not None:
            self.file.close()
            logging.info(f'Exited the context, file closed: {self.filename}')
        if exc_type is not None:
            logging.error(f'An exception of type {exc_type} occurred with value: {exc_value}')
        return False  # If you want exceptions to propagate, return False


# Example of using the custom context manager
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
filename = 'example.txt'

with FileContextManager(filename, 'w') as file:
    file.write('Hello, world!')

with FileContextManager(filename, 'r') as file:
    content = file.read()
    print(content)

print(f'Context counter: {FileContextManager(filename).counter}')
