import json
import xml.etree.ElementTree as etree


class XMLConnector(object):
    """parse xml data"""

    def __init__(self, file_path: str) -> None:
        self.data = etree.parse(file_path)

    @property
    def parse_data(self):
        return self.data


class JSONConnector(object):
    """parse json data"""

    def __init__(self, file_path: str) -> None:
        with open(file_path, "rt", encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def parse_data(self):
        return self.data


def connector_factory(filepath: str):
    if filepath.endswith(".xml"):
        connector = XMLConnector
    elif filepath.endswith(".json"):
        connector = JSONConnector
    else:
        raise ValueError("Cannot connect to {}".format(filepath))

    return connector(filepath)


def connect_to(filepath: str):
    factory = None
    try:
        factory = connector_factory(filepath)
    except ValueError as e:
        print(e)
    return factory


if __name__ == '__main__':
    sqlite_factory = connect_to("../data/person.sq3")
    json_factory = connect_to("../data/donut.json")
    json_data = json_factory.parse_data
    print(json_data)

