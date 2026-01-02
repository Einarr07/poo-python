from typing import Protocol

from exceptions import BookNotAvailable


# ============================================================
# PROTOCOL (Structural Typing / Polymorphism)
# ============================================================
# This protocol defines a "contract" for book-like objects.
# Any class that implements these methods can be treated as a Book,
# even if it does NOT explicitly inherit from this protocol.
#
# This is an example of structural typing and interface-based design.
class BookProtocol(Protocol):

    def lend(self) -> str:
        """Defines the behavior for lending a book"""
        ...

    def return_book(self) -> str:
        """Defines the behavior for returning a book"""
        ...

    def duration_calculate(self) -> str:
        """Defines how long the book can be borrowed"""
        ...


# ============================================================
# BASE CLASS: Book
# ============================================================
# Represents a generic book in the library system.
# This class demonstrates:
# - Encapsulation
# - Class methods
# - Properties
# - Business logic inside objects
class Book:

    # --------------------------------------------------------
    # Constructor
    # --------------------------------------------------------
    # Initializes the internal state of a Book object.
    # This method sets both public and private attributes.
    def __init__(
            self,
            id: int,
            title: str,
            author: str,
            price: float,
            available: bool = True,
    ):
        # Public attributes
        self.id = id  # Unique identifier for the book
        self.title = title  # Book title
        self.author = author  # Book author
        self.price = price  # Book price
        self.available = available  # Indicates if the book can be borrowed

        # Private attribute (Encapsulation)
        # Keeps track of how many times the book has been borrowed
        self.__borrowed_times = 0

    # --------------------------------------------------------
    # Class Method
    # --------------------------------------------------------
    # Factory method that creates a Book instance
    # already marked as unavailable.
    @classmethod
    def create_not_available(
            cls,
            id: int,
            title: str,
            author: str,
            price: float,
    ) -> 'Book':
        return cls(
            id=id,
            title=title,
            author=author,
            price=price,
            available=False
        )

    # --------------------------------------------------------
    # Behavior: lend the book
    # --------------------------------------------------------
    # - Validates availability
    # - Updates internal state
    # - Demonstrates exception handling
    def lend(self):
        if not self.available:
            # Domain-specific exception
            raise BookNotAvailable(f'{self.title} was not available')

        self.available = False
        self.__borrowed_times += 1

        return (
            f'{self.title} was lent successfully. '
            f'Total lends: {self.__borrowed_times}'
        )

    # --------------------------------------------------------
    # Behavior: return the book
    # --------------------------------------------------------
    # Restores availability of the book.
    def return_book(self):
        if not self.available:
            self.available = True
        return f'{self.title} was returned successfully.'

    # --------------------------------------------------------
    # Computed Property (Business Rule)
    # --------------------------------------------------------
    # Determines whether a book is "popular"
    # based on how many times it was borrowed.
    @property
    def is_popular(self):
        return self.__borrowed_times > 5

    # --------------------------------------------------------
    # String Representation
    # --------------------------------------------------------
    # Improves readability when printing the object
    # or debugging.
    def __str__(self):
        return (
            f'{self.id} - {self.title} - {self.author} - '
            f'{self.price} - Available: {self.available}'
        )

    # --------------------------------------------------------
    # Getter (Encapsulation)
    # --------------------------------------------------------
    # Provides read-only access to a private attribute.
    @property
    def borrowed_times(self):
        return self.__borrowed_times

    # --------------------------------------------------------
    # Setter (Encapsulation)
    # --------------------------------------------------------
    # Controls how the private attribute can be modified.
    # This enforces validation rules.
    @borrowed_times.setter
    def borrowed_times(self, value):
        if value > 0:
            self.__borrowed_times = value
            return
        raise ValueError('The value of borrowed_times must be positive')

    # --------------------------------------------------------
    # Additional Read-Only Property
    # --------------------------------------------------------
    # Returns a human-readable description of the book.
    @property
    def all_description(self):
        return f'{self.title} by {self.author} -> Price: ${self.price}'


# ============================================================
# CHILD CLASS: PhysicalBook
# ============================================================
# Inherits from Book and overrides behavior.
# Demonstrates inheritance and polymorphism.
class PhysicalBook(Book):

    # --------------------------------------------------------
    # Polymorphic Method
    # --------------------------------------------------------
    # Physical books have a shorter loan period.
    def duration_calculate(self):
        return "7 days"


# ============================================================
# CHILD CLASS: DigitalBook
# ============================================================
# Inherits from Book and customizes behavior.
class DigitalBook(Book):

    # --------------------------------------------------------
    # Polymorphic Method
    # --------------------------------------------------------
    # Digital books allow longer borrowing periods.
    def duration_calculate(self):
        return "14 days"
