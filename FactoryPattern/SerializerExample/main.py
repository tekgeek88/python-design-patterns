from FactoryPattern.SerializerExample import serializers
from FactoryPattern.SerializerExample.song import Song
import FactoryPattern.SerializerExample.yaml_serializer

########################################################
#                   Main Program
########################################################
if __name__ == '__main__':

    song_01 = Song('1', 'Gangsta Rap Made Me Do It', 'Ice Cube')
    song_02 = Song('2', 'It Was A Good Day', 'Ice Cube')
    song_03 = Song('3', 'Yaml on a Camel', 'Smokin Joe')

    serializer = serializers.ObjectSerializer()

    print(serializer.serialize(song_01, 'JSON'))

    print(serializer.serialize(song_02, 'XML'))

    print(serializer.serialize(song_03, 'YAML'))


