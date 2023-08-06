import xml.etree.ElementTree as ET
import weakref
import collections

from .domain import (DomainMixin, DomainLocationIterator, DomainLocation, ELEMENT_CONTENT_TYPE, ATTRIBUTE_CONTENT_TYPE,
                     UnionIterator, get_content_property_content_type)


class XMLDomain(DomainMixin, object):

    class ElementIterator(DomainLocationIterator):

        def __init__(self, xml_domain, selector):
            super().__init__()

            self.xml_domain_ = xml_domain
            self.iterator_ = iter(self.xml_domain_.xml_tree_.findall(selector))

        def __iter__(self):
            return self

        def __next__(self) -> DomainLocation:

            while True:

                location = next(self.iterator_)

                if (self.xml_domain_.selected_locations_ is not None and
                        location not in self.xml_domain_.selected_locations_):
                    continue

                break

            return location

    class AttributeIterator(DomainLocationIterator):

        def __init__(self, xml_domain, selector):
            super().__init__()

            expected_attributes = []

            if selector.do_create_if_missing:
                expected_attributes.append((selector.attribute_name,""))

            self.xml_domain_ = xml_domain
            self.iterator_ = xml_domain.iterate(elements=False, properties=False, expected_attributes=expected_attributes)
            self.selector_ = selector

        def __iter__(self):
            return self

        def __next__(self) -> DomainLocation:

            location = None

            while location is None:

                location = next(self.iterator_)
                attribute = location.attribute

                if attribute.attribute_name != self.selector_.attribute_name:
                    location = None
                    continue

            return location

    class PropertyIterator(DomainLocationIterator):

        def __init__(self, xml_domain, selector):
            super().__init__()

            expected_attributes = []

            if selector.do_create_if_missing:
                expected_attributes.append((selector.attribute_name,""))

            expected_properties = []

            if selector.do_create_if_missing:
                expected_properties.append((selector.property_name, ""))

            self.xml_domain_ = xml_domain
            self.iterator_ = xml_domain.iterate(elements=False, attributes=False, expected_attributes=expected_attributes, expected_properties=expected_properties)
            self.selector_ = selector

        def __iter__(self):
            return self

        def __next__(self) -> DomainLocation:

            location = None

            while location is None:

                location = next(self.iterator_)
                property = location.property

                if property.attribute.attribute_name != self.selector_.attribute_name or \
                    property.property_name != self.selector_.property_name:
                    location = None
                    continue

            return location

    def __init__(self, xml_tree, selected_locations=None):

        super().__init__()
        self.xml_tree_ = xml_tree
        self.selected_locations_ = selected_locations

    @property
    def root_locations_(self):
        return list(self.selected_locations_.keys()) if self.selected_locations_ is not None else [self.xml_tree_.location_for_element(self.xml_tree_.root_)]

    def iterate(self, elements=True, attributes=True, properties=True, expected_attributes=None, expected_properties=None) -> DomainLocationIterator:

        options = {
            "do_iterate_elements": elements,
            "do_iterate_children": self.selected_locations_ is None,
            "do_iterate_attributes": attributes,
            "do_iterate_properties": properties,
            "expected_attributes": expected_attributes,
            "expected_properties": expected_properties
        }

        return XMLDomainIterator(self.xml_tree_, self.root_locations_, options)

    def __iter__(self) -> DomainLocationIterator:
        return self.iterate()

    def iterate_elements(self, selector):
        return self.ElementIterator(self, selector)

    def iterate_attributes(self, selector):
        return self.AttributeIterator(self, selector)

    def iterate_content_properties(self, selector):
        return self.PropertyIterator(self, selector)

    def select_union(self, selectors):

        selected_locations = collections.OrderedDict()

        for location in UnionIterator(self, selectors):

            #if self.selected_locations_ is not None and location not in self.selected_locations_:
            #    continue

            selected_locations[location] = None

        result = XMLDomain(self.xml_tree_, selected_locations=selected_locations)
        return result

    def independent_copy(self):

        xml_tree = self.xml_tree_.independent_copy()
        selected_locations = collections.OrderedDict(self.selected_locations_.items()) if self.selected_locations_ else None

        return XMLDomain(xml_tree, selected_locations)

    def to_text(self):

        for prefix, namespace in self.xml_tree_.prefix_bindings_:
            ET.register_namespace(prefix, namespace)

        result = ET.tostring(self.xml_tree_.root_).decode()
        return result

    @staticmethod
    def from_binary_file(file, prefix_bindings):
        file.seek(0)
        bytes = file.read()
        return XMLDomain.from_bytes(bytes, prefix_bindings)

    @staticmethod
    def from_bytes(bytes, prefix_bindings):
        text = bytes.decode("utf-8")
        return XMLDomain.from_text(text, prefix_bindings)

    @staticmethod
    def from_text(text, prefix_bindings):

        for prefix, namespace in prefix_bindings:
            ET.register_namespace(prefix, namespace)

        tree = ET.fromstring(text)
        return XMLDomain.from_tree(tree, text, prefix_bindings)

    @staticmethod
    def from_tree(tree, text, prefix_bindings):
        xml_tree = XMLTree(tree, text, prefix_bindings)
        return XMLDomain(xml_tree)


