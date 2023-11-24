class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.fail_message(message)

    def fail_message(self, message):
        with open("logs.txt", "a+") as file:
            file.write(f"{message} \n")


raise CustomException(message="ERROR")
