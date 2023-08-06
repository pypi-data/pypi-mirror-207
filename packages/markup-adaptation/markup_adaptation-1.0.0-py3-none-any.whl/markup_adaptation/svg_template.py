
import xml.etree.ElementTree as ET
import collections

from .adaptation import MarkupTemplate, AdaptationSchema
from .xml_domain import XMLDomain, XMLTree

import re

LENGTH_VALUE_RE = re.compile(r'(([0-9]+(\.[0-9]+)?)|(\.[0-9]+))(em|ex|px|in|cm|mm|pt|pc|%)')


def format_length(number, unit):

    try:
        number = "{:d}".format(number)
    except ValueError:
        number = "{:f}".format(number)

    return number + unit


def parse_length_value(string):
    match = LENGTH_VALUE_RE.match(string)

    if match is None:
        return None

    number = match.group(1)

    try:
        number = int(number)
    except ValueError:
        number = float(number)

    unit = match.group(5)

    return number, unit


def format_preserve_aspect_ratio(align, directive=None):

    result = align

    if directive is not None:
        result += " " + directive

    return result


def parse_preserve_aspect_ratio(string):

    parts = string.split(' ')
    align = parts[0]

    if len(parts) > 2:
        raise ValueError('Invalid preserveAspectRatio attribute.')

    if len(parts) == 2:
        directive = parts[1]
    else:
        directive = None

    return align, directive


class SVGContent(XMLDomain):

    @property
    def svg_attributes(self):
        return self.xml_tree_.root_.attrib

    @property
    def view_box(self):
        value = self.svg_attributes.get('viewBox', None)

        if value is None:
            return value

        parts = value.split(' ')
        value = []

        for part in parts:
            value.extend(part.split(','))

        values = []

        for element in value:
            try:
                element = int(element)
            except ValueError:
                element = float(element)

            values.append(element)

        return values

    @view_box.setter
    def view_box(self, value):

        if value is None:
            if 'viewBox' in self.svg_attributes:
                del self.svg_attributes['viewBox']
            return

        values = []

        for part in value:
            try:
                part = "{:d}".format(part)
            except ValueError:
                part = "{:f}".format(part)

            values.append(part)

        self.svg_attributes['viewBox'] = ' '.join(values)

    @property
    def width(self):
        value = self.svg_attributes.get('width', None)

        if value is None:
            return value

        value = parse_length_value(value)

        return value

    @width.setter
    def width(self, value):

        if value is None:
            if 'width' in self.svg_attributes:
                del self.svg_attributes['width']
            return

        if isinstance(value, str):
            self.svg_attributes['width'] = value
            return

        number, unit = value
        self.svg_attributes['width'] = format_length(number, unit)

    @property
    def height(self):
        value = self.svg_attributes.get('height', None)

        if value is None:
            return value

        value = parse_length_value(value)

        return value

    @height.setter
    def height(self, value):

        if value is None:
            if 'height' in self.svg_attributes:
                del self.svg_attributes['height']
            return

        if isinstance(value, str):
            self.svg_attributes['height'] = value
            return

        number, unit = value
        self.svg_attributes['height'] = format_length(number, unit)

    @property
    def overflow(self):
        value = self.svg_attributes.get('overflow', None)

        if value is None:
            return value
        return value

    @overflow.setter
    def overflow(self, value):

        if value is None:
            if 'overflow' in self.svg_attributes:
                del self.svg_attributes['overflow']
            return

        if isinstance(value, str):
            self.svg_attributes['overflow'] = value
            return

        self.svg_attributes['overflow'] = value

    @property
    def style(self):
        value = self.svg_attributes.get('style', None)

        if value is None:
            return value

        return value

    @style.setter
    def style(self, value):

        if value is None:
            if 'style' in self.svg_attributes:
                del self.svg_attributes['style']
            return

        if isinstance(value, str):
            self.svg_attributes['style'] = value
            return

        self.svg_attributes['style'] = value

    @property
    def preserve_aspect_ratio(self):

        value = self.svg_attributes.get('preserveAspectRatio', None)

        if value is None:
            return value

        value = parse_preserve_aspect_ratio(value)
        return value

    @preserve_aspect_ratio.setter
    def preserve_aspect_ratio(self, value):

        if value is None:
            if 'preserveAspectRatio' in self.svg_attributes:
                del self.svg_attributes['preserveAspectRatio']
            return

        if isinstance(value, str):
            self.svg_attributes['preserveAspectRatio'] = value
            return

        align, directive = value
        self.svg_attributes['preserveAspectRatio'] = format_preserve_aspect_ratio(align, directive)

    @property
    def pointer_events(self):
        value = self.svg_attributes.get('pointer-events', None)

        if value is None:
            return value
        return value

    @pointer_events.setter
    def pointer_events(self, value):

        if value is None:
            if 'pointer-events' in self.svg_attributes:
                del self.svg_attributes['pointer-events']
            return

        if isinstance(value, str):
            self.svg_attributes['pointer-events'] = value
            return

        self.svg_attributes['pointer-events'] = value

    def __init__(self, xml_tree):
        super().__init__(xml_tree)

    def wrap_child_elements(self, wrapper_tag, parent_element=None):

        if parent_element is None:
            parent_element = self.xml_tree_.root_

        children = list(parent_element)
        wrapper = ET.SubElement(parent_element, wrapper_tag)

        for child in children:
            parent_element.remove(child)
            wrapper.append(child)

        return wrapper

    @staticmethod
    def from_binary_file(file, prefix_bindings=None):

        file.seek(0)
        bytes = file.read()
        return SVGContent.from_bytes(bytes, prefix_bindings)

    @staticmethod
    def from_bytes(bytes, prefix_bindings=None):
        text = bytes.decode("utf-8")
        return SVGContent.from_text(text, prefix_bindings)

    @staticmethod
    def from_text(text, prefix_bindings=None):

        if prefix_bindings is not None:
            prefix_bindings = collections.OrderedDict(prefix_bindings) #[(ns, p) for p, ns in prefix_bindings])
        else:
            prefix_bindings = collections.OrderedDict()

        bindings = [("", "http://www.w3.org/2000/svg"), ("xlink", "http://www.w3.org/1999/xlink")]

        bindings = collections.OrderedDict(bindings) #[(ns, p) for p, ns in bindings])

        bindings.update(prefix_bindings)
        #bindings = collections.OrderedDict([(p, ns) for ns, p in bindings.items()])

        for prefix, namespace in bindings.items():
            ET.register_namespace(prefix, namespace)

        tree = ET.fromstring(text)
        xml_tree = XMLTree(tree, text, bindings.items())
        result = SVGContent(xml_tree)
        return result

    @staticmethod
    def from_xml_domain(xml_domain):

        result = SVGContent(xml_domain)
        return result