class XMLDomainIterator(DomainLocationIterator):

    def __init__(self, xml_tree, root_locations, options):

        super().__init__()
        self.xml_tree_ = xml_tree
        self.do_iterate_elements_ = options.get("do_iterate_elements", True)
        self.do_iterate_children_ = options.get("do_iterate_children", True)
        self.do_iterate_attributes_ = options.get("do_iterate_attributes", True)
        self.do_iterate_properties_ = options.get("do_iterate_properties", True)
        self.expected_attributes_ = options.get("expected_attributes", None)
        self.expected_properties_ = options.get("expected_properties", None)

        if self.expected_attributes_ is None:
            self.expected_attributes_ = []

        if self.expected_properties_ is None:
            self.expected_properties_ = []

        self.stack_ = [(None, 0, root_locations)]

    def __iter__(self):
        return self

    def children_at_location(self, location):

        if location is None:
            return []
        elif location.content_type == ELEMENT_CONTENT_TYPE:

            result = []

            element = location.element

            if self.do_iterate_attributes_ or self.do_iterate_properties_:

                keys = set(element.keys())

                for key, value in self.expected_attributes_:
                    keys.add(key)

                result += [location.location_for_attribute(key, self.xml_tree_.is_structured_attribute(key), do_create=len(self.expected_attributes_) > 0) for key in keys]

            if self.do_iterate_children_ or self.do_iterate_attributes_ or self.do_iterate_properties_:
                result += [self.xml_tree_.location_for_element(x) for x in list(element)]

            return result

        elif location.content_type == ATTRIBUTE_CONTENT_TYPE:

            result = []

            attribute = location.attribute

            if self.do_iterate_properties_:

                structured_content = self.xml_tree_.parse_attribute_content(attribute)

                keys = set(structured_content.keys()) if structured_content else set()

                for key, value in self.expected_properties_:
                    keys.add(key)

                if structured_content is not None:
                    result += [location.location_for_property(key, do_create=len(self.expected_attributes_) > 0) for key in keys]

            return result
        else:
            return []

    def __next__(self) -> DomainLocation:

        location = None

        while self.stack_:

            location, index, children = self.stack_[-1]

            if children is None:
                children = self.children_at_location(location)
                self.stack_[-1] = location, index, children

                if location is not None:

                    if location.content_type == ELEMENT_CONTENT_TYPE and self.do_iterate_elements_:
                        break

                    if location.content_type == ATTRIBUTE_CONTENT_TYPE and self.do_iterate_attributes_:
                        break

                    if location.content_type.name.endswith("_property") and self.do_iterate_properties_:
                        break

            if index >= len(children):
                self.stack_.pop()
                continue

            child_location = children[index]
            index += 1

            self.stack_[-1] = location, index, children
            self.stack_.append((child_location, 0, None))

        if location is None:
            raise StopIteration()

        return location


