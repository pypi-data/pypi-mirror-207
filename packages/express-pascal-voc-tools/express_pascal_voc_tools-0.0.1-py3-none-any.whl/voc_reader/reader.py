import os
import pathlib
import xml.etree.ElementTree as ET


class Annotation:
    def __init__(self, xmin, ymin, xmax, ymax, center_x, center_y, class_name):
        self._xmin, self._ymin, self._xmax, self._ymax, self._center_x, self._center_y, self._class_name = (
            xmin, ymin, xmax,
            ymax, center_x,
            center_y,
            class_name)

    @property
    def xmin(self):
        return self._xmin

    @property
    def ymin(self):
        return self._ymin

    @property
    def xmax(self):
        return self._xmax

    @property
    def ymax(self):
        return self._ymax

    @property
    def center_x(self):
        return self._center_x

    @property
    def center_y(self):
        return self._center_y

    @property
    def class_name(self):
        return self._class_name


def from_xml(xml_file: str):
    """
    Generate a list of Annotation objects from a given VOC XML file
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()

    list_with_all_boxes = []

    filename = root.find('filename').text
    for boxes in root.iter('object'):
        class_ = boxes.find("name").text
        ymin = int(boxes.find("bndbox/ymin").text)
        xmin = int(boxes.find("bndbox/xmin").text)
        ymax = int(boxes.find("bndbox/ymax").text)
        xmax = int(boxes.find("bndbox/xmax").text)
        cx = (xmin + xmax) / 2
        cy = (ymin + ymax) / 2

        list_with_single_boxes = (xmin, ymin, xmax, ymax, cx, cy, class_)
        yield list_with_single_boxes

    return list_with_all_boxes


def from_directory(dir_path: str):
    """
    Generate a list of Annotation object per file form a given directory
    """
    dir_path = pathlib.Path(dir_path)
    annotations_dir = dir_path / "Annotations"
    for xml_file in os.listdir(str(annotations_dir)):
        yield xml_file.strip(".xml"), *from_xml(str(annotations_dir / xml_file))
