from lib.album import Album

#  makes with id, title, release_year and artist_id

def test_constructs_with_fields():
    album = Album(1, "Dark Side", 1995, 2)
    assert album.id == 1
    assert album.title == 'Dark Side'
    assert album.release_year == 1995
    assert album.artist_id == 2


# when I construct two albums with the same fields they are equal
def test_albums_are_equal():
    album1 = Album(1, "Dark Side", 1995, 2)
    album2 = Album(1, "Dark Side", 1995, 2)
    assert album1 == album2

#  when I construct an Artist and I format it to a string 
# it comes out in a friendly format

def test_albums_format_nicely():
    album = Album(1, "Dark Side", 1995, 2)
    assert str(album) == "Album(1, Dark Side, 1995, 2)"


