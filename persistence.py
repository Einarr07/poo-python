import json
from datetime import datetime

from books import PhysicalBook
from library import Library
from users import Student


# ============================================================
# PERSISTENCE CLASS
# ============================================================
# Responsible for saving and loading library data to/from a JSON file.
# Demonstrates:
# - Separation of concerns (Persistence vs Business Logic)
# - Object serialization/deserialization
# - Encapsulation of file I/O
class Persistence:

    # --------------------------------------------------------
    # Constructor
    # --------------------------------------------------------
    # Initializes the persistence layer with a default file.
    def __init__(self, file="library.json") -> None:
        self.file = file

    # --------------------------------------------------------
    # Save Library Data
    # --------------------------------------------------------
    # Converts the library, users, and books into a JSON-serializable format.
    # Adds a timestamp of the save operation.
    def save_data(self, library):
        data = {
            'name': library.name,
            'users': [
                user.__dict__  # Converts user object attributes to a dictionary
                for user in library.users
            ],
            'books': [
                book.__dict__  # Converts book object attributes to a dictionary
                for book in library.books
            ],
            'save_date': datetime.now().strftime('%d/%m/%Y %H:%M:%S')  # Timestamp
        }

        # Write the data to a JSON file
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    # --------------------------------------------------------
    # Load Library Data
    # --------------------------------------------------------
    # Reads the JSON file and reconstructs Library, Book, and Student objects.
    # Demonstrates deserialization and object reconstruction.
    def load_data(self):
        with open(self.file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Recreate the Library instance
        library = Library(data['name'])

        # Reconstruct Book objects and add them to the library
        for data_book in data['books']:
            book = PhysicalBook(
                id=data_book['id'],
                title=data_book['title'],
                author=data_book['author'],
                price=data_book['price'],
                available=data_book['available'],
            )
            library.books.append(book)

        # Reconstruct Student objects and add them to the library
        for data_user in data['users']:
            user = Student(
                id=data_user['id'],
                name=data_user['name'],
                id_card=data_user['id_card'],
                subject=data_user['subject']
            )
            library.users.append(user)

        # Return the reconstructed library
        return library
