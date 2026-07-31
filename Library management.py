books = []

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")

        book = {
            "title": title,
            "author": author
        }

        books.append(book)
        print("Book added successfully!")

    elif choice == "2":
        if len(books) == 0:
            print("No books found.")
        else:
            print("\nBooks in the Library:")
            for book in books:
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("----------------------")

    elif choice == "3":
        search = input("Enter book title to search: ")

        found = False

        for book in books:
            if book["title"].lower() == search.lower():
                print("\nBook Found!")
                print("Title:", book["title"])
                print("Author:", book["author"])
                found = True
                break

        if found == False:
            print("Book not found.")

    elif choice == "4":
        delete = input("Enter book title to delete: ")

        found = False

        for book in books:
            if book["title"].lower() == delete.lower():
                books.remove(book)
                print("Book deleted successfully!")
                found = True
                break

        if found == False:
            print("Book not found.")

    elif choice == "5":
        print("Thank you for using the Library Management System.")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 5.")