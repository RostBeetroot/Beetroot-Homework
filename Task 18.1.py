import re


class Mail:
    def __init__(self, email: str):
        self.email = email
        self.validate()

    def validate(self):
        current_mail = r'^[a-zA-Z0-9]+(?:\.[a-zA-Z0-9])*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]{2,7}$'
        our_mail = self.email
        if not re.match(current_mail, our_mail):
            raise ValueError("incorrect mail")


mail_1 = Mail("rrr@gmail.com")  # Valid email
mail_2 = Mail("abcd@mail.co")  # Valid email
# mail_3 = Mail("abc.def@mail")  # Invalid email
# mail_4 = Mail("abc#def@mail.com")  # Invalid email
# mail_5 = Mail("abc-@mail.com")  # Invalid email
