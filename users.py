from typing import Protocol, List


# -------- PROTOCOL (Polymorphism via structural typing) --------
class ApplicantProtocol(Protocol):
    def book_request(self, title: str) -> str:
        """
        Any class that wants to behave like an 'applicant'
        MUST implement this method.
        This enables polymorphism without inheritance.
        """
        ...


# -------- BASE CLASS --------
class User:
    def __init__(self, id: int, name: str, id_card: str):
        # Common attributes for all users
        self.id = id
        self.name = name
        self.id_card = id_card
        self.lend_books = []

    def book_request(self, title: str):
        """
        Default implementation for requesting a book.
        Subclasses can override this behavior.
        """
        return f'Request of book {title} successful'


# -------- CHILD CLASS (Inheritance + Polymorphism) --------
class Student(User):
    def __init__(self, id: int, name: str, id_card: str, subject: str):
        # Initialize attributes from the parent class
        super().__init__(id, name, id_card)
        self.subject = subject
        self.limit_books = 3  # Students can borrow up to 3 books

    def book_request(self, title: str):
        """
        Overrides User.book_request().
        Students can only borrow books up to their limit.
        """
        if len(self.lend_books) < self.limit_books:
            self.lend_books.append(title)
            return f'Request of book {title} successful'
        else:
            return 'You have reached the limit of 3 borrowed books'


# -------- CHILD CLASS (Inheritance + Polymorphism) --------
class Teacher(User):
    def __init__(self, id: int, name: str, id_card: str):
        # Initialize attributes from the parent class
        super().__init__(id, name, id_card)
        self.limit_books = None  # Teachers have no limit

    def book_request(self, title: str):
        """
        Overrides User.book_request().
        Teachers can request books without restrictions.
        """
        return f'Request of book {title} successful'


# -------- OBJECT CREATION --------
domenica = Student(1, name="Domenica", id_card="123", subject='Math')
jose = Student(3, name='Jose', id_card="456", subject='Physics')
luis = Teacher(2, name="Luis", id_card="456")

# -------- POLYMORPHISM IN ACTION --------
# All objects in this list implement ApplicantProtocol
users: List[ApplicantProtocol] = [domenica, jose, luis]

# The same method call works for different object types
# Each object responds according to its own implementation
for user in users:
    print(user.book_request('Politica para Amador'))
