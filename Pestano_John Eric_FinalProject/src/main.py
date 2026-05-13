"""
Library Manager System
A CLI-based application for managing books and borrowing transactions.

Author: Your Name
"""

import json
import os


class Book:
    """
    Represents a single book object.
    """

    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def to_dict(self):
        """
        Converts object to dictionary.
        """
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "available": self.available
        }

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.book_id:<5} | {self.title:<30} | {self.author:<20} | {status}"


class Library:
    """
    Handles all library operations.
    """

    def __init__(self):
        self.books = []
        self.file_name = "books.json"
        self.load_books()

    def load_books(self):
        """
        Loads books from JSON file.
        """

        if not os.path.exists(self.file_name):
            return

        with open(self.file_name, "r", encoding="utf-8") as file:
            data = json.load(file)

            for item in data:
                self.books.append(
                    Book(
                        item["book_id"],
                        item["title"],
                        item["author"],
                        item["available"]
                    )
                )

    def save_books(self):
        """
        Saves books to JSON file.
        """

        data = [book.to_dict() for book in self.books]

        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def add_book(self):
        """
        Adds a new book.
        """

        try:
            book_id = len(self.books) + 1

            title = input("Enter book title: ")
            author = input("Enter author name: ")

            self.books.append(Book(book_id, title, author))

            print("\nBook added successfully!\n")

        except Exception as e:
            print(f"Error: {e}")

    def view_books(self):
        """
        Displays all books.
        """

        if not self.books:
            print("\nNo books available.\n")
            return

        print("\n========================================================================")
        print("ID    | Title                          | Author               | Status")
        print("------------------------------------------------------------------------")

        for book in self.books:
            print(book)

        print("========================================================================\n")

    def search_book(self):
        """
        Searches books by title.
        """

        keyword = input("Enter title keyword: ").lower()

        results = [
            book for book in self.books
            if keyword in book.title.lower()
        ]

        if results:
            print("\nSearch Results:\n")

            for book in results:
                print(book)

            print()

        else:
            print("\nNo matching books found.\n")

    def borrow_book(self):
        """
        Borrows a book.
        """

        try:
            book_id = int(input("Enter Book ID to borrow: "))

            for book in self.books:

                if book.book_id == book_id:

                    if book.available:
                        book.available = False
                        print("\nBook borrowed successfully!\n")

                    else:
                        print("\nBook is already borrowed.\n")

                    return

            print("\nBook not found.\n")

        except ValueError:
            print("\nInvalid input. Please enter a number.\n")

    def return_book(self):
        """
        Returns a borrowed book.
        """

        try:
            book_id = int(input("Enter Book ID to return: "))

            for book in self.books:

                if book.book_id == book_id:

                    if not book.available:
                        book.available = True
                        print("\nBook returned successfully!\n")

                    else:
                        print("\nBook was not borrowed.\n")

                    return

            print("\nBook not found.\n")

        except ValueError:
            print("\nInvalid input. Please enter a number.\n")


def display_menu():
    """
    Displays the main menu.
    """

    print("==========================================")
    print("        LIBRARY MANAGER SYSTEM")
    print("==========================================")
    print("1. View All Books")
    print("2. Add Book")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Save Data")
    print("7. Exit")
    print("==========================================")


def main():
    """
    Main application function.
    """

    library = Library()

    while True:

        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            library.view_books()

        elif choice == "2":
            library.add_book()

        elif choice == "3":
            library.search_book()

        elif choice == "4":
            library.borrow_book()

        elif choice == "5":
            library.return_book()

        elif choice == "6":
            library.save_books()
            print("\nData saved successfully!\n")

        elif choice == "7":
            library.save_books()
            print("\nThank you for using Library Manager System!")
            break

        else:
            print("\nInvalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
