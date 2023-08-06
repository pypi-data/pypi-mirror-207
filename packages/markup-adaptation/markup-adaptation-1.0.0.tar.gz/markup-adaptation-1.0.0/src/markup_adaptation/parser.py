from .controls import Choice, ChoiceOption, URLControl
from .actions import Assign, Edit
from .common import Group
from .expressions import *
from .domain import (DomainQueryMixin, ElementQuery, AttributeQuery, StylePropertyQuery,
                     ElementSelector, AttributeSelector, StylePropertySelector)

from xml.etree import ElementTree as ET


class Diagnostics(object):

    def __init__(self):
        self.errors_ = []

    def unexpected_tag(self, tag_name, container_name, expectations):
        self.errors_.append("Unexpected tag \"{}\" in <{}> element: Expected one of {{{}}}.".format(tag_name,
                            container_name, ", ".join(["<" + x + ">" for x in expectations])))

    def missing_child_in_element(self, container_name):
        self.errors_.append("Missing child in <{}> element".format(container_name))

    def unexpected_child_in_element(self, tag_name, container_name):
        self.errors_.append("Unexpected child \"{}\" in <{}> element".format(tag_name,
                            container_name))

    def expecting_at_least(self, tag_name, container_name, min_count):
        self.errors_.append("Expecting at least {:d} consecutive <{}> elements in <{}>.".format(min_count, tag_name, container_name))

    def expecting_at_most(self, tag_name, container_name, min_count):
        self.errors_.append("Expecting at most {:d} consecutive <{}> elements in <{}>.".format(min_count, tag_name, container_name))

    def invalid_format_specifier(self, errors):
        self.errors_.append("Format specifier contains errors: " + "\n".join(errors))


def tag_name(element):

    if element.tag.startswith('{http://xml.hdng.website/Adaptations.xsd}'):
        return element.tag[len('{http://xml.hdng.website/Adaptations.xsd}'):]

    return element.tag


def adapt_parse_handler(handler, parent_assignment, **kwargs):
     return lambda arg1, arg2, arg3, arg4: handler(arg1, arg2, arg3, arg4, parent_assignment, **kwargs)


def parse_element_sequence(elements, parent_element, parent_object, expectations, diagnostics):

    actual_counts = [0] * len(expectations)
    expectations_offset = 0

    while elements and expectations:

        element = elements.pop(0)

        element_name = tag_name(element)

        expectation_index = -1
        applicable_max_count = 0
        handler = None

        for index, specifier in enumerate(expectations):
            name, min_count, max_count, handler = specifier

            if name == element_name:
                expectation_index = index + expectations_offset
                applicable_max_count = max_count
                break

            handler = None

            if actual_counts[index + expectations_offset] < min_count:
                diagnostics.expecting_at_least(name, tag_name(parent_element), min_count)
                return False

        if expectation_index < 0:
            # diagnostics.unexpected_tag(tag_name(element), tag_name(tree_element), expectations)
            elements.insert(0, element)
            return True

        actual_counts[expectation_index] += 1

        if applicable_max_count and actual_counts[expectation_index] > applicable_max_count:
            diagnostics.expecting_at_most(tag_name(element), tag_name(parent_element), applicable_max_count)
            return False

        if applicable_max_count and actual_counts[expectation_index] == applicable_max_count:
            expectations = expectations[expectation_index - expectations_offset + 1:]
            expectations_offset = expectation_index + 1

        if not handler:
            continue

        handler(element, parent_element, parent_object, diagnostics)

    return True


def parse_element_choice(elements, parent_element, parent_object, handlers, diagnostics):

    expectations = sorted(handlers.keys())
    actual_counts = {}

    while elements:

        element = elements.pop(0)

        element_name = tag_name(element)
        min_count, max_count, handler = handlers.get(element_name, (0, None, None))

        if not handler:
            diagnostics.unexpected_tag(tag_name(element), tag_name(parent_element), expectations)
            return False

        element_count = actual_counts.setdefault(element_name, 0)
        element_count += 1

        if max_count and element_count > max_count:
            diagnostics.expecting_at_most(element_name, tag_name(parent_element), max_count)
            return False

        actual_counts[element_name] = element_count

        handler(element, parent_element, parent_object, diagnostics)

    for element_name, element_count in actual_counts.items():

        min_count, _, _ = handlers.get(element_name, (0, None, None))

        if element_count < min_count:
            diagnostics.expecting_at_least(element_name, tag_name(parent_element), min_count)
            return False

    return True


