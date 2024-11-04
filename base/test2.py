import json
import datetime

class LibrarySystem:
    def __init__(self):
        self.books = []
        self.readers = []
        self.librarians = []
        self.admins = []
        self.suggestions = []
        self.activity_logs = []
        self.backup_data = {}

        # Load existing data if available
        self.load_data()

    def save_data(self):
        data = {
            "books": [book.__dict__ for book in self.books],
            "readers": [reader.__dict__ for reader in self.readers],
            "activity_logs": self.activity_logs,
            "suggestions": self.suggestions,
        }
        with open("library_data.json", "w") as file:
            json.dump(data, file, default=str)  # default=str to handle datetime serialization

    def load_data(self):
        try:
            with open("library_data.json", "r") as file:
                data = json.load(file)
                self.books = [Book(**book) for book in data.get("books", [])]
                self.readers = [Reader(**reader) for reader in data.get("readers", [])]
                self.activity_logs = data.get("activity_logs", [])
                self.suggestions = data.get("suggestions", [])
        except FileNotFoundError:
            pass  # No data to load initially

    # Example usage of save after making a change
    def add_book(self, book):
        self.books.append(book)
        self.save_data()
