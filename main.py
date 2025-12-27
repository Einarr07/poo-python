# ------------------------------------------------
# Imports from domain modules
# ------------------------------------------------
# Book implementations
from data import data_books, data_students
from exceptions import UserNoFoudError, BookNotAvailable
# Library (composition root)
from library import Library

library = Library('Las Aguas')

library.books = data_books
library.users = data_students

print('-' * 30)
print('| Welcome to the library! |')
print('-' * 30)

print(f'We have available {len(library.books_available())} books')

count = 0
for book in library.books:
    if book.available:
        count += 1
        print(f'{count} ---> Title:{book.title} - Author:{book.author}')

id_card = input('Input your id card: ')

try:
    user = library.find_user(id_card)
    print(f'{user.id_card} whit name {user.name}')
except UserNoFoudError as e:
    print(e)
    print('The user does not exist')

title = input('Input the title of the book: ')

try:
    book = library.find_book(title)
    print(f'The book that your request is: {title}')
except BookNotAvailable as e:
    print(e)
    print('The book does not exist or is not available')

request_book = user.book_request(book.title)
print(f'\n{request_book}')

try:
    book_lend = book.lend()
    print(f'\n{book_lend}')
except BookNotAvailable as e:
    print(e)
