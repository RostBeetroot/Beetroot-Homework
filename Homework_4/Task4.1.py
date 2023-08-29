def get_string(text):
    if len(text) < 2:
        return ""
    return text[:2] + text[-2:]


string = input("Enter a string: ")
print('new string:', get_string(string))
