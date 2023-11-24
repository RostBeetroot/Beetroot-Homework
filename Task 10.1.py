def oops():
    raise IndexError
    # raise KeyError


def catch_oops():
    try:
        oops()
    except IndexError:
        print("I caught an IndexError")
    except KeyError:
        print("I caught an KeyError")


catch_oops()
