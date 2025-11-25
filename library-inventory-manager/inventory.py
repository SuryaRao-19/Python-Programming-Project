# inventory.py

import json
from book import Book

class LibraryInventory:
    def __init__(self, file_name="books.json"):
        self.file_name = file_name
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open(self.file_name, "r") as f:
                data = json.load(f)
                self.books = [Book(**item) for item in data]
        except:
            self.books = []
            self.save_books()

    def save_books(self):
        with open(self.file_name, "w") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=4)

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def find_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def show_all(self):
        if len(self.books) == 0:
            print("No books available.")
        for b in self.books:
            print(b)
