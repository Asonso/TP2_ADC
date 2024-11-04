from library_system import LibrarySystem


def main():
    system = LibrarySystem()
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Admin Menu")
        print("2. Librarian Menu")
        print("3. Reader Menu")
        print("4. Exit")
        choice = input("Select an option: ")
        
        if choice == "1":
            admin_menu(system)
        elif choice == "2":
            librarian_menu(system)
        elif choice == "3":
            reader_menu(system)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def admin_menu(system):
    print("\n--- Admin Menu ---")
    print("1. Add User")
    print("2. Configure Reminders")
    print("3. Backup Data")
    print("4. Restore Data")
    print("5. Monitor System Performance")
    choice = input("Select an option: ")

    if choice == "1":
        name = input("Enter user name: ")
        role = input("Enter role (Admin/Librarian/Reader): ")
        user = {"name": name}
        system.add_user(user, role)
    elif choice == "2":
        print(system.send_return_reminders())
    elif choice == "3":
        print(system.backup_data_system())
    elif choice == "4":
        print(system.restore_data())
    elif choice == "5":
        print(system.monitor_system_performance())
    else:
        print("Invalid choice.")

def librarian_menu(system):
    print("\n--- Librarian Menu ---")
    print("1. Add Book")
    print("2. Generate Monthly Report")
    print("3. Check Inventory")
    choice = input("Select an option: ")

    if choice == "1":
        book_id = input("Enter book ID: ")
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        category = input("Enter book category: ")
        book = Book(book_id, title, author, category)
        system.add_book(book)
    elif choice == "2":
        print(system.generate_monthly_report())
    elif choice == "3":
        print(system.check_inventory())
    else:
        print("Invalid choice.")

def reader_menu(system):
    print("\n--- Reader Menu ---")
    print("1. View Account")
    print("2. Suggest a Book")
    choice = input("Select an option: ")

    if choice == "1":
        reader_id = input("Enter your reader ID: ")
        print(system.view_account(reader_id))
    elif choice == "2":
        reader_id = input("Enter your reader ID: ")
        title = input("Enter book title: ")
        author = input("Enter author: ")
        print(system.suggest_book(reader_id, title, author))
    else:
        print("Invalid choice.")

    


if __name__ == "__main__":
    main()
