import json
from xml.etree import ElementTree


class Song:

    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:

    def serialize(self, song, format):
        if format == 'JSON':
            song_info = {
                'id': song.song_id,
                'title': song.title,
                'artist': song.artist
            }
            return json.dumps(song_info)
        elif format == 'XML':
            song_info = ElementTree.Element('song', attrib={'id': song.song_id})
            title = ElementTree.SubElement(song_info, 'title')
            title.text = song.title
            artist = ElementTree.SubElement(song_info, 'artist')
            artist.text = song.artist
            return ElementTree.tostring(song_info, encoding='unicode')
        else:
            raise ValueError(format)

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