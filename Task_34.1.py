import threading


class Counter(threading.Thread):
    counter = 0
    rounds = 100000

    def run(self):
        for _ in range(self.rounds):
            self.counter += 1


if __name__ == "__main__":
    # Create two instances of the Counter class
    thread1 = Counter()
    thread2 = Counter()

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

    # Check the result of the counter
    result = Counter.counter
    print("Final Counter Value:", result)


# import threading


class Counter(threading.Thread):
    counter = 0
    rounds = 100000
    lock = threading.Lock()

    def run(self):
        for _ in range(self.rounds):
            with self.lock:
                self.counter += 1


if __name__ == "__main__":
    # Create two instances of the Counter class
    thread1 = Counter()
    thread2 = Counter()

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

    # Check the result of the counter
    result = Counter.counter
    print("Final Counter Value:", result)
