class Song:

    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist

    # Implementing the serializable interface
    def serialize(self, serialzer):
        serialzer.start_object('song', self.song_id)
        serialzer.add_property('title', self.title)
        serialzer.add_property('artist', self.artist)