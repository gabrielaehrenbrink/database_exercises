from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.book_repository import BookRepository

# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# List them out
for artist in artists:
    print(artist)


album_repository = AlbumRepository(connection)

for album in album_repository.all():
    print(album)


# print out the list of books to the terminal
book_repository = BookRepository(connection)

for book in book_repository.all():
    print(book)