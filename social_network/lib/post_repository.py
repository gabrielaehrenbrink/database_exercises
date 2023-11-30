from lib.post import Post

class PostRepository:

    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        posts = []
        for row in rows:
            item = Post(row["id"], row["title"], row["content"], row['views'], row['user_id'])
            posts.append(item)
        return posts

    def find(self, id):
        rows = self._connection.execute('SELECT * from posts WHERE id= %s', [id])
        row = rows[0]
        return Post(row["id"], row["title"], row["content"], row['views'], row['user_id'])
    
    def create(self, post):
        self._connection.execute("INSERT INTO posts (title, content, views, user_id) VALUES (%s, %s, %s, %s)", [post.title, post.content, post.views, post.user_id])
        return None


    def delete(self, id):
        self._connection.execute(
            'DELETE FROM posts WHERE id = %s', [id])
        return None
    
    def update(self, post):
        self._connection.execute(
            "UPDATE posts SET title = %s, content = %s, views = %s, user_id = %s WHERE id=%s",
            [post.title, post.content, post.views, post.user_id, post.id]

        )