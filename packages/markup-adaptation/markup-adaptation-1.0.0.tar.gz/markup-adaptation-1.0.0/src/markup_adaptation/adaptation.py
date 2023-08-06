
import collections
import xml.etree.ElementTree as ET

from .common import *
from .paths import *


class Adaptation(DescribableMixin, object):

    @property
    def controls(self):
        return self.controls_

    @property
    def actions(self):
        return self.actions_[:]

    @property
    def identifier(self):
        return self.identifier_

    @identifier.setter
    def identifier(self, value):
        self.identifier_ = value

    def __init__(self):
        super().__init__()

        self.identifier_ = ""
        self.controls_ = Group()
        self.actions_ = []

    def add_control(self, control):
        self.controls_.add_child(control)

    def add_action(self, action):
        self.actions_.append(action)

    def define_defaults(self, configuration):

        for control in self.controls_.children:
            control.define_defaults(configuration)

    def apply(self, configuration, domain):

        for action in self.actions:
            action(configuration, domain)


class AdaptationSchema(object):

    @property
    def adaptations(self):
        return list(self.adaptations_.values())

    def __init__(self):
        self.adaptations_ = collections.OrderedDict()

    def define_defaults(self, configuration):

        for adaptation in self.adaptations:
            adaptation.define_defaults(configuration)

    def apply(self, configuration, domain):

        for adaptation in self.adaptations:
            adaptation.apply(configuration, domain)

    def add_adaptation(self, adaptation):
        self.adaptations_[adaptation.identifier] = adaptation

    class ControlScopeAdapter(object):

        def __init__(self, schema):
            self.schema = schema

        def __getitem__(self, key):
            return Group.ControlScopeAdapter(self.schema.adaptations_[key].controls_)

    def control_for_identifier(self, identifier):
        return get_path_value(identifier, self.ControlScopeAdapter(self))

    @staticmethod
    def from_file(file):
        file.seek(0)
        text = file.read()
        context, errors = AdaptationSchema.from_text(text)
        return context, errors

    @staticmethod
    def from_text(text):
        tree = ET.fromstring(text.decode("utf-8"))
        context, errors = AdaptationSchema.from_tree(tree)
        return context, errors

    @staticmethod
    def from_tree(tree):

        from .parser import parse_adaptation_schema_from_tree
        context, diagnostics = parse_adaptation_schema_from_tree(tree)
        return context, diagnostics.errors_


class MarkupTemplate(object):

    @property
    def schema(self):
        return self.schema_

    @property
    def domain(self):
        return self.domain_

    def __init__(self, schema, domain):
        self.schema_ = schema
        self.domain_ = domain
        self.schema_element_ = None

    def build_adaptation(self, configuration):

        result = self.domain_.independent_copy()
        self.schema_.apply(configuration, result)

        return result
