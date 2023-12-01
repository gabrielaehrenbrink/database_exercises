from lib.comment_repository import CommentRepository
from lib.post import Post
from lib.comments import Comment

# Find a single cohort(artist), along with their students(albums)
def test_find_with_posts(db_connection):
    db_connection.seed("seeds/blog.sql")
    repository = CommentRepository(db_connection)
    post = repository.find_with_post(1)
    assert post == Post(1, 'Post title', 'Lots of content', [
    Comment(1, 'Loved it', 'This post is amazing', 'gabs123', 1),
    Comment(2, 'amazing', 'cool blog', 'misterious_author', 1),
    Comment(3, 'Nice', 'very interesting', 'john', 1)
])