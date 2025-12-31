from typing import Protocol

from exceptions import BookNotAvailable


# ============================================================
# PROTOCOL (Structural Typing / Polymorphism)
# ============================================================
# This protocol defines the behavior that any "Book-like"
# object must implement.
# Classes do NOT need to inherit from this protocol explicitly,
# they just need to implement the required methods.
class BookProtocol(Protocol):

    def lend(self) -> str:
        ...

    def return_book(self) -> str:
        ...

    def duration_calculate(self) -> str:
        ...


# ============================================================
# BASE CLASS: Book
# Represents a generic book in the system
# ============================================================
class Book:

    # --------------------------------------------------------
    # Constructor
    # Initializes the internal state of the Book object
    # --------------------------------------------------------
    def __init__(
            self,
            id: int,
            title: str,
            author: str,
            price: float,
            available: bool = True,
    ):
        # Public attributes (can be accessed directly)
        self.id = id  # Unique identifier
        self.title = title  # Book title
        self.author = author  # Book author
        self.price = price  # Book price
        self.available = available  # Availability status

        # Private attribute (Encapsulation)
        # Tracks how many times the book has been borrowed
        self.__borrowed_times = 0

    @classmethod
    def create_not_available(
            cls,
            id: int,
            title: str,
            author: str,
            price: float,
    ) -> 'Book':
        return cls(
            id, title, author, price, available=False
        )

    # --------------------------------------------------------
    # Behavior: lend the book
    # Changes availability and updates borrow counter
    # --------------------------------------------------------
    def lend(self):
        if not self.available:
            raise BookNotAvailable(f'{self.title} was not available')

        if self.available:
            self.available = False
            self.__borrowed_times += 1
            return (
                f'{self.title} was lent successfully. '
                f'Total lends: {self.__borrowed_times}'
            )
        return f'{self.title} is unavailable'

    # --------------------------------------------------------
    # Behavior: return the book
    # Makes the book available again
    # --------------------------------------------------------
    def return_book(self):
        if not self.available:
            self.available = True
        return f'{self.title} was returned successfully.'

    # --------------------------------------------------------
    # Business logic method
    # Determines if the book is considered "popular"
    # --------------------------------------------------------
    @property
    def is_popular(self):
        return self.__borrowed_times > 5

    # --------------------------------------------------------
    # String representation
    # Helps when printing or debugging objects
    # --------------------------------------------------------
    def __str__(self):
        return (
            f'{self.id} - {self.title} - {self.author} - '
            f'{self.price} - Available: {self.available}'
        )

    # --------------------------------------------------------
    # Getter (Encapsulation)
    # Provides controlled read access to private attribute
    # --------------------------------------------------------
    @property
    def borrowed_times(self):
        return self.__borrowed_times

    # --------------------------------------------------------
    # Setter (Encapsulation)
    # Provides controlled write access to private attribute
    # --------------------------------------------------------

    @borrowed_times.setter
    def borrowed_times(self, value):
        if value > 0:
            self.__borrowed_times = value
        raise ValueError('The value of borrowed_times must be positive')

    @property
    def all_description(self):
        return f'{self.title} by {self.author} -> Price: ${self.price}'


# ============================================================
# CHILD CLASS: PhysicalBook
# Inherits from Book and customizes behavior
# ============================================================
class PhysicalBook(Book):

    # Polymorphic method
    # Physical books have a shorter loan duration
    def duration_calculate(self):
        return "7 days"


# ============================================================
# CHILD CLASS: DigitalBook
# Inherits from Book and customizes behavior
# ============================================================
class DigitalBook(Book):

    # Polymorphic method
    # Digital books can be borrowed for a longer period
    def duration_calculate(self):
        return "14 days"
