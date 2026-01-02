# ============================================================
# CUSTOM EXCEPTIONS MODULE
# ============================================================
# This file defines domain-specific exceptions for the library
# application.
#
# Using custom exceptions allows:
# - Clearer error handling
# - Better separation between technical and business errors
# - More readable and maintainable code


# ============================================================
# BASE EXCEPTION: LibraryError
# ============================================================
# Acts as the base class for all custom exceptions
# related to the library domain.
#
# This allows catching all library-related errors
# with a single except block if needed.
class LibraryError(Exception):
    pass


# ============================================================
# INVALID TITLE ERROR
# ============================================================
# Raised when a book title is invalid or does not meet
# expected validation rules.
class InvalidTitleError(LibraryError):
    pass


# ============================================================
# BOOK NOT AVAILABLE ERROR
# ============================================================
# Raised when attempting to lend a book that is already
# borrowed or marked as unavailable.
class BookNotAvailable(LibraryError):
    pass


# ============================================================
# USER NOT FOUND ERROR
# ============================================================
# Raised when a requested user cannot be found
# in the system.
#
# This is a domain-level exception, not a technical one.
class UserNoFoudError(LibraryError):
    pass