class StyleAttributeContentHandler(object):

    def parse(self, style):
        properties = [p for p in style.split(";") if p]
        properties = [p.split(":") for p in properties]
        properties = [(p[0].strip(), p[1].strip()) for p in properties]
        properties = dict(properties)
        return properties

    def serialise(self, structured_content):

        result = ""

        for key, value in structured_content.items():
            result += "{}: {};".format(key, value)

        return result


class XMLTree(object):

    class Iterator(object):

        def __init__(self, tree):
            self.tree_ = tree
            self.element_iterator_ = self.tree_.root_.iter()

        def __iter__(self):
            return self

        def __next__(self):

            element = next(self.element_iterator_)
            location = self.tree_.location_for_element(element)
            return location

    def __init__(self, root, text, prefix_bindings, attribute_content_handlers=None):

        self.root_ = root
        self.text_ = text
        self.prefix_bindings_ = list(prefix_bindings)
        self.locations_ = {}

        if attribute_content_handlers is None:
            attribute_content_handlers = []

        self.attribute_content_handlers_ = dict(attribute_content_handlers)

        if "style" not in self.attribute_content_handlers_:
            self.attribute_content_handlers_["style"] = StyleAttributeContentHandler()

    def location_for_element(self, element, do_create=True):

        location = self.locations_.get(element, None)

        if location is None and do_create:

            location = XMLElementLocation(self, element)
            self.locations_[element] = location

        return location

    def findall(self, selector):
        return [self.location_for_element(x) for x in self.root_.findall(selector.text)]

    def __iter__(self):
        return self.Iterator(self)

    def is_structured_attribute(self, attribute_name):
        return attribute_name in self.attribute_content_handlers_

    def parse_attribute_content(self, attribute):

        handler = self.attribute_content_handlers_.get(attribute.attribute_name, None)

        if handler is not None:
            return handler.parse(attribute.get(""))

        return None

    def serialise_attribute_content(self, attribute):

        handler = self.attribute_content_handlers_.get(attribute.attribute_name, None)

        if handler is not None:
            return handler.serialise(attribute.structured_content)

        return None

    def independent_copy(self):

        for prefix, namespace in self.prefix_bindings_:
            ET.register_namespace(prefix, namespace)

        tree_copy = XMLTree(ET.fromstring(self.text_), self.text_, self.prefix_bindings_,
                            self.attribute_content_handlers_.items())

        i = iter(self.root_)
        j = iter(tree_copy.root_)

        try:

            while True:

                element = next(i)
                element_copy = next(j)

                element_loc = self.locations_.get(element, None)

                if element_loc is None:
                    continue

                element_loc_copy = tree_copy.location_for_element(element_copy)

                for attribute_loc in element_loc.attribute_locations:

                    attribute_loc_copy = element_loc_copy.location_for_attribute(attribute_loc.attribute.attribute_name,
                                                                                 attribute_loc.attribute.is_structured,
                                                                                 do_create=True)

                    attribute_loc_copy.attribute.set(attribute_loc.attribute.get())

                    for property_loc in attribute_loc.property_locations:

                        property_loc_copy = attribute_loc_copy.location_for_property(property_loc.property.property_name,
                                                                                     do_create=True)

                        property_loc_copy.property.set(property_loc.property.get())

        except StopIteration:
            pass

        return tree_copy

    def apply_all_changes(self):

        """
        for element in iter(self.root_):

            element_loc = self.location_for_element(element, do_create=False)

            if element_loc is None:
                continue

            if element_loc.is_cleared:

                pass

            pass

        pass
        """


class XMLContentProperty(object):

    @property
    def attribute(self):
        return self.attribute_()

    def __init__(self, attribute, property_name):
        self.attribute_ = weakref.ref(attribute)
        self.property_name = property_name

    def get(self, default=None):
        return self.attribute.get_content_property(self.property_name, default)

    def setdefault(self, default=None):
        return self.attribute.set_content_property_default(self.property_name, default)

    def set(self, value):
        self.attribute.set_content_property(self.property_name, value)


