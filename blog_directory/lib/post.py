class Post:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, title, content, comments):
        self.id = id
        self.title = title
        self.content = content
        self.comments = comments

    def __eq__(self, other):
        if isinstance(other, Post):
            return self.id == other.id and self.title == other.title and self.content == other.content and self.comments == other.comments
        return False

    def __repr__(self):
        return f"Post({self.id}, {self.title}, {self.content}, {self.comments})"