def parse_literal(tree_element, parent_element, parent, diagnostics,
                 add_to_parent=lambda child, parent: None):

    if tag_name(tree_element) != "literal":
        diagnostics.unexpected_tag(tag_name(tree_element), tag_name(parent_element), ["literal"])
        return

    value = ""

    for text in tree_element.itertext():
        value += text

    literal = Literal()
    literal.string = value

    add_to_parent(literal, parent)


def parse_integer(tree_element, parent_element, parent, diagnostics,
                 add_to_parent=lambda child, parent: None):

    if tag_name(tree_element) != "integer":
        diagnostics.unexpected_tag(tag_name(tree_element), tag_name(parent_element), ["integer"])
        return

    value = ""

    for text in tree_element.itertext():
        value += text

    value = int(value)

    integer = Integer()
    integer.value = value

    add_to_parent(integer, parent)


def parse_description(tree_element, parent_element, describable, diagnostics):

    if tag_name(tree_element) != "description":
        diagnostics.unexpected_tag(tag_name(tree_element), tag_name(parent_element), ["description"])
        return

    describable.description = ""

    for text in tree_element.itertext():
        describable.description += text


def parse_label(tree_element, parent_element, labelled, diagnostics):

    if tag_name(tree_element) != "label":
        diagnostics.unexpected_tag(tag_name(tree_element), tag_name(parent_element), ["label"])
        return

    labelled.label = ""

    for text in tree_element.itertext():
        labelled.label += text


def set_condition_in_parent(condition, parent):
    parent.condition = condition


def set_constant_in_parent(constant, parent):
    parent.constant = constant

def set_expression_in_parent(expression, parent):
    parent.expression = expression


def set_default_expression_in_parent(expression, parent):
    parent.default_expression = expression


def set_variable_in_parent(variable, parent):
    parent.variable = variable


def set_query_in_parent(query, parent):
    parent.query = query


def add_part_to_parent(part, parent):
    parent.add_part(part)


def add_selector_to_parent(selector, parent):
    parent.add_selector(selector)


def set_controls_in_parent(controls, parent):
    parent.controls = controls


def parse_option(tree_element, parent_element, parent, diagnostics,
                 add_to_parent=lambda child, parent: parent.add_option(child)):

    if tag_name(tree_element) != "option":
        diagnostics.unexpected_tag(tag_name(tree_element), tag_name(parent_element), ["option"])
        return

    option = ChoiceOption()
    children = list(tree_element)

    defined_id = tree_element.get("local_id", "")
    option.local_identifier = defined_id
    expectations = [("label", 1, 1, parse_label)]

    if not parse_element_sequence(children, tree_element, option, expectations, diagnostics):
        return

    handlers = {"literal": (0, 1, adapt_parse_handler(parse_literal, set_constant_in_parent)),
                "integer": (0, 1, adapt_parse_handler(parse_integer, set_constant_in_parent)),}

    if not parse_element_choice(children, tree_element, option, handlers, diagnostics):
        return

    add_to_parent(option, parent)


def parse_group(tree_element, parent_element, parent, diagnostics,
                add_to_parent=lambda child, parent: parent.add_child(child),
                alias="group"):

    if tag_name(tree_element) != alias:
        diagnostics.unexpected_tag(tag_name(tree_element), tag_name(parent_element), [alias])
        return

    id = diagnostics.provide_id_for_element(tree_element)

    group = Group()
    children = list(tree_element)

    defined_id = tree_element.get("id", "")
    group.identifier = diagnostics.global_name_for(id) if defined_id else ""

    with diagnostics.name_scope(defined_id):

        expectations = [("description", 0, 1, parse_description)]

        if not parse_element_sequence(children, tree_element, group, expectations, diagnostics):
            return

        handlers = {"group": (0, None, parse_group),
                    "choice": (0, None, parse_choice),
                    "url": (0, None, parse_url) }

        if not parse_element_choice(children, tree_element, group, handlers, diagnostics):
            return

        add_to_parent(group, parent)


