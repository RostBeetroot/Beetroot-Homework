# Write a decorator that takes a list of stop words
# and replaces them with * inside the decorated function

def stop_words(words: list):
    def first_wrapper(func):  # takes function "create_slogan"
        def second_wrapper(*args, **kwargs):  # replace second wrapper with args & kwargs -> parameter "name"
            returned_result = func(*args, **kwargs)
            for i in words:
                returned_result = returned_result.replace(i, "*")
            print(returned_result)
            return returned_result  # return result create_slogan

        return second_wrapper  # return replaced function

    return first_wrapper  # return inner function


@stop_words(['pepsi', 'BMW'])  # replace word to '*'
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
