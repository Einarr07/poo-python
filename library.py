from exceptions import UserNoFoudError, BookNotAvailable


# ============================================================
# CORE DOMAIN CLASS: Library
# ============================================================
# Represents a library as a central coordinator.
# This class does NOT represent a physical object,
# but a domain service that manages books and users.
#
# It demonstrates:
# - Composition
# - Object coordination
# - Domain-level validation
# - Encapsulation of business rules
class Library:

    # --------------------------------------------------------
    # Constructor
    # --------------------------------------------------------
    # Initializes the library with a name and empty collections.
    def __init__(self, name) -> None:
        # Public attribute: library name
        self.name = name

        # ----------------------------------------------------
        # COMPOSITION
        # ----------------------------------------------------
        # A Library *has* books and users.
        # The Library does not inherit from Book or User;
        # instead, it contains them.
        #
        # This allows:
        # - Loose coupling
        # - Clear responsibility boundaries
        self.books = []  # Collection of Book objects
        self.users = []  # Collection of User objects

    # --------------------------------------------------------
    # Query Behavior: available books
    # --------------------------------------------------------
    # Returns a list of books that are currently available.
    #
    # This property:
    # - Does NOT mutate state
    # - Acts as a computed view over the books collection
    @property
    def books_available(self):
        return [
            book
            for book in self.books
            if book.available  # Filters only available books
        ]

    # --------------------------------------------------------
    # Behavior: find a user by ID card
    # --------------------------------------------------------
    # Searches for a user in the library collection.
    #
    # Raises a domain-specific exception if the user
    # does not exist.
    def find_user(self, id_card):
        for user in self.users:
            if user.id_card == id_card:
                return user

        # Domain-level error: user not found
        raise UserNoFoudError(f'User with id card: {id_card} not found')

    # --------------------------------------------------------
    # Behavior: find a book by title
    # --------------------------------------------------------
    # Normalizes the input title to ensure
    # case-insensitive and whitespace-safe comparison.
    #
    # Raises a domain-specific exception if the book
    # does not exist in the library.
    def find_book(self, title: str):
        normalized = title.strip().lower()

        for book in self.books:
            if book.title.lower() == normalized:
                return book

        # Domain-level error: book not found or unavailable
        raise BookNotAvailable(f'Book with title: {title} not found')

    # --------------------------------------------------------
    # Static Method: ID validation
    # --------------------------------------------------------
    # Validates an identifier without accessing
    # instance or class state.
    #
    # Demonstrates the use of static methods
    # for utility and validation logic.
    @staticmethod
    def validated_id(id: int):
        return isinstance(id, int) and id >= 0
