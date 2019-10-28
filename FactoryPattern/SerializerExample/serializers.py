import json
from xml.etree import ElementTree

class SerializerFactory:

    def __init__(self):
        self._creators = {}

    def register_format(self, format, creator):
        self._creators[format] = creator

    def get_serializer(self, format):
        creator = self._creators.get(format)
        return creator()


class JsonSerializer:

    def __init__(self):
        self._current_object = None

    def start_object(self, object_name, object_id):
        self._current_object = {
            'id': object_id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class XmlSerializer:

    def __init__(self):
        self._element = None

    def start_object(self, object_name, object_id):
        self._element = ElementTree.Element(object_name, attrib={'id': object_id})

    def add_property(self, name, value):
        prop = ElementTree.SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return ElementTree.tostring(self._element, encoding='unicode')


class ObjectSerializer:
    def serialize(self, serializable, format):
        serializer = factory.get_serializer(format)
        serializable.serialize(serializer)
        return serializer.to_str()

factory = SerializerFactory()
factory.register_format('JSON', JsonSerializer)
factory.register_format('XML', XmlSerializer)