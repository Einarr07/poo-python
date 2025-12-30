from abc import ABC, abstractmethod
from typing import Protocol

from exceptions import InvalidTitleError


# ============================================================
# PROTOCOL (Polymorphism via structural typing)
# ============================================================
# A Protocol defines a "contract".
# Any class that implements the required methods
# can be used polymorphically, even without inheritance.
class ApplicantProtocol(Protocol):

    def book_request(self, title: str) -> str:
        """
        Any class that wants to act as an 'Applicant'
        MUST implement this method.

        This allows polymorphism without requiring
        a shared base class.
        """
        ...


class BaseUser(ABC):

    @abstractmethod
    def book_request(self):
        pass


# ============================================================
# BASE CLASS
# ============================================================
# The User class represents a generic user of the system.
# It provides common attributes and default behavior.
class User(BaseUser):

    def __init__(self, id: int, name: str, id_card: str):
        # Unique identifier of the user
        self.id = id

        # User's full name
        self.name = name

        # Identification card number
        self.id_card = id_card

        # List to keep track of borrowed books
        self.lend_books = []

    def book_request(self, title: str):
        """
        Default implementation for requesting a book.

        This method can be overridden by subclasses
        to apply specific rules.
        """
        return f'Request of book {title} successful'


# ============================================================
# CHILD CLASS: Student (Inheritance + Polymorphism)
# ============================================================
# Student inherits from User and customizes behavior.
class Student(User):

    def __init__(self, id: int, name: str, id_card: str, subject: str):
        # Call the parent constructor to reuse initialization logic
        super().__init__(id, name, id_card)

        # Student's academic subject
        self.subject = subject

        # Maximum number of books a student can borrow
        self.limit_books = 3

    def book_request(self, title: str):
        """
        Overrides User.book_request().

        Students are limited to a maximum number
        of borrowed books.
        """

        if not title:
            raise InvalidTitleError('Please provide a title')

        if len(self.lend_books) < self.limit_books:
            # Add the book to the borrowed list
            self.lend_books.append(title)
            return f'Request of book {title} successful'
        else:
            # Deny the request if the limit is reached
            return 'You have reached the limit of 3 borrowed books'


# ============================================================
# CHILD CLASS: Teacher (Inheritance + Polymorphism)
# ============================================================
# Teacher also inherits from User but has different rules.
class Teacher(User):

    def __init__(self, id: int, name: str, id_card: str):
        # Initialize shared attributes from User
        super().__init__(id, name, id_card)

        # Teachers do not have a borrowing limit
        self.limit_books = None

    def book_request(self, title: str):
        """
        Overrides User.book_request().

        Teachers can request books without restrictions.
        """
        return f'Request of book {title} successful'
