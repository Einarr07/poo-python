# Book class definition
# This class represents a book with basic attributes
class Book:

    # Constructor method
    # It initializes the attributes of the Book object
    def __init__(self, id: int, title: str, author: str, price: float, available: bool):
        self.id = id              # Unique identifier for the book
        self.title = title        # Title of the book
        self.author = author      # Author of the book
        self.price = price        # Price of the book
        self.available = available  # Availability status (True if available, False otherwise)


# List of Book objects (book catalog)
catalogo = [
    Book(id=11, title="El santuario en la tiera", author="Sixto Paz", price=5.00, available=True),
    Book(id=12, title="Budismo", author="Joshua R. Pazakiewicz", price=5.00, available=True),
    Book(id=13, title="Etica para amador", author="Fernando Savater", price=5.00, available=True),
    Book(id=14, title="Habitos atomicos", author="James Clear", price=5.00, available=True),
]

# Iterate over the catalog and display basic book information
for book in catalogo:
    print(f'{book.id} - {book.title} - {book.author}')


# Creating individual Book instances
one_hundred = Book(
    1,
    '100 Años de soledad',
    'Gabriel Garcia Marquez',
    price=10.5,
    available=True
)

principito = Book(
    2,
    'Principito',
    'Saint-Exupéry',
    price=12.3,
    available=False
)

# Display selected book information (view layer)
print(f'{one_hundred.title} - {one_hundred.author}')
print(f'{principito.title} - {principito.author}')