def parse_choice(tree_element, parent_element, parent, diagnostics,
                 add_to_parent=lambda child, parent: parent.add_child(child)):

    if tag_name(tree_element) != "choice":
        diagnostics.unexpected_tag(tag_name(tree_element), tag_name(parent_element), ["choice"])
        return

    id = diagnostics.provide_id_for_element(tree_element)

    choice = Choice()
    children = list(tree_element)

    defined_id = tree_element.get("id", "")
    choice.identifier = diagnostics.global_name_for(id) if defined_id else ""

    with diagnostics.name_scope(defined_id):

        expectations = [("label", 1, 1, parse_label)]

        if not parse_element_sequence(children, tree_element, choice, expectations, diagnostics):
            return

        handlers = {"option": (0, None, parse_option)}

        if not parse_element_choice(children, tree_element, choice, handlers, diagnostics):
            return

        add_to_parent(choice, parent)


def parse_url(tree_element, parent_element, parent, diagnostics,
              add_to_parent=lambda child, parent: parent.add_child(child)):

    if tag_name(tree_element) != "url":
        diagnostics.unexpected_tag(tag_name(tree_element), tag_name(parent_element), ["url"])
        return

    id = diagnostics.provide_id_for_element(tree_element)

    url_control = URLControl()
    children = list(tree_element)

    defined_id = tree_element.get("id", "")
    url_control.identifier = diagnostics.global_name_for(id) if defined_id else ""

    with diagnostics.name_scope(defined_id):

        expectations = [("label", 1, 1, parse_label)]

        if not parse_element_sequence(children, tree_element, url_control, expectations, diagnostics):
            return

        accepted_mime_types = tree_element.get("accepted_mime_types", "").split()

        for mime_type in accepted_mime_types:
            url_control.accept_mime_type(mime_type)

        add_to_parent(url_control, parent)


def add_control_to_parent(action, parent):
    parent.add_control(action)


def parse_controls(tree_element, parent_element, parent, diagnostics,
                  add_to_parent=lambda child, parent: parent.add_child(child)):

    if tag_name(tree_element) != "controls":
        diagnostics.unexpected_tag(tag_name(tree_element), tag_name(parent_element), ["controls"])
        return False

    children = list(tree_element)

    handlers = {"group": (0, None, adapt_parse_handler(parse_group, add_to_parent)),
                "choice": (0, None, adapt_parse_handler(parse_choice, add_to_parent)),
                "url": (0, None, adapt_parse_handler(parse_url, add_to_parent)) }

    if not parse_element_choice(children, tree_element, parent, handlers, diagnostics):
        return False

    return True


def parse_variable(tree_element, parent_element, parent, diagnostics,
                        add_to_parent=lambda child, parent: parent.add_child(child)):

    if tag_name(tree_element) != "variable":
        diagnostics.unexpected_tag(tag_name(tree_element), tag_name(parent_element), ["variable"])
        return

    value = ""

    for text in tree_element.itertext():
        value += text

    variable = Variable()
    variable.name = diagnostics.global_name_for(value)
    variable.format_specifier = tree_element.get("format", "")

    _, errors = variable.format_functional_and_errors

    if variable.format_specifier and errors:
        diagnostics.invalid_format_specifier(errors)
        return

    add_to_parent(variable, parent)


