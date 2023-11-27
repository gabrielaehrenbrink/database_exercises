from lib.book_repository import *


# test class to return a list of all book objects 

def test_get_all_books(db_connection):
    db_connection.seed('seeds/book_store.sql')
    repository = BookRepository(db_connection)

    books = repository.all()

    assert books == [
        (1, 'Nineteen Eighty-Four', 'George Orwell'),
        (2, 'Mrs Dalloway', 'Virginia Woolf'),
        (3, 'Emma', 'Jane Austen'),
        (4, 'Dracula', 'Bram Stoker'),
        (5, 'The Age of Innocence', 'Edith Wharton'),
    ]