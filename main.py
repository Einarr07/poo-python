# ============================================
# Book Management System
# Demonstrates OOP concepts:
# - Encapsulation
# - Inheritance
# - Polymorphism
# - Composition
# ============================================

from typing import Protocol


# --------------------------------------------
# Protocol (Interface-like behavior)
# Defines the methods that a Book-type object
# must implement
# --------------------------------------------
class BookProtocol(Protocol):
    def lend(self) -> str:
        ...

    def return_book(self) -> str:
        ...

    def duration_calculate(self) -> str:
        ...


# --------------------------------------------
# Base Book class
# Represents a generic book
# --------------------------------------------
class Book:

    # Constructor
    # Initializes the state of the Book object
    def __init__(self, id: int, title: str, author: str,
                 price: float, available: bool, borrowed_times: int):
        self.id = id  # Unique book identifier
        self.title = title  # Book title
        self.author = author  # Book author
        self.price = price  # Book price
        self.available = available  # Availability status

        # Private attribute (Encapsulation)
        # Keeps track of how many times the book was borrowed
        self.__borrowed_times = borrowed_times

    # ----------------------------------------
    # Behavior: lend the book
    # Updates availability and borrow counter
    # ----------------------------------------
    def lend(self):
        if self.available:
            self.available = False
            self.__borrowed_times += 1
            return f'{self.title} was lent successfully. Total lends: {self.__borrowed_times}'
        return f'{self.title} is unavailable'

    # ----------------------------------------
    # Behavior: return the book
    # Makes the book available again
    # ----------------------------------------
    def return_book(self):
        if not self.available:
            self.available = True
        return f'{self.title} was returned successfully.'

    # ----------------------------------------
    # Business logic method
    # Determines if the book is popular
    # ----------------------------------------
    def is_popular(self):
        return self.__borrowed_times > 5

    # ----------------------------------------
    # String representation
    # Useful for debugging and printing
    # ----------------------------------------
    def __str__(self):
        return f'{self.id} - {self.title} - {self.author} - {self.price} - Available: {self.available}'

    # ----------------------------------------
    # Getter (Encapsulation)
    # Controlled access to private attribute
    # ----------------------------------------
    def get_borrowed_times(self):
        return self.__borrowed_times

    # ----------------------------------------
    # Setter (Encapsulation)
    # Controlled modification of private attribute
    # ----------------------------------------
    def set_borrowed_times(self, value):
        self.__borrowed_times = value


# --------------------------------------------
# Inheritance
# Physical book specialization
# --------------------------------------------
class FisicBook(Book):
    def duration_calculate(self):
        return "7 days"


# --------------------------------------------
# Inheritance
# Digital book specialization
# --------------------------------------------
class DigitalBook(Book):
    def duration_calculate(self):
        return "14 days"


# --------------------------------------------
# BookStore class
# Demonstrates COMPOSITION
# --------------------------------------------
class BookStore:
    def __init__(self, name) -> None:
        self.name = name

        # COMPOSITION:
        # A BookStore HAS books and users
        # Books can exist independently from BookStore,
        # but BookStore uses them as part of its behavior
        self.books = []
        self.users = []

    # ----------------------------------------
    # Returns a list of available book titles
    # ----------------------------------------
    def books_available(self):
        return [
            book.title
            for book in self.books
            if book.available
        ]


# --------------------------------------------
# Book catalog (Aggregation of Book objects)
# --------------------------------------------
catalogo = [
    Book(id=11, title="El santuario en la tierra", author="Sixto Paz",
         price=5.00, available=True, borrowed_times=0),

    Book(id=12, title="Budismo", author="Joshua R. Pazakiewicz",
         price=5.00, available=True, borrowed_times=0),

    Book(id=13, title="Ética para Amador", author="Fernando Savater",
         price=5.00, available=False, borrowed_times=0),

    Book(id=14, title="Hábitos Atómicos", author="James Clear",
         price=5.00, available=True, borrowed_times=0),

    Book(
        1,
        '100 Años de Soledad',
        'Gabriel García Márquez',
        10.5,
        True,
        0
    ),

    Book(
        2,
        'Principito',
        'Saint-Exupéry',
        12.3,
        False,
        0
    )
]

# --------------------------------------------
# Creating a BookStore instance
# --------------------------------------------
library = BookStore('Las Aguas')

# COMPOSITION in action:
# The BookStore uses Book objects to perform operations
library.books = catalogo

# Display available books
print(library.books_available())
