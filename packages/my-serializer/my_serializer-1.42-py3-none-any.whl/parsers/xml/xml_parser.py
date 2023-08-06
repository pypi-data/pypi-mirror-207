from parsers.src.general_serialize_functions import serialize, deserialize
from parsers.xml.xml_functions import serialize_xml, deserialize_xml


class XmlParser:

    @staticmethod
    def dumps(obj) -> str:
        obj = serialize(obj)
        return serialize_xml(obj).replace("\n", "\\n")

    @staticmethod
    def dump(obj, file):
        file.write(XmlParser.dumps(obj))

    @staticmethod
    def loads(obj: str):
        obj = deserialize_xml(obj.replace("\\n", "\n"))
        return deserialize(obj)

    @staticmethod
    def load(file):
        return XmlParser.loads(file.read())
