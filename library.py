from exceptions import UserNoFoudError


class Library:
    def __init__(self, name) -> None:
        # Name of the library
        self.name = name

        # ------------------------------------------------
        # COMPOSITION
        # ------------------------------------------------
        # A Library *has* books and users.
        # The Library does not inherit from Book or User;
        # instead, it contains them as part of its state.
        #
        # Books and users can exist independently,
        # but the Library coordinates their interaction.
        self.books = []  # Collection of Book objects
        self.users = []  # Collection of User objects

    # ------------------------------------------------
    # Behavior: list available books
    # ------------------------------------------------
    # Iterates over all books in the library and
    # returns only the titles of those that are available.
    #
    # This method does not modify state;
    # it only queries existing data.
    def books_available(self):
        return [
            book.title  # Extract the book title
            for book in self.books
            if book.available  # Filter only available books
        ]

    def find_user(self, id_card):
        for user in self.users:
            if user.id_card == id_card:
                return user

        raise UserNoFoudError(f'User with id card: {id_card} not found')
