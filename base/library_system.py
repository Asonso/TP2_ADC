import datetime

# Enum for user roles
class Role:
    ADMIN = "Admin"
    LIBRARIAN = "Librarian"
    READER = "Reader"

# Updated LibrarySystem class
class LibrarySystem:
    def __init__(self):
        self.books = []
        self.readers = []
        self.librarians = []
        self.admins = []
        self.suggestions = []
        self.activity_logs = []
        self.backup_data = {}

    # Access Level Management
    def add_user(self, user, role):
        if role == Role.ADMIN:
            self.admins.append(user)
        elif role == Role.LIBRARIAN:
            self.librarians.append(user)
        elif role == Role.READER:
            self.readers.append(user)
        else:
            print("Invalid role specified.")

    # Generate Monthly Report (for Librarian)
    def generate_monthly_report(self):
        # This could include book borrow/return logs, reader activity, etc.
        report = {
            "total_books": len(self.books),
            "total_readers": len(self.readers),
            "total_librarians": len(self.librarians),
            "suggestions": self.suggestions,
            "logs": self.activity_logs
        }
        self.activity_logs.append(f"Monthly report generated on {datetime.datetime.now()}")
        return report

    # Reader Online Access: Account Info and Loan History
    def view_account(self, reader_id):
        reader = self.find_reader(reader_id)
        if reader:
            return {
                "name": reader.name,
                "borrowed_books": reader.borrowed_books
            }
        return "Reader not found."

    # Automatic Return Reminders
    def send_return_reminders(self):
        reminders = []
        for reader in self.readers:
            for book in reader.borrowed_books:
                # Assuming each book has a 'due_date' attribute
                if book.due_date <= datetime.date.today() + datetime.timedelta(days=3):
                    reminders.append(f"Reminder sent to {reader.name} for book {book.title}")
        self.activity_logs.extend(reminders)
        return reminders

    # Book Suggestion (Reader functionality)
    def suggest_book(self, reader_id, book_title, author):
        reader = self.find_reader(reader_id)
        if reader:
            suggestion = {"reader_id": reader_id, "title": book_title, "author": author}
            self.suggestions.append(suggestion)
            self.activity_logs.append(f"Book suggestion added by {reader.name}: {book_title} by {author}")
            return "Suggestion added."
        return "Reader not found."

    # Backup System Data
    def backup_data_system(self):
        # Simplified: Back up essential data structures
        self.backup_data = {
            "books": self.books.copy(),
            "readers": self.readers.copy(),
            "suggestions": self.suggestions.copy(),
            "activity_logs": self.activity_logs.copy()
        }
        self.activity_logs.append(f"System backup created on {datetime.datetime.now()}")
        return "Backup created."

    # Restore System Data
    def restore_data(self):
        if self.backup_data:
            self.books = self.backup_data.get("books", [])
            self.readers = self.backup_data.get("readers", [])
            self.suggestions = self.backup_data.get("suggestions", [])
            self.activity_logs = self.backup_data.get("activity_logs", [])
            self.activity_logs.append(f"System data restored on {datetime.datetime.now()}")
            return "Data restored from backup."
        return "No backup data found."

    # System Performance Monitoring (Basic Example)
    def monitor_system_performance(self):
        # For simplicity, we assume these are some performance metrics
        performance = {
            "total_books": len(self.books),
            "total_readers": len(self.readers),
            "activity_logs": len(self.activity_logs)
        }
        self.activity_logs.append(f"System performance checked on {datetime.datetime.now()}")
        return performance

    # Inventory Notification
    def check_inventory(self):
        notifications = []
        for book in self.books:
            # Assuming each book has a 'stock' attribute
            if book.stock == 0:
                notifications.append(f"Book out of stock: {book.title}")
            elif book.stock < 0:
                notifications.append(f"Book missing: {book.title}")
        self.activity_logs.extend(notifications)
        return notifications


    