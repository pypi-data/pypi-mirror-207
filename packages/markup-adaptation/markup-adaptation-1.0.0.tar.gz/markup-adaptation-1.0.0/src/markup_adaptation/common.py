import unicodedata, re

from .paths import last_path_component
from .formatting.functional import Functional


class DescribableMixin:

    @property
    def description(self):
        return self.description_

    @description.setter
    def description(self, value):
        self.description_ = value

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.description_ = ""


class IdentifiableMixin:

    @property
    def identifier(self):
        return self.identifier_

    @identifier.setter
    def identifier(self, value):
        self.identifier_ = value

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.identifier_ = ""


class LabelMixin:

    @property
    def label(self):
        return self.label_

    @label.setter
    def label(self, value):
        self.label_ = value

    @property
    def label_as_identifier(self):
        value = unicodedata.normalize('NFKD', self.label_).encode('ascii', 'ignore').decode('ascii')
        value = re.sub(r'[^\w\s-]', '', value).strip().lower()
        value = re.sub(r'[-\s]+', '-', value)
        return value

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_ = ""


class FormatMixin:

    @property
    def format_specifier(self):
        return self.format_specifier_

    @format_specifier.setter
    def format_specifier(self, value):
        self.format_specifier_ = value
        self.format_functional_ = None
        self.format_errors_ = []

    @property
    def format_functional_and_errors(self):

        if self.format_functional_ is None:
            self.format_functional_, self.format_errors_ = Functional.parse_text(self.format_specifier_)

        return self.format_functional_, self.format_errors_

    @property
    def format_functional(self):
        f, _ = self.format_functional_and_errors
        return f

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.format_specifier_ = ""
        self.format_functional_ = None
        self.format_errors_ = []


class ContentType(object):

    @property
    def name(self):
        return self.name_

    def __init__(self, name):
        self.name_ = name


class EnterGroup(object):

    @property
    def do_skip(self):
        return self.do_skip_

    @do_skip.setter
    def do_skip(self, value):
        self.do_skip_ = value

    def __init__(self, group):
        self.group = group
        self.do_skip_ = False


class ExitGroup(object):

    def __init__(self, group):
        self.group = group


class Group(IdentifiableMixin, DescribableMixin, object):

    class Iterator(object):

        def __init__(self, children, hide_groups=True, use_group_markers=False):
            self.stack_ = [(None, None, 0, children)]
            self.hide_groups_ = hide_groups
            self.use_group_markers_ = use_group_markers

        def __iter__(self):
            return self

        def __next__(self):

            node = None

            while self.stack_:

                node, marker, index, children = self.stack_[-1]

                if children is None:

                    try:
                        children = node.children
                        is_group = True
                    except AttributeError:
                        children = []
                        is_group = False

                    if is_group and self.use_group_markers_:
                        marker = EnterGroup(node)
                    else:
                        marker = None

                    self.stack_[-1] = node, marker, index, children

                    if node is not None and (not self.hide_groups_ or not is_group):
                        if marker:
                            node = marker
                        break

                if index >= len(children) or (marker and marker.do_skip):
                    self.stack_.pop()

                    try:
                        _ = node.children
                        is_group = True
                    except AttributeError:
                        is_group = False

                    if not self.hide_groups_ and is_group:
                        if self.use_group_markers_:
                            node = ExitGroup(node)
                        break

                    continue

                child = children[index]
                index += 1

                self.stack_[-1] = node, marker, index, children
                self.stack_.append((child, None, 0, None))

            if node is None:
                raise StopIteration()

            return node

    @property
    def children(self):
        return self.children_[:]

    def __init__(self):
        super().__init__()
        self.children_ = []
        self.identifiable_descendants_ = {}

    def add_child(self, child):
        self.children_.append(child)

        if child.identifier:
            key = last_path_component(child.identifier)
            self.identifiable_descendants_[key] = child

        elif isinstance(child, Group):

            tmp = dict(child.identifiable_descendants_.items())
            tmp.update(self.identifiable_descendants_)
            self.identifiable_descendants_ = tmp

    def define_defaults(self, configuration):

        for child in self.children:
            child.define_defaults(configuration)

    def __iter__(self):
        return self.iterate()

    def iterate(self, hide_groups=True, use_group_markers=False):
        return self.Iterator(self.children, hide_groups=hide_groups, use_group_markers=use_group_markers)

    class ControlScopeAdapter(object):

        def __init__(self, group):
            self.group = group

        def __getitem__(self, key):

            child = self.group.identifiable_descendants_[key]

            if isinstance(child, Group):
                child = Group.ControlScopeAdapter(child)

            return child