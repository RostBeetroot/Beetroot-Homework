import random

user_input = input("Enter a word, minimum 5 letters: ")

a = 0
word_1 = ""
word_2 = ""
word_3 = ""
word_4 = ""
word_5 = ""

if len(user_input) < 5:
    print("once more, minimum 5 letters!")
else:
    while len(user_input) != a:
        word_1 += random.choice(user_input)
        word_2 += random.choice(user_input)
        word_3 += random.choice(user_input)
        word_4 += random.choice(user_input)
        word_5 += random.choice(user_input)
        a += 1
    print(word_1, word_2, word_3, word_4, word_5)
