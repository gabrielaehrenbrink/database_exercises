from lib.user import User
from lib.user_repository import UserRepository

def test_user_constructs():
    user = User(1, 'gabi123', 'gabi@gmail.com')
    assert user.id == 1
    assert user.username == 'gabi123'
    assert user.email == 'gabi@gmail.com'

def test_users_are_equal():
    user1 = User(1, "username", "email@email.com")
    user2 = User(1, "username", "email@email.com")
    assert user1 == user2


def test_all(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = UserRepository(db_connection)

    users = repository.all() 


    assert users == [
        User(1, 'gabi123', 'gabi@gmail.com'),
        User(2, 'john_doe', 'john.doe@example.com'),
        User(3, 'alice_smith', 'alice.smith@example.com'),
        User(4, 'robert_jones', 'robert.jones@example.com'),
        User(5, 'emily_miller', 'emily.miller@example.com')
    ]

def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = UserRepository(db_connection)
    result = repository.find(2)
    assert result == User(2, 'john_doe', 'john.doe@example.com')

def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = UserRepository(db_connection)
    repository.create(User(None, "mary123", "mary@hotmail.com"))

    result = repository.all()

    assert result == [
        User(1, 'gabi123', 'gabi@gmail.com'),
        User(2, 'john_doe', 'john.doe@example.com'),
        User(3, 'alice_smith', 'alice.smith@example.com'),
        User(4, 'robert_jones', 'robert.jones@example.com'),
        User(5, 'emily_miller', 'emily.miller@example.com'),
        User(6, "mary123", "mary@hotmail.com")
    ]

def test_delete(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = UserRepository(db_connection)
    repository.delete(6)

    result = repository.all()
    assert result == [
        User(1, 'gabi123', 'gabi@gmail.com'),
        User(2, 'john_doe', 'john.doe@example.com'),
        User(3, 'alice_smith', 'alice.smith@example.com'),
        User(4, 'robert_jones', 'robert.jones@example.com'),
        User(5, 'emily_miller', 'emily.miller@example.com')
    ]


def test_update(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = UserRepository(db_connection)
    user = repository.find(1)
    user.email = "gabi@hotmail.com"
    assert repository.update(user) is None
    assert repository.all() == [
        User(2, 'john_doe', 'john.doe@example.com'),
        User(3, 'alice_smith', 'alice.smith@example.com'),
        User(4, 'robert_jones', 'robert.jones@example.com'),
        User(5, 'emily_miller', 'emily.miller@example.com'),
        User(1, 'gabi123', 'gabi@hotmail.com')
    ]




