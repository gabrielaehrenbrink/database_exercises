class Book():
    def __init__(self, id, title, author_name):
        self.id = id
        self.title = title
        self.author_name = author_name
    
    def book_format(self):
        return f"Book({self.title}, written by: {self.author_name})"

    def get_author(self, title):
        return self.author_name
    
    def get_book(self, author_name):
        return self.title

