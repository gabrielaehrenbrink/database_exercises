from lib.user import User

class UserRepository:

    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["username"], row["email"])
            users.append(item)
        return users

    def find(self, id):
        rows = self._connection.execute('SELECT * from users WHERE id= %s', [id])
        row = rows[0]
        return User(row["id"], row["username"], row["email"])
    
    def create(self, user):
        self._connection.execute("INSERT INTO users (username, email) VALUES (%s, %s)", [user.username, user.email])
        return None

    def delete(self, id):
        self._connection.execute(
            'DELETE FROM users WHERE id = %s', [id])
        return None
    
    def update(self, user):
        self._connection.execute(
            "UPDATE users SET username = %s, email = %s WHERE id=%s",
            [user.username, user.email, user.id]

        )