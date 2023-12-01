from lib.post import Post
from lib.comments import Comment


class CommentRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Find a single cohort, along with their students
    def find_with_post(self, post_id):
        rows = self._connection.execute(
            "SELECT posts.id, posts.title, posts.content, comments.id as comment_id, comments.title_comment, comments.content_comment, comments.author, comments.post_id FROM posts INNER JOIN comments ON posts.id = comments.post_id WHERE posts.id = %s",
    [post_id]
)
        comments = []
        post = Post(rows[0]["id"], rows[0]["title"], rows[0]["content"], comments)
        for row in rows:
            comment = Comment(row["comment_id"], row["title_comment"], row["content_comment"], row["author"], row["post_id"])
            comments.append(comment)

        
        return post
