from collections import defaultdict
from operator import attrgetter


class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

    def __str__(self):
        return f"{self.title} by {self.author}"


class Shelf:
    def __init__(self, category):
        self.category = category
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def sort_books(self):
        self.books.sort(key=attrgetter('title'))


def organize_books(books):
    shelves = defaultdict(lambda: Shelf('Uncategorized'))
    for book in books:
        shelves[book.category].add_book(book)
    return shelves


def sort_books_on_shelves(shelves):
    for shelf in shelves.values():
        shelf.sort_books()


books = [
    Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"),
    Book("To Kill a Mockingbird", "Harper Lee", "Fiction"),
    Book("The Catcher in the Rye", "J.D. Salinger", "Fiction"),
    Book("The Hobbit", "J.R.R. Tolkien", "Fantasy"),
    Book("1984", "George Orwell", "Science Fiction"),
]

shelves = organize_books(books)
sort_books_on_shelves(shelves)

for shelf in shelves.values():
    print(f"--- {shelf.category} ---")
    for book in shelf.books:
        print(book)
