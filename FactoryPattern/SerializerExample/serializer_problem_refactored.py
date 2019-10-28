import json
from xml.etree import ElementTree


class Song:

    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:

    # This is the client component of the code
    # This function depends on an interface to complete its task
    # The interface is refred to as the product component
    # The product is a function that takes a song and returns a string
    def serialize(self, song, format):
        serializer = self._get_serializer(format)
        return serializer(song)

    # The creator component
    def _get_serializer(self, format):
        if format == 'JSON':
            return self._serialize_to_json
        elif format == 'XML':
            return self._serialize_to_xml
        else:
            raise TypeError(format)


    # Concete implementations of the product
    def _serialize_to_json(self, song):
        payload = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(payload)

    # Concete implementations of the product
    def _serialize_to_xml(self, song):
        song_info = ElementTree.Element('song', attrib={'id': song.song_id})
        title = ElementTree.SubElement(song_info, 'title')
        title.text = song.title
        artist = ElementTree.SubElement(song_info, 'artist')
        artist.text = song.artist
        return ElementTree.tostring(song_info, encoding='unicode')

########################################################
#                   Main Program
########################################################
if __name__ == '__main__':

    song_01 = Song('1', 'Gangsta Rap Made Me Do It', 'Ice Cube')
    song_02 = Song('2', 'It Was A Good Day', 'Ice Cube')

    serializer = SongSerializer()

    print("Serializing JSON")

    print(serializer.serialize(song_01, 'JSON'))
    print(serializer.serialize(song_02, 'JSON'))
    print()

    print("Serializing XML")
    print(serializer.serialize(song_01, 'XML'))
    print(serializer.serialize(song_02, 'XML'))

    print("Finished running program...")