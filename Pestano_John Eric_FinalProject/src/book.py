"""
Book module
Represents a single book object in the Library Manager System.
"""

class Book:
    """
    A class that represents a book in the library system.
    """

    def __init__(self, book_id, title, author, available=True):
        """
        Initialize a Book object.

        Args:
            book_id (str): Unique ID of the book
            title (str): Title of the book
            author (str): Author of the book
            available (bool): Availability status
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    # ---------------- CONVERT TO DICTIONARY ----------------
    def to_dict(self):
        """
        Converts Book object to dictionary (for JSON storage).
        """
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "available": self.available
        }

    # ---------------- CREATE FROM DICTIONARY ----------------
    @staticmethod
    def from_dict(data):
        """
        Creates Book object from dictionary (loaded from JSON).
        """
        return Book(
            data["book_id"],
            data["title"],
            data["author"],
            data.get("available", True)
        )

    # ---------------- STRING REPRESENTATION ----------------
    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"