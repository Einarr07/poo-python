class User:
    def __init__(self, id: int, name: str, id_card: str):
        self.id = id
        self.name = name
        self.id_card = id_card
        self.lend_books = []

    def book_request(self, title: str):
        return f'Request of book {title} successful'


# Simple herencie
class Student(User):
    def __init__(self, id: int, name: str, id_card: str, subject: str):
        super().__init__(id, name, id_card)
        self.subject = subject
        self.limit_books = 3

    def book_request(self, title: str):
        if len(self.lend_books) < self.limit_books:
            self.lend_books.append(title)
            return f'Request of book {title} successful'
        else:
            return f'You have reached the limit of 3 borrowed books'


class Teacher(User):
    def __init__(self, id: int, name: str, id_card: str):
        super().__init__(id, name, id_card)
        self.limit_books = None

    def book_request(self, title: str):
        return f'Request of book {title} successful'


domenica = Student(1, name="Domenica", id_card="123", subject='Math')
luis = Teacher(2, name="Luis", id_card="456")

print(domenica.book_request('Las auroras boreales'))
print(domenica.book_request('Las auroras boreales'))
print(domenica.book_request('Las auroras boreales'))
print(domenica.book_request('Las auroras boreales'))
print(domenica.book_request('Las auroras boreales'))
print(luis.book_request('Estrepitoso'))
print(luis.book_request('Estrepitoso'))
print(luis.book_request('Estrepitoso'))
print(luis.book_request('Estrepitoso'))
print(luis.book_request('Estrepitoso'))
print(luis.book_request('Estrepitoso'))
