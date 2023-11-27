from lib.book import Book

# test book constructs
def test_book_constructs():
    book = Book('id', 'Title', "Author name")
    assert book.title == "Title"
    assert book.author_name == "Author name"


# test book format string
def test_book_format():
    book = Book('id', 'Title', "Author name")
    assert book.book_format() == "Book(Title, written by: Author name)"


# title method should return the author of a book when given a title
def test_author_by_book_title():
    book = Book('id', 'Title', 'Author name')
    book2 = Book('id2', 'Title2', 'Author name2')
    book3 = Book('id3', 'Title3', 'Author name3')
    result = book.get_author('Title')
    assert result == "Author name"



# author method should return all books from a given author
def test_book_by_author():
    book = Book('id', 'Title', 'Author name')
    book2 = Book('id2', 'Title2', 'Author name2')
    book3 = Book('id3', 'Title3', 'Author name3')
    result = book.get_book('Author name')
    assert result == "Title"