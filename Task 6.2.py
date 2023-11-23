import random

list_1 = []
list_2 = []

count = 0
while count < 10:
    list_1.append(random.randint(1, 10))
    list_2.append(random.randint(1, 10))
    count += 1
print(list_1)
print(list_2)

new_list = list_1 + list_2
new_list = list(set(new_list))
print(new_list)
