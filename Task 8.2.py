country = input("Enter country’s name: ")
capital = input("Enter it's capital: ")


def make_country(country1, capital1):
    my_book = {}
    my_book.update({country1: capital1})
    return my_book


print(make_country(country, capital))
