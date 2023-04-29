import xml.etree.ElementTree as ET


def get_movie_description():
    tree = ET.parse('movies.xml')
    description = tree.find(".//movie[@title=\"Ferris Bueller's Day Off\"]/description")
    if description is not None:
        return description.text
    return None


get_movie_description()
