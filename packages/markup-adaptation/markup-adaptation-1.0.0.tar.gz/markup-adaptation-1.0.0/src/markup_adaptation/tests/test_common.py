import os, io

from unittest import TestCase

from ..adaptation import AdaptationSchema
from ..configuration import EditableConfiguration
from ..svg_template import SVGContent, SVGTemplate


class AdaptationsTest(TestCase):

    def test_parser(self):

        example_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "adaptation_schema.xml")
        schema = None

        with open(example_path, mode="rb") as file:
            schema = AdaptationSchema.from_file(file)

        pass


class SVGContentTest(TestCase):

    def test_template(self):

        example_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "template_example.svg")

        with open(example_path, mode="rb") as file:
            svg_content = SVGContent.from_binary_file(file)
            view_box = svg_content.view_box
            aspect_ratio = svg_content.preserve_aspect_ratio
            pass

        pass


class SVGTemplateTest(TestCase):

    def test_template(self):

        example_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "template_example.svg")

        with open(example_path, mode="rb") as file:
            template = SVGTemplate.from_binary_file(file)
            configuration = EditableConfiguration()
            template.schema.define_defaults(configuration)
            result = template.build_adaptation(configuration)

        pass