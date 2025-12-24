# ------------------------------------------------
# Imports from domain modules
# ------------------------------------------------
# Book implementations
from books import PhysicalBook, DigitalBook
from exceptions import UserNoFoudError
# Library (composition root)
from library import Library
# User types and protocol for polymorphism
from users import Student, Teacher

# =================================================
# Library initialization
# =================================================
# Create a Library instance
library = Library('Las Aguas')

# =================================================
# User creation
# =================================================
# Create users with different concrete types
# (Student and Teacher) that share the same behavior
# through ApplicantProtocol
users = [
    Student(1, name="Domenica", id_card="123", subject='Math'),
    Student(3, name='Jose', id_card="456", subject='Physics'),
    Teacher(2, name="Luis", id_card="456")
]

# =================================================
# Book creation
# =================================================
# Physical books (concrete implementation of Book)
physical_books = [
    PhysicalBook(
        id=11,
        title="El santuario en la tierra",
        author="Sixto Paz",
        price=5.00,
        available=True,
        borrowed_times=0
    ),

    PhysicalBook(
        id=12,
        title="Budismo",
        author="Joshua R. Pazakiewicz",
        price=5.00,
        available=True,
        borrowed_times=0
    ),

    PhysicalBook(
        id=13,
        title="Ética para Amador",
        author="Fernando Savater",
        price=5.00,
        available=False,
        borrowed_times=0
    ),

    PhysicalBook(
        id=14,
        title="Hábitos Atómicos",
        author="James Clear",
        price=5.00,
        available=True,
        borrowed_times=0
    ),

    # Positional-argument examples
    PhysicalBook(
        1,
        '100 Años de Soledad',
        'Gabriel García Márquez',
        10.5,
        True,
        0
    ),

    PhysicalBook(
        2,
        'Principito',
        'Saint-Exupéry',
        12.3,
        False,
        0
    )
]

# Digital books (different behavior via polymorphism)
digital_books = [
    DigitalBook(1, 'Normandia', 'Norma Guatemala', 12, True, 2),
    DigitalBook(2, 'Sistemas', 'James', 56, True, 6),
    DigitalBook(3, 'La razon para estudiar', 'Erick', 56, True, 6),
    DigitalBook(4, 'Computacion', 'Henrry', 56, True, 6),
    DigitalBook(5, 'Algebra', 'Sofia', 56, True, 6)
]

# =================================================
# Composition: add books and users to the library
# =================================================
# The Library "has" books and users
library.books = physical_books + digital_books
library.users = users

print('-' * 30)
print('| Welcome to the library! |')
print('-' * 30)

print(f'We have available {len(library.books_available())} books')
for book in library.books:
    if book.available:
        print(f' ---> Title:{book.title} - Author:{book.author}')

try:
    id_card = input('Input your id card: ')
    user = library.find_user(id_card)
    print(f'{user.id_card} whit name {user.name}')
except UserNoFoudError as e:
    print(e)
    print('The user does not exist')
