import random

number = random.randint(1, 10)

while True:
    guess = int(input(f"Enter a number between 1 and 10: "))

    if guess < number:
        print(f"{guess} is too low")
    elif guess > number:
        print(f"{guess} is too high")
    else:
        print(f"{guess} is correct!")
        break
