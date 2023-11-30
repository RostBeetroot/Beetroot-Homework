class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author({self.name}, {self.country}, {self.birthday})"

    def __str__(self):
        return f"{self.name} ({self.birthday}), {self.country}"


class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.total_books += 1
        author.books.append(self)

    def __repr__(self):
        return f"Book({self.name}, {self.year}, {self.author})"

    def __str__(self):
        return f"{self.name} ({self.year}) by {self.author.name}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        new_book = Book(name, year, author)
        self.books.append(new_book)
        if author not in self.authors:
            self.authors.append(author)
        return new_book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library({self.name}, Books: {len(self.books)}, Authors: {len(self.authors)})"

    def __str__(self):
        return f"{self.name} Library"


# Create authors

author1 = Author("Jack", "USA", "01-01-1990")
author2 = Author("Tom", "Canada", "02-02-1980")

# Create a library
library = Library("Beetroot")
print(library)

# Add books to the library
book1 = library.new_book("Book 1", 2000, author1)
book2 = library.new_book("Book 2", 2005, author2)
book3 = library.new_book("Book 3", 2002, author1)

# Group books by author and year
print(library.group_by_author(author1))
print(library.group_by_year(2005))
