from books import PhysicalBook
from users import Student

# ============================================================
# DATA INITIALIZATION MODULE
# ============================================================
# This file is responsible for creating sample data used
# throughout the application.
# It helps separate data creation from business logic,
# following the Single Responsibility Principle (SRP).


# ============================================================
# BOOK INSTANCES CREATION
# ============================================================
# Each object represents a PhysicalBook instance.
# This demonstrates:
# - Object instantiation
# - Constructor usage
# - Inheritance (PhysicalBook -> Book)
book1 = PhysicalBook(1, "Cien años de soledad", "Gabriel García Márquez", 25.50)
book2 = PhysicalBook(2, "1984", "George Orwell", 18.90)
book3 = PhysicalBook(3, "El Principito", "Antoine de Saint-Exupéry", 12.00)
book4 = PhysicalBook(4, "Don Quijote de la Mancha", "Miguel de Cervantes", 30.00)
book5 = PhysicalBook(5, "Orgullo y Prejuicio", "Jane Austen", 15.75)
book6 = PhysicalBook(6, "El Hobbit", "J.R.R. Tolkien", 22.00)
book7 = PhysicalBook(7, "Crónica de una muerte anunciada", "Gabriel García Márquez", 14.20)
book8 = PhysicalBook(8, "Fahrenheit 451", "Ray Bradbury", 16.50)
book9 = PhysicalBook(9, "Rayuela", "Julio Cortázar", 21.00)
book10 = PhysicalBook(10, "El resplandor", "Stephen King", 19.99)

# ============================================================
# STUDENT INSTANCES CREATION
# ============================================================
# Each object represents a Student instance.
# This demonstrates:
# - Object creation from a custom class
# - Passing domain-specific attributes
# - Composition (students will interact with books)
student1 = Student(1, "Alejandro Ruiz", "STU001", "Ingeniería de Software")
student2 = Student(2, "Mariana López", "STU002", "Medicina")
student3 = Student(3, "Carlos Mendoza", "STU003", "Derecho")
student4 = Student(4, "Lucía Fernández", "STU004", "Psicología")
student5 = Student(5, "Roberto Gómez", "STU005", "Arquitectura")
student6 = Student(6, "Elena Torres", "STU006", "Diseño Gráfico")
student7 = Student(7, "Mateo Rivas", "STU007", "Economía")
student8 = Student(8, "Sofía Castro", "STU008", "Biología")
student9 = Student(9, "Diego Herrera", "STU009", "Historia")
student10 = Student(10, "Valeria Ortiz", "STU010", "Filosofía")

# ============================================================
# DATA COLLECTIONS
# ============================================================
# Lists group objects of the same type.
# These collections are typically passed to other layers
# (library, persistence, services) for processing.

# Collection of book objects
data_books = [
    book1, book2, book3, book4, book5,
    book6, book7, book8, book9, book10
]

# Collection of student objects
data_students = [
    student1, student2, student3, student4, student5,
    student6, student7, student8, student9, student10
]
