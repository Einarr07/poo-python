# Object-Oriented Programming (OOP) with Python - Library Project

This README combines a detailed explanation of OOP concepts with a visual map of the project.

---

## 1. Introduction

Object-Oriented Programming (OOP) in Python is a paradigm based on **objects**, which are instances of **classes**.
Classes allow developers to model real-world entities using attributes (data) and methods (behavior).

This project demonstrates OOP concepts using a **library management system** with Books, Users, and a Library
coordinating interactions.

---

## 2. Project Structure

```
.
├── books.py          # Book classes: base and specialized types
├── users.py          # User classes: Student, Teacher, protocols
├── library.py        # Library class: composition of books and users
├── persistence.py    # Handles saving/loading data to JSON
├── data.py           # Sample books and users data
├── exceptions.py     # Custom domain-specific exceptions
├── main.py           # CLI script demonstrating system interaction
├── library.json      # Persisted library data
└── README.md         # Project documentation and visual OOP map
```

---

## 3. Key OOP Concepts Applied

| Concept                | Where / How Applied                                                                     |
|------------------------|-----------------------------------------------------------------------------------------|
| **Encapsulation**      | Private attributes like `__borrowed_times` in Book. Access via properties.              |
| **Inheritance**        | PhysicalBook/DigitalBook inherit from Book; Student/Teacher inherit from User.          |
| **Polymorphism**       | Overriding `book_request()` for Student/Teacher; `duration_calculate()` for Book types. |
| **Composition**        | Library contains Books and Users as collections.                                        |
| **Abstract Classes**   | `BaseUser` forces `book_request()` implementation.                                      |
| **Protocols**          | `BookProtocol` and `ApplicantProtocol` allow structural typing.                         |
| **Exception Handling** | Domain-specific errors: `BookNotAvailable`, `UserNoFoudError`, `InvalidTitleError`.     |
| **Persistence / I/O**  | Persistence class handles JSON serialization/deserialization.                           |
| **Properties**         | Computed attributes like `books_available`, `borrowed_times`.                           |
| **Constructor**        | `__init__` initializes attributes for all objects.                                      |

---

## 4. Class Relationships and Hierarchy

```
                 +----------------+
                 |   BookProtocol |
                 +----------------+
                         ^
                         |
                 +----------------+
                 |      Book      |
                 +----------------+
                 | id, title,     |
                 | author, price, |
                 | available      |
                 +----------------+
                         ^
        -----------------|-----------------
        |                               |
+----------------+               +----------------+
| PhysicalBook   |               | DigitalBook    |
+----------------+               +----------------+
| duration_calculate()          | duration_calculate() |
+----------------+               +----------------+


                 +----------------+
                 | ApplicantProtocol |
                 +----------------+
                         ^
                         |
                 +----------------+
                 |     BaseUser   |
                 +----------------+
                         ^
                 +----------------+
                 |      User      |
                 +----------------+
                         ^
        -----------------|----------------
        |                               |
+----------------+               +----------------+
|   Student      |               |    Teacher     |
+----------------+               +----------------+
| subject        |               | no borrow limit|
| limit_books    |               |                |
| book_request() |               | book_request() |
+----------------+               +----------------+


+----------------+
|    Library     |
+----------------+
| books []       |
| users []       |
| books_available|
| find_book()    |
| find_user()    |
+----------------+
        |
        v
+----------------+
| Persistence    |
+----------------+
| save_data()    |
| load_data()    |
+----------------+
```

---

## 5. Example Usage

```python
student = Student(1, "Alice", "STU001", "Computer Science")
book = PhysicalBook(1, "1984", "George Orwell", 18.90)

# Polymorphic book request
print(student.book_request(book.title))

# Lend the book
print(book.lend())
```

---

## 6. Benefits of OOP Demonstrated

* Models real-world entities naturally.
* Encourages modular and reusable design.
* Provides encapsulation for controlled data access.
* Supports polymorphic behavior for flexible code.
* Separates concerns (Persistence vs Business Logic).
* Handles errors through domain-specific exceptions.

---

## 7. Running the Project

1. Run `main.py` to interact with the CLI.
2. Enter a user ID card and a book title.
3. System will validate, process the request, and update library state.
4. All changes are automatically saved in `library.json`.

---

This single README now contains both a **conceptual explanation of OOP** and a **visual map of the project structure and
relationships** for quick study and revision.
