from lib.post import Post
from lib.post_repository import PostRepository


def test_post_constructs():
    post = Post(1, 'title', 'my contents', 2, 1)
    assert post.id == 1
    assert post.title == 'title'
    assert post.content == 'my contents'
    assert post.views == 2
    assert post.user_id == 1


def test_all(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = PostRepository(db_connection)

    posts = repository.all() 


    assert posts == [
        Post(1, 'title', 'my contents', 2, 1),
        Post(2, 'another post', 'different content', 8, 3),
        Post(3, 'long post', 'This is a much longer content for the post. It can include multiple sentences or paragraphs.', 12, 4),
        Post(4, 'popular post', 'interesting content', 20, 2)
    ]

def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = PostRepository(db_connection)
    result = repository.find(2)
    assert result == Post(2, 'another post', 'different content', 8, 3)

def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = PostRepository(db_connection)
    repository.create(Post(None, 'new post', 'new content', 8, 6))

    result = repository.all()

    assert result == [
        Post(1, 'title', 'my contents', 2, 1),
        Post(2, 'another post', 'different content', 8, 3),
        Post(3, 'long post', 'This is a much longer content for the post. It can include multiple sentences or paragraphs.', 12, 4),
        Post(4, 'popular post', 'interesting content', 20, 2),
        Post(5, 'new post', 'new content', 8, 6)
    ]

def test_delete(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = PostRepository(db_connection)
    repository.delete(5)

    result = repository.all()
    assert result == [
        Post(1, 'title', 'my contents', 2, 1),
        Post(2, 'another post', 'different content', 8, 3),
        Post(3, 'long post', 'This is a much longer content for the post. It can include multiple sentences or paragraphs.', 12, 4),
        Post(4, 'popular post', 'interesting content', 20, 2)
    ]


def test_update(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = PostRepository(db_connection)
    user = repository.find(1)
    user.title = "Better title"
    assert repository.update(user) is None
    assert repository.all() == [
        Post(2, 'another post', 'different content', 8, 3),
        Post(3, 'long post', 'This is a much longer content for the post. It can include multiple sentences or paragraphs.', 12, 4),
        Post(4, 'popular post', 'interesting content', 20, 2),
        Post(1, 'Better title', 'my contents', 2, 1)
    ]




