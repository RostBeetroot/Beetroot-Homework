def valid_phone_number(input_str):
    if len(input_str) != 10:
        return False
    if not input_str.isdigit():
        return False
    return True


phone_number = input("Enter a phone number: ")
if valid_phone_number(phone_number):
    print("The phone number is valid.")
else:
    print("The phone number is not valid.")