def parse_switch_case(tree_element, parent_element, parent, diagnostics,
                      add_to_parent=lambda child, parent: parent.add_case(child)):

    if tag_name(tree_element) != "case":
        diagnostics.unexpected_tag(tag_name(tree_element), tag_name(parent_element), ["case"])
        return

    case = SwitchCase()
    children = list(tree_element)

    if len(children) < 2:
        diagnostics.missing_child_in_element(tag_name(tree_element))

    if len(children) > 2:
        diagnostics.unexpected_child_in_element(children[2].tag, tag_name(tree_element))

    handlers = {"literal": (0, 1, adapt_parse_handler(parse_literal, set_condition_in_parent)),
                "integer": (0, 1, adapt_parse_handler(parse_integer, set_condition_in_parent)),}

    if not parse_element_choice(children[0:1], tree_element, case, handlers, diagnostics):
        return

    handlers = {"literal": (0, 1, adapt_parse_handler(parse_literal, set_expression_in_parent)),
                "integer": (0, 1, adapt_parse_handler(parse_integer, set_expression_in_parent)),
                "variable": (0, 1, adapt_parse_handler(parse_variable, set_expression_in_parent)),
                "switch": (0, 1, adapt_parse_handler(parse_switch, set_expression_in_parent)),
                "concatenate": (0, 1, adapt_parse_handler(parse_concatenate, set_expression_in_parent)),
               }

    if not parse_element_choice(children[1:2], tree_element, case, handlers, diagnostics):
        return

    add_to_parent(case, parent)


def parse_switch_default(tree_element, parent_element, parent, diagnostics):

    if tag_name(tree_element) != "default":
        diagnostics.unexpected_tag(tag_name(tree_element), tag_name(parent_element), ["default"])
        return

    children = list(tree_element)

    if len(children) < 1:
        diagnostics.missing_child_in_element(tag_name(tree_element))

    if len(children) > 1:
        diagnostics.unexpected_child_in_element(children[1].tag, tag_name(tree_element))

    handlers = {"literal": (0, 1, adapt_parse_handler(parse_literal, set_default_expression_in_parent)),
                "integer": (0, 1, adapt_parse_handler(parse_integer, set_default_expression_in_parent)),
                "variable": (0, 1, adapt_parse_handler(parse_variable, set_default_expression_in_parent)),
                "switch": (0, 1, adapt_parse_handler(parse_switch, set_default_expression_in_parent)),
                "concatenate": (0, 1, adapt_parse_handler(parse_concatenate, set_default_expression_in_parent)),
               }

    if not parse_element_choice(children, tree_element, parent, handlers, diagnostics):
        return


def parse_switch(tree_element, parent_element, parent, diagnostics,
                        add_to_parent=lambda child, parent: parent.add_child(child)):

    if tag_name(tree_element) != "switch":
        diagnostics.unexpected_tag(tag_name(tree_element), tag_name(parent_element), ["switch"])
        return

    switch = Switch()
    children = list(tree_element)

    expectations = [("variable", 1, 1, adapt_parse_handler(parse_variable, set_variable_in_parent))]

    if not parse_element_sequence(children, tree_element, switch, expectations, diagnostics):
        return

    handlers = {"case": (0, None, parse_switch_case),
                "default": (0, 1, parse_switch_default),
               }

    if not parse_element_choice(children, tree_element, switch, handlers, diagnostics):
        return

    add_to_parent(switch, parent)


def parse_concatenate(tree_element, parent_element, parent, diagnostics,
                        add_to_parent=lambda child, parent: parent.add_child(child)):

    if tag_name(tree_element) != "concatenate":
        diagnostics.unexpected_tag(tag_name(tree_element), tag_name(parent_element), ["concatenate"])
        return

    concatenation = Concatenate()
    children = list(tree_element)

    handlers = {"literal": (0, None, adapt_parse_handler(parse_literal, add_part_to_parent)),
                "integer": (0, None, adapt_parse_handler(parse_integer, add_part_to_parent)),
                "variable": (0, None, adapt_parse_handler(parse_variable, add_part_to_parent)),
                "switch": (0, None, adapt_parse_handler(parse_switch, add_part_to_parent)),
               }

    if not parse_element_choice(children, tree_element, concatenation, handlers, diagnostics):
        return

    add_to_parent(concatenation, parent)


XPATH_ELEMENT = ET.Element("test")


def parse_element_selector(tree_element, parent_element, parent, diagnostics,
                           add_to_parent=lambda child, parent: parent.add_child(child)):

    if tag_name(tree_element) != "element":
        diagnostics.unexpected_tag(tag_name(tree_element), tag_name(parent_element), ["element"])
        return

    selector = ElementSelector()

    value = ""

    for text in tree_element.itertext():
        value += text

    XPATH_ELEMENT.findall(value)

    selector.text = value

    add_to_parent(selector, parent)


