def is_balanced(sequence):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in sequence:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or stack.pop() != brackets[char]:
                return False

    return not stack


if __name__ == "__main__":
    input_sequence = input("Enter a sequence of characters: ")

    if is_balanced(input_sequence):
        print("The sequence is balanced.")
    else:
        print("The sequence is not balanced.")
