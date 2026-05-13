"""
Library module
Handles all book operations and JSON storage
"""

import json
import os
from book import Book


class Library:
    def __init__(self, file_path="data/books.json"):
        self.file_path = file_path
        self.books = []

        # FIX: ensure folder exists (prevents your FileNotFoundError)
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        self.load_books()

    # ---------------- LOAD ----------------
    def load_books(self):
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    self.books = [Book.from_dict(b) for b in data]
            else:
                self.books = []
        except json.JSONDecodeError:
            self.books = []

    # ---------------- SAVE ----------------
    def save_books(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump([b.to_dict() for b in self.books], file, indent=4)

    # ---------------- VIEW ----------------
    def view_books(self):
        return self.books

    # ---------------- ADD ----------------
    def add_book(self, book_id, title, author):
        if any(b.book_id == book_id for b in self.books):
            return "❌ Book ID already exists!"

        self.books.append(Book(book_id, title, author))
        self.save_books()
        return "✅ Book added successfully!"

    # ---------------- SEARCH ----------------
    def search_books(self, keyword):
        return [
            b for b in self.books
            if keyword.lower() in b.title.lower()
            or keyword.lower() in b.author.lower()
        ]

    # ---------------- BORROW ----------------
    def borrow_book(self, book_id):
        for b in self.books:
            if b.book_id == book_id:
                if not b.available:
                    return "❌ Book already borrowed!"
                b.available = False
                self.save_books()
                return "✅ Book borrowed successfully!"
        return "❌ Book not found!"

    # ---------------- RETURN ----------------
    def return_book(self, book_id):
        for b in self.books:
            if b.book_id == book_id:
                if b.available:
                    return "❌ Book was not borrowed!"
                b.available = True
                self.save_books()
                return "✅ Book returned successfully!"
        return "❌ Book not found!"

    # ---------------- SORT ----------------
    def sort_books(self, mode="title"):
        if mode == "author":
            return sorted(self.books, key=lambda b: b.author.lower())
        return sorted(self.books, key=lambda b: b.title.lower())