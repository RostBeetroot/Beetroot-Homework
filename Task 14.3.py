def arg_rules(type_: str, max_length: int, contains: list):
    def decorator(func):  # takes function "create_slogan"
        def wrapper(*args, **kwargs):

            result = func(*args, **kwargs)

            for mail in args:

                if not isinstance(mail, type_):
                    return False

                if len(mail) >= max_length:
                    return False

                for item in contains:
                    if item in mail:
                        return result
                    else:
                        return False

            return result

        return wrapper

    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('Tom') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
