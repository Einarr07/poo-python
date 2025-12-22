# Book class definition
# This class represents a book and demonstrates OOP concepts such as
# encapsulation, methods, and object state management
class Book:

    # Constructor method
    # Initializes all attributes when a Book object is created
    def __init__(self, id: int, title: str, author: str,
                 price: float, available: bool, borrowed_times: int):
        self.id = id  # Unique identifier of the book
        self.title = title  # Book title
        self.author = author  # Book author
        self.price = price  # Book price
        self.available = available  # Availability status

        # Private attribute (encapsulation)
        # The double underscore makes this attribute harder to access directly
        # from outside the class
        self.__borrowed_times = borrowed_times

    # Method to lend a book
    # Changes availability and increases the borrow counter
    def lend(self):
        if self.available:
            self.available = False
            self.__borrowed_times += 1
            return f'{self.title} was lent successfully. Total lends: {self.__borrowed_times}'
        return f'{self.title} is unavailable'

    # Method to return a book
    # Makes the book available again
    def return_book(self):
        if not self.available:
            self.available = True
        return f'{self.title} was returned successfully.'

    # Method to check if a book is popular
    # A book is considered popular if it was borrowed more than 5 times
    def is_popular(self):
        return self.__borrowed_times > 5

    # String representation of the object
    # This method is automatically called when printing the object
    def __str__(self):
        return f'{self.id} - {self.title} - {self.author} - {self.price} - Available: {self.available}'

    # Getter method
    # Allows controlled access to the private attribute
    def get_borrowed_times(self):
        return self.__borrowed_times

    # Setter method
    # Allows controlled modification of the private attribute
    def set_borrowed_times(self, value):
        self.__borrowed_times = value


# List of Book objects (book catalog)
# This simulates a collection of books in a library
catalogo = [
    Book(id=11, title="El santuario en la tiera", author="Sixto Paz",
         price=5.00, available=True, borrowed_times=0),
    Book(id=12, title="Budismo", author="Joshua R. Pazakiewicz",
         price=5.00, available=True, borrowed_times=0),
    Book(id=13, title="Etica para amador", author="Fernando Savater",
         price=5.00, available=False, borrowed_times=0),
    Book(id=14, title="Habitos atomicos", author="James Clear",
         price=5.00, available=True, borrowed_times=0),
]

# Creating individual Book instances
one_hundred = Book(
    1,
    '100 Años de soledad',
    'Gabriel Garcia Marquez',
    price=10.5,
    available=True,
    borrowed_times=0
)

principito = Book(
    2,
    'Principito',
    'Saint-Exupéry',
    price=12.3,
    available=False,
    borrowed_times=0
)

# Lending and returning books
print(one_hundred.lend())
print(principito.return_book())

# Using setter and getter methods
one_hundred.set_borrowed_times(5)
print(f'{one_hundred.title} was borrowed {one_hundred.get_borrowed_times()} times')

# Adding books to the catalog
catalogo.append(one_hundred)
catalogo.append(principito)

# Displaying all books in the catalog
for book in catalogo:
    print(book)
