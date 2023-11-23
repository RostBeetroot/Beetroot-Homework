my_list = list(range(1, 101))

new_list = []

element = 0

while element < 100:
    if my_list[element] % 7 == 0 and my_list[element] % 5 != 0:
        new_list.append(my_list[element])
    element += 1

print(new_list)
