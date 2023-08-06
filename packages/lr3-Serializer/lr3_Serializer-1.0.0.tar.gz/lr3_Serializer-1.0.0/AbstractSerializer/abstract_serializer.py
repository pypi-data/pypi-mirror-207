from Parser.json.json_parser import Json
from Parser.xml.xml_parser import Xml


class GeneralSerializer(object):

    @staticmethod
    def parser(type_: str):
        if type_.__eq__('json'):
            return Json()
        elif type_.__eq__('xml'):
            return Xml()
        else:
            return Json()
