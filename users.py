from abc import ABC, abstractmethod
from typing import Protocol

from exceptions import InvalidTitleError


# ============================================================
# PROTOCOL (Polymorphism via structural typing)
# ============================================================
# A Protocol defines a "contract".
# Any class implementing the required methods
# can be used polymorphically, even without inheritance.
class ApplicantProtocol(Protocol):

    def book_request(self, title: str) -> str:
        """
        Contract method: any class acting as an Applicant
        must implement this method.

        Enables polymorphism without a shared base class.
        """
        ...


# ============================================================
# ABSTRACT BASE CLASS
# ============================================================
# BaseUser is an abstract class that enforces
# that all subclasses implement certain methods.
class BaseUser(ABC):

    @abstractmethod
    def book_request(self):
        """Subclasses must provide their own implementation."""
        pass


# ============================================================
# BASE CLASS: User
# ============================================================
# Represents a generic system user.
# Provides shared attributes and default behavior.
class User(BaseUser):

    def __init__(self, id: int, name: str, id_card: str):
        # Unique system identifier
        self.id = id

        # User's full name
        self.name = name

        # Identification card number
        self.id_card = id_card

        # List to track borrowed books
        self.lend_books = []

    def book_request(self, title: str):
        """
        Default book request behavior.
        Can be overridden by subclasses for specific rules.
        """
        return f'Request of book {title} successful'

    @property
    def full_name(self):
        """Returns a formatted string with user ID and name."""
        return f'{self.id_card} with name {self.name}'


# ============================================================
# CHILD CLASS: Student
# ============================================================
# Inherits from User and applies specific borrowing rules.
# Demonstrates:
# - Inheritance
# - Polymorphism (overriding methods)
class Student(User):

    def __init__(self, id: int, name: str, id_card: str, subject: str):
        # Reuse parent initialization
        super().__init__(id, name, id_card)

        # Academic subject of the student
        self.subject = subject

        # Maximum books a student can borrow
        self.limit_books = 3

    def book_request(self, title: str):
        """
        Overrides User.book_request().

        Students are limited to a maximum number of borrowed books.
        Validates input and enforces borrowing limit.
        """
        if not title:
            raise InvalidTitleError('Please provide a title')

        if len(self.lend_books) < self.limit_books:
            # Borrow the book
            self.lend_books.append(title)
            return f'Request of book {title} successful'
        else:
            # Deny request if limit reached
            return 'You have reached the limit of 3 borrowed books'


# ============================================================
# CHILD CLASS: Teacher
# ============================================================
# Inherits from User but has no borrowing limit.
# Demonstrates polymorphic behavior with different rules.
class Teacher(User):

    def __init__(self, id: int, name: str, id_card: str):
        # Initialize shared attributes
        super().__init__(id, name, id_card)

        # No borrowing limit for teachers
        self.limit_books = None

    def book_request(self, title: str):
        """
        Overrides User.book_request().

        Teachers can request books without restriction.
        """
        return f'Request of book {title} successful'
