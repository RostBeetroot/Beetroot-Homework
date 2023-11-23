import random

random_numbers = []

count = 0
while count < 10:
    random_numbers.append(random.randint(1, 100))
    count += 1
print(random_numbers)
print(max(random_numbers))