def parse_attribute_selector(tree_element, parent_element, parent, diagnostics,
                             add_to_parent=lambda child, parent: parent.add_child(child),
                             do_create_if_missing=False):

    if tag_name(tree_element) != "attribute":
        diagnostics.unexpected_tag(tag_name(tree_element), tag_name(parent_element), ["attribute"])
        return

    selector = AttributeSelector()
    selector.do_create_if_missing = do_create_if_missing

    value = ""

    for text in tree_element.itertext():
        value += text

    selector.attribute_name = value

    add_to_parent(selector, parent)


def parse_style_property_selector(tree_element, parent_element, parent, diagnostics,
                                  add_to_parent=lambda child, parent: parent.add_child(child),
                                  do_create_if_missing=False):

    if tag_name(tree_element) != "style_property":
        diagnostics.unexpected_tag(tag_name(tree_element), tag_name(parent_element), ["style_property"])
        return

    selector = StylePropertySelector()
    selector.do_create_if_missing = do_create_if_missing

    value = ""

    for text in tree_element.itertext():
        value += text

    selector.property_name = value

    add_to_parent(selector, parent)


def parse_locations(tree_element, parent_element, parent, diagnostics,
                    add_to_parent=lambda child, parent: parent.add_child(child),
                    do_create_if_missing=False):

    if tag_name(tree_element) != "locations":
        diagnostics.unexpected_tag(tag_name(tree_element), tag_name(parent_element), ["locations"])
        return

    expectations = None
    query = None
    children = list(tree_element)

    if not children:
        query = DomainQueryMixin()
    elif tag_name(children[0]) == "element":
        query = ElementQuery()
        expectations = [("element", 0, None, adapt_parse_handler(parse_element_selector, add_selector_to_parent))]
    elif tag_name(children[0]) == "attribute":
        query = AttributeQuery()
        expectations = [("attribute", 0, None, adapt_parse_handler(parse_attribute_selector, add_selector_to_parent,  do_create_if_missing=do_create_if_missing))]
    elif tag_name(children[0]) == "style_property":
        query = StylePropertyQuery()
        expectations = [("style_property", 0, None, adapt_parse_handler(parse_style_property_selector, add_selector_to_parent, do_create_if_missing=do_create_if_missing))]

    if expectations is not None:
        if not parse_element_sequence(children, tree_element, query, expectations, diagnostics):
            return

    add_to_parent(query, parent)


def parse_edit_action(tree_element, parent_element, parent, diagnostics,
                      add_to_parent=lambda child, parent: parent.add_child(child)):

    if tag_name(tree_element) != "edit":
        diagnostics.unexpected_tag(tag_name(tree_element), tag_name(parent_element), ["edit"])
        return

    action = Edit()
    children = list(tree_element)

    expectations = [("locations", 1, 1, adapt_parse_handler(parse_locations, set_query_in_parent))]

    if not parse_element_sequence(children, tree_element, action, expectations, diagnostics):
        return

    handlers = {"edit": (0, None, adapt_parse_handler(parse_edit_action, add_to_parent)),
                "assign": (0, None, adapt_parse_handler(parse_assign_action, add_to_parent)),}

    if not parse_element_choice(children, tree_element, action, handlers, diagnostics):
        return False

    add_to_parent(action, parent)


