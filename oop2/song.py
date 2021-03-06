class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (Artist): an artist object representing the songs creator
        duration (int): duration of the song in seconds. may be zero
    """
    def __init__(self, title, artist, duration=0):
        """Song init method
        Args:
            title (str): initializes the title attribute
            artist (Artist): an artist object representing the song's creator
            duration (optional(int)): initial value for the duration attribute
                will default to zero if not specified.
        """
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Class to represent an Album, comprising its track list

    Attributes:
        name (str): The name of the album
        year (int): the year the album was released
        artist (Artist): the artist responsible for the album. If not specified,
        the artist will default to an artist with the name "Various Artists".
        tracks (List[Song]): a list of the songs on teh album.

    Methods:
        add_song: used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the tracklist

        Args:
            song (Song): a song to add.
            position (optional[int]): if specified, the song will be added to that position in the track list-
            inserting it between songs if necessary. otherwise the song will be added to the end of the list.
        """

        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store artist details.

    Attributes:
        name (str): the name of the artist
        albums (List[Album]): list of the albums by this artist.
            the list includes only those albums in this collection, it is not an exhaustive list

    Methods:
        add_album: add a new album to teh artist's list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list

        Args:
            album (Album): album object to add to teh list.
                if the album is already present, it will not be added again
                (this is yet to be implemented)
        """
        self.albums.append(album)


def find_object(field, object_list):
    """Check object_list to see if an object with a name attribute equal to field exists, return it if so"""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                # we've read details for a new artist
                # retrieve artist object if exists, otherwise create new and add to artist list
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)
            elif new_album != album_field:
                # we've just read a new album fot the current artist
                # retrieve album object if exists, otherwise create new and store in the artist's collection
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                    new_artist.add_album(new_album)

            # create a new song object and add it to the current album's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

    return artist_list


def create_check_file(artist_list):
    """Create a check file from the object data for comparison with the original file"""
    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)


if __name__ == "__main__":
    artists = load_data()
    print("There are {} artists.".format(len(artists)))
    create_check_file(artists)
