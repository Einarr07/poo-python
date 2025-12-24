from typing import List

# ------------------------------------------------
# Imports from domain modules
# ------------------------------------------------
# Book implementations
from books import PhysicalBook, DigitalBook
# Library (composition root)
from library import Library
# User types and protocol for polymorphism
from users import Student, Teacher, ApplicantProtocol

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
domenica = Student(1, name="Domenica", id_card="123", subject='Math')
jose = Student(3, name='Jose', id_card="456", subject='Physics')
luis = Teacher(2, name="Luis", id_card="456")

# Polymorphic collection:
# All objects conform to ApplicantProtocol
users: List[ApplicantProtocol] = [domenica, jose, luis]

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

# =================================================
# Program execution
# =================================================
# Iterate over the polymorphic user list
# and access shared attributes
for user in users:
    print(f'name: {user.name}')