class XMLAttribute(object):

    @property
    def element(self):
        return self.element_()

    @property
    def is_structured(self):
        return self.is_structured_

    @property
    def structured_content(self):
        return self.structured_content_

    def __init__(self, xml_domain, element, attribute_name, is_structured):
        self.xml_domain_ = weakref.ref(xml_domain)
        self.element_ = weakref.ref(element)
        self.attribute_name = attribute_name
        self.is_structured_ = is_structured
        self.structured_content_ = {}

        if is_structured:
            attribute_content = xml_domain.parse_attribute_content(self)

            for key, value in attribute_content.items():
                self.set_content_property(key, value)

    def get(self, default=None):
        return self.element.get(self.attribute_name, default)

    def setdefault(self, default=None):

        value = self.element.get(self.attribute_name, MissingMarker)

        if value == MissingMarker:
            self.element.set(self.attribute_name, default)
            return default

        return value

    def set(self, value):
        self.element.set(self.attribute_name, value)

    def get_content_property(self, name, default=None):
        return self.structured_content_.get(name, default)

    def set_content_property(self, name, value):
        self.structured_content_[name] = value

        xml_domain = self.xml_domain_()

        if xml_domain:
            self.set(xml_domain.serialise_attribute_content(self))

    def set_content_property_default(self, name, default=None):

        value = self.structured_content_.get(name, MissingMarker)

        if value == MissingMarker:
            self.structured_content_[name] = default

            xml_domain = self.xml_domain_()

            if xml_domain:
                self.set(xml_domain.serialise_attribute_content(self))

            return default

        return value


class MissingMarker(object):
    pass


class XMLContentPropertyLocation(DomainLocation):

    @property
    def property(self):
        return self.property_

    def __init__(self, xml_tree, attribute_location, property_name):
        super().__init__()
        self.content_type_ = get_content_property_content_type(attribute_location.attribute.attribute_name, do_create=True)
        self.attribute_location_ = weakref.ref(attribute_location)
        self.property_ = XMLContentProperty(attribute_location.attribute, property_name)

    def get(self, default_value=None):
        return self.property_.get(default_value)

    def set(self, value):
        self.property_.set(value)


class XMLAttributeLocation(DomainLocation):

    @property
    def property_locations(self):
        return self.property_locations_.values()

    @property
    def attribute(self):
        return self.attribute_

    def __init__(self, xml_tree, element_location, attribute_name, is_structured=False):
        super().__init__()
        self.content_type_ = ATTRIBUTE_CONTENT_TYPE
        self.xml_tree_ = weakref.ref(xml_tree)
        self.element_location_ = weakref.ref(element_location)
        self.attribute_ = XMLAttribute(xml_tree, element_location.element, attribute_name, is_structured)
        self.property_locations_ = collections.OrderedDict()

        if is_structured:
            attribute_content = xml_tree.parse_attribute_content(self.attribute_)

            for key in attribute_content.keys():
                self.location_for_property(key, do_create=True)

        pass

    def get(self, default_value=None):
        return self.attribute_.get(default_value)

    def set(self, value):
        self.attribute_.set(value)

    def location_for_property(self, property_name, do_create=True):

        location = self.property_locations_.get(property_name, None)

        if location is None and do_create:
            location = XMLContentPropertyLocation(self.xml_tree_(), self, property_name)
            self.property_locations_[property_name] = location

        return location


class XMLElementLocation(DomainLocation):

    @property
    def attribute_locations(self):
        return self.attribute_locations_.values()

    @property
    def element(self):
        return self.element_

    def __init__(self, xml_tree, element):
        super().__init__()
        self.content_type_ = ELEMENT_CONTENT_TYPE
        self.xml_tree_ = weakref.ref(xml_tree)
        self.element_ = element
        self.attribute_locations_ = collections.OrderedDict()

        for key in element.keys():
            self.location_for_attribute(key, is_structured=xml_tree.is_structured_attribute(key), do_create=True)

    def get(self):
        return self.element_

    def set(self, value):
        self.element_ = value

    def location_for_attribute(self, attribute_name, is_structured, do_create=True):

        location = self.attribute_locations_.get(attribute_name, None)

        if location is None and do_create:
            location = XMLAttributeLocation(self.xml_tree_(), self, attribute_name, is_structured)
            self.attribute_locations_[attribute_name] = location

        return location


