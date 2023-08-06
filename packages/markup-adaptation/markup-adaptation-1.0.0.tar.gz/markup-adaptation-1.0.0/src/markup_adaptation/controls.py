from .common import *
import collections


class ControlMixin(IdentifiableMixin, LabelMixin, object):

    def __init__(self):
        super().__init__()

    def define_defaults(self, configuration):
        pass


class Choice(ControlMixin, object):

    @property
    def options(self):
        return self.options_.values()

    def __init__(self):
        super().__init__()
        self.options_ = collections.OrderedDict()

    def add_option(self, option):
        self.options_[option.local_identifier] = option

    def define_defaults(self, configuration):

        if self.options_:

            option = list(self.options)[0]
            configuration.set_variable(self.identifier, option.constant())

    def choices_as_labels_and_identifiers(self):

        result = []

        for option in self.options:
            result.append((option.label, option.local_identifier))

        return result

    def option_for_local_identifier(self, local_id):
        result = self.options_.get(local_id, None)
        return result


class ChoiceOption(LabelMixin, object):

    @property
    def local_identifier(self):
        return self.local_identifier_

    @local_identifier.setter
    def local_identifier(self, value):
        self.local_identifier_ = value

    @property
    def constant(self):
        return self.constant_

    @constant.setter
    def constant(self, value):
        self.constant_ = value

    def __init__(self):
        super().__init__()
        self.local_identifier_ = ""
        self.constant_ = None


class URLControl(ControlMixin, object):

    @property
    def accepted_mime_types(self):
        return self.accepted_mime_types_[:]

    def __init__(self):
        super().__init__()
        self.accepted_mime_types_ = []

    def accept_mime_type(self, mime_type):
        self.accepted_mime_types_.append(mime_type)

    def define_defaults(self, configuration):
        configuration.set_variable(self.identifier, "")
