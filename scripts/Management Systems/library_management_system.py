import json
import os

class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                return [Book(**b) for b in data]
        return []

    def save_books(self):
        with open(self.filename, "w") as f:
            json.dump([b.__dict__ for b in self.books], f, indent=2)

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author: ")
        self.books.append(Book(book_id, title, author))
        self.save_books()
        print(f"Book '{title}' added successfully!")

    def view_books(self):
        print("\nLibrary Books:")
        for b in self.books:
            status = "Available" if b.available else "Borrowed"
            print(f"{b.book_id} | {b.title} | {b.author} | {status}")

    def borrow_book(self):
        book_id = input("Enter Book ID to borrow: ")
        for b in self.books:
            if b.book_id == book_id and b.available:
                b.available = False
                self.save_books()
                print(f"You borrowed '{b.title}'")
                return
        print("Book not available or invalid ID!")

    def return_book(self):
        book_id = input("Enter Book ID to return: ")
        for b in self.books:
            if b.book_id == book_id and not b.available:
                b.available = True
                self.save_books()
                print(f"You returned '{b.title}'")
                return
        print("Invalid Book ID or book was not borrowed!")

def main():
    library = Library()
    while True:
        print("\n--- Library Management ---")
        print("1. Add Book  2. View Books  3. Borrow Book  4. Return Book  5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            library.borrow_book()
        elif choice == "4":
            library.return_book()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
