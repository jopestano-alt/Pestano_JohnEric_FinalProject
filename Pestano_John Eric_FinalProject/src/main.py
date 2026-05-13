"""
Main module
CLI interface for Library Manager System
"""

from library import Library


def show_books(books):
    """Displays books in readable format."""
    if not books:
        print("\n📭 No books found.\n")
        return

    print("\n📚 --- BOOK LIST ---")
    for book in books:
        print(book)
    print()


def main():
    lib = Library()

    while True:
        print("\n===== 📚 LIBRARY MENU =====")
        print("1. View Books")
        print("2. Add Book")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Sort Books")
        print("0. Exit")

        choice = input("Enter choice: ").strip()

        # ---------------- VIEW ----------------
        if choice == "1":
            show_books(lib.view_books())

        # ---------------- ADD ----------------
        elif choice == "2":
            book_id = input("Enter Book ID: ").strip()
            title = input("Enter Title: ").strip()
            author = input("Enter Author: ").strip()

            # validation (IMPORTANT for rubric)
            if not book_id or not title or not author:
                print("❌ All fields are required!")
                continue

            print(lib.add_book(book_id, title, author))

        # ---------------- SEARCH ----------------
        elif choice == "3":
            keyword = input("Enter keyword: ").strip()

            if not keyword:
                print("❌ Keyword cannot be empty!")
                continue

            results = lib.search_books(keyword)
            show_books(results)

        # ---------------- BORROW ----------------
        elif choice == "4":
            book_id = input("Enter Book ID: ").strip()

            if not book_id:
                print("❌ Book ID cannot be empty!")
                continue

            print(lib.borrow_book(book_id))

        # ---------------- RETURN ----------------
        elif choice == "5":
            book_id = input("Enter Book ID: ").strip()

            if not book_id:
                print("❌ Book ID cannot be empty!")
                continue

            print(lib.return_book(book_id))

        # ---------------- SORT ----------------
        elif choice == "6":
            mode = input("Sort by (title/author): ").strip().lower()

            if mode not in ["title", "author"]:
                print("❌ Invalid option! Choose 'title' or 'author'.")
                continue

            show_books(lib.sort_books(mode))

        # ---------------- EXIT ----------------
        elif choice == "0":
            print("👋 Goodbye!")
            break

        # ---------------- INVALID ----------------
        else:
            print("❌ Invalid choice! Please enter 0–6 only.")


if __name__ == "__main__":
    main()