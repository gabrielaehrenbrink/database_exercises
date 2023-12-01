class Comment:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, title_comment, content_comment, author, post_id):
        self.id = id
        self.title_comment = title_comment
        self.content_comment = content_comment
        self.author = author
        self.post_id = post_id

    def __eq__(self, other):
        if isinstance(other, Comment):
            return self.id == other.id and self.title_comment == other.title_comment and self.content_comment == other.content_comment and self.author == other.author and self.post_id == other.post_id
        return False

    def __repr__(self):
        return f"Comment({self.id}, {self.title_comment}, {self.content_comment}, {self.author}, {self.post_id})"