class SVGTemplate(MarkupTemplate):

    def __init__(self, schema, domain):
        super().__init__(schema, domain)

    @staticmethod
    def from_binary_file(file, prefix_bindings=None):

        file.seek(0)
        bytes = file.read()
        return SVGTemplate.from_bytes(bytes, prefix_bindings)

    @staticmethod
    def from_bytes(bytes, prefix_bindings=None):
        text = bytes.decode("utf-8")
        return SVGTemplate.from_text(text, prefix_bindings)

    @staticmethod
    def from_text(text, prefix_bindings=None):

        if prefix_bindings is not None:
            prefix_bindings = collections.OrderedDict(prefix_bindings) #[(ns, p) for p, ns in prefix_bindings])
        else:
            prefix_bindings = collections.OrderedDict()

        bindings = [("adap", "http://xml.hdng.website/Adaptations.xsd")]

        bindings = collections.OrderedDict(bindings) #[(ns, p) for p, ns in bindings])

        bindings.update(prefix_bindings)
        #bindings = collections.OrderedDict([(p, ns) for ns, p in bindings.items()])

        result = SVGContent.from_text(text, bindings.items())
        result = SVGTemplate.from_svg_content(result)

        return result

    @staticmethod
    def from_svg_content(svg_content):

        schemata = [location.element for location in svg_content.iterate(elements=True, attributes=False, properties=False)
                    if location.element.tag == "{http://xml.hdng.website/Adaptations.xsd}schema"]

        if len(schemata) == 0:
            return None

        if len(schemata) > 1:
            return None

        schema_tree = schemata[0]
        schema, errors = AdaptationSchema.from_tree(schema_tree)

        template = SVGTemplate(schema, svg_content)
        return template
