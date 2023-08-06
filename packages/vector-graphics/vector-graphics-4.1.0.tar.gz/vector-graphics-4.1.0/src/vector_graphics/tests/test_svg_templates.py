from django.test import SimpleTestCase, TestCase
from wagtail.tests.utils import WagtailTestUtils

import os, sys, random, codecs

from ..svg_templates import *


def parse_svg_file(file_path):

    with codecs.open(file_path, "rb", encoding="utf-8") as file:
        svg_text = file.read()
        return ET.fromstring(svg_text)


def parse_svg_text(text):
    svg = ET.fromstring(text.decode("utf-8"))
    return svg


class TestSVGTemplate(WagtailTestUtils, SimpleTestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.svg_file_path_ = os.path.join(os.path.dirname(__file__), "test_template.svg")

    def test_parsing(self):

        svg_root = parse_svg_file(self.svg_file_path_)
        template = SVGTemplate.parse_from_svg_tree(svg_root)

        pass