def parse_assign_action(tree_element, parent_element, parent, diagnostics,
                        add_to_parent=lambda child, parent: parent.add_child(child)):

    if tag_name(tree_element) != "assign":
        diagnostics.unexpected_tag(tag_name(tree_element), tag_name(parent_element), ["assign"])
        return

    action = Assign()
    children = list(tree_element)

    expectations = [("locations", 1, 1, adapt_parse_handler(parse_locations, set_query_in_parent, do_create_if_missing=True))]

    if not parse_element_sequence(children, tree_element, action, expectations, diagnostics):
        return

    handlers = {"literal": (0, 1, adapt_parse_handler(parse_literal, set_expression_in_parent)),
                "integer": (0, 1, adapt_parse_handler(parse_integer, set_expression_in_parent)),
                "variable": (0, 1, adapt_parse_handler(parse_variable, set_expression_in_parent)),
                "switch": (0, 1, adapt_parse_handler(parse_switch, set_expression_in_parent)),
                "concatenate": (0, 1, adapt_parse_handler(parse_concatenate, set_expression_in_parent)),
               }

    if len(children) < 1:
        diagnostics.missing_child_in_element(tag_name(tree_element))

    if len(children) > 1:
        diagnostics.unexpected_child_in_element(children[1].tag, tag_name(tree_element))

    if not parse_element_choice(children, tree_element, action, handlers, diagnostics):
        return

    add_to_parent(action, parent)


def add_action_to_parent(action, parent):
    parent.add_action(action)


def parse_actions(tree_element, parent_element, parent, diagnostics,
                  add_to_parent=lambda child, parent: parent.add_child(child)):

    if tag_name(tree_element) != "actions":
        diagnostics.unexpected_tag(tag_name(tree_element), tag_name(parent_element), ["actions"])
        return False

    children = list(tree_element)

    handlers = {"edit": (0, None, adapt_parse_handler(parse_edit_action, add_to_parent)),
                "assign": (0, None, adapt_parse_handler(parse_assign_action, add_to_parent)),}

    if not parse_element_choice(children, tree_element, parent, handlers, diagnostics):
        return False

    return True


def parse_adaptation(tree_element, parent_element, parent, diagnostics,
                     add_to_parent=lambda child, parent: parent.add_adaptation(child)):

    if tag_name(tree_element) != "adaptation":
        diagnostics.unexpected_tag(tag_name(tree_element), tag_name(parent_element), ["adaptation"])
        return

    from .adaptation import Adaptation

    id = diagnostics.provide_id_for_element(tree_element)

    adaptation = Adaptation()
    children = list(tree_element)

    adaptation.identifier = diagnostics.global_name_for(id)

    with diagnostics.name_scope(id):

        expectations = [("description", 0, 1, parse_description),
                        ("controls", 0, 1, adapt_parse_handler(parse_controls, add_control_to_parent)),
                        ("actions", 0, 1, adapt_parse_handler(parse_actions, add_action_to_parent))]

        if not parse_element_sequence(children, tree_element, adaptation, expectations, diagnostics):
            return

        add_to_parent(adaptation, parent)


class ExtendedDiagnostics(Diagnostics):

    class NameScope(object):

        def __init__(self, parent, name):
            self.parent = parent
            self.name = name

        def __enter__(self):
            if self.name:
                self.parent.name_scopes_.append(self.name)
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            if self.name:
                self.parent.name_scopes_.pop()

    @property
    def current_name_prefix(self):
        return ".".join(self.name_scopes_)

    def __init__(self):
        super().__init__()
        self.name_scopes_ = []
        self.element_counts_ = {}

    def name_scope(self, name):
        return self.NameScope(self, name)

    def count_element(self, name):
        value = self.element_counts_.setdefault(name, 0)
        value += 1
        self.element_counts_[name] = value
        return value

    def provide_id_for_element(self, element):

        id = element.get("id", None)

        if id is None:
            name = tag_name(element)
            count = self.count_element(name)
            id = "{}-{:d}".format(name, count)

        return id

    def global_name_for(self, name):
        prefix = self.current_name_prefix

        if prefix:
            name = prefix + "." + name

        return name


def parse_adaptation_schema_from_tree(tree):

    from .adaptation import AdaptationSchema
    context = AdaptationSchema()

    diagnostics = ExtendedDiagnostics()

    if tag_name(tree) != "schema":
        diagnostics.unexpected_tag(tag_name(tree), "root", ["schema"])
        return context, diagnostics

    for element in tree:
        if tag_name(element) != "adaptation":
            diagnostics.unexpected_tag(tag_name(element), "adaptations", ["adaptation"])
            continue

        parse_adaptation(element, tree, context, diagnostics)

    return context, diagnostics