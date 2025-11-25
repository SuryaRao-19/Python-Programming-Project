# main.py

from book import Book
from inventory import LibraryInventory

inventory = LibraryInventory()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book by Title")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")

        new_book = Book(title, author, isbn)
        inventory.add_book(new_book)
        print("Book added successfully!")

    elif choice == "2":
        isbn = input("Enter ISBN to issue: ")
        book = inventory.find_by_isbn(isbn)
        if book and book.issue():
            inventory.save_books()
            print("Book issued!")
        else:
            print("Book not available or not found.")

    elif choice == "3":
        isbn = input("Enter ISBN to return: ")
        book = inventory.find_by_isbn(isbn)
        if book and book.return_book():
            inventory.save_books()
            print("Book returned!")
        else:
            print("Book not found or already returned.")

    elif choice == "4":
        inventory.show_all()

    elif choice == "5":
        title = input("Enter title search keyword: ")
        results = inventory.search_by_title(title)
        if results:
            for b in results:
                print(b)
        else:
            print("No books found.")

    elif choice == "6":
        print("Thank you for using the Library Inventory!")
        break

    else:
        print("Invalid choice. Try again.")
