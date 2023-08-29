import random


def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    question = f"{num1} {operator} {num2}"
    correct_answer = eval(question)
    return question, correct_answer


def main():
    print("Welcome to the Math Quiz!")

    while True:
        question, correct_answer = generate_question()

        print(f"What is the answer to {question}?")
        user_answer = input("Your answer: ")

        try:
            user_answer = float(user_answer)
            if user_answer == correct_answer:
                print("Correct! Well done.")
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")
        except ValueError:
            print("Invalid input. Please enter a numerical answer.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break


if __name__ == "__main__":
    main()
