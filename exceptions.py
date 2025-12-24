class LibraryError(Exception):
    pass


class InvalidTitleError(LibraryError):
    pass


class BookNotAvailable(LibraryError):
    pass


class UserNoFoudError(LibraryError):
    pass
