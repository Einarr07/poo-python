# ============================================================
# MAIN APPLICATION ENTRY POINT
# ============================================================
# This script demonstrates:
# - Composition: Library has Users and Books
# - Object interaction (User requests Book, Library coordinates)
# - Exception handling
# - Persistence (saving/loading data)
# - Simple CLI for user interaction

# ------------------------------------------------------------
# Imports from domain modules
# ------------------------------------------------------------
import sys

from exceptions import UserNoFoudError, BookNotAvailable
from persistence import Persistence

# ------------------------------------------------------------
# Load persisted library data
# ------------------------------------------------------------
# Persistence layer reconstructs Library, Books, and Users
persistence = Persistence()
library = persistence.load_data()

# ------------------------------------------------------------
# Welcome message
# ------------------------------------------------------------
print('-' * 30)
print('| Welcome to the library! |')
print('-' * 30)

# ------------------------------------------------------------
# Show available books
# ------------------------------------------------------------
# Demonstrates iteration over object collections
# and using properties to query object state
print(f'We have available {len(library.books_available)} books')

count = 0
for book in library.books_available:
    count += 1
    print(f'{count} ---> {book.all_description}\nBorrowed times: {book.borrowed_times}')

# ------------------------------------------------------------
# User input: identify user
# ------------------------------------------------------------
id_card = input('Input your id card: ')

try:
    # Attempt to find the user in the library
    user = library.find_user(id_card)
    print(f'{user.id_card} with name {user.name}')
except UserNoFoudError as e:
    # Domain-specific exception handling
    print(e)
    print('The user does not exist')
    sys.exit(1)  # Exit if user not found

# ------------------------------------------------------------
# User input: request a book by title
# ------------------------------------------------------------
title = input('Input the title of the book: ')

try:
    # Attempt to find the book in the library
    book = library.find_book(title)
    print(f'The book that your request is: {title}')
except BookNotAvailable as e:
    # Handle book not available or not found
    print(e)
    print('The book does not exist or is not available')
else:
    # --------------------------------------------------------
    # User requests the book (polymorphic method)
    # --------------------------------------------------------
    request_book = user.book_request(book.title)
    print(f'\n{request_book}')

    try:
        # Lend the book (updates availability and borrowed times)
        result = book.lend()
        print(f'\n{result}')
    except BookNotAvailable as e:
        print(e)

# ------------------------------------------------------------
# Save library state
# ------------------------------------------------------------
# Persist updated library data (books and users)
persistence.save_data(library)
