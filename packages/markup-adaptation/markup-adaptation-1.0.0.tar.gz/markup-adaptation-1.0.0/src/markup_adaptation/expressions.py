from .common import FormatMixin
from .formatting.functional import Configuration as FunctionalConfiguration

class ExpressiveMixin(object):

    def __init__(self):
        super().__init__()

    def __call__(self, configuration):
        return None


class ConstantMixin(object):

    def __init__(self):
        super().__init__()

    def __call__(self, configuration=None):
        return None


class Literal(ConstantMixin, object):

    @property
    def string(self):
        return self.string_

    @string.setter
    def string(self, value):
        self.string_ = value

    def __init__(self):
        super().__init__()
        self.string_ = ""

    def __call__(self, configuration=None):
        return self.string_


class Integer(ConstantMixin, object):

    @property
    def value(self):
        return self.value_

    @value.setter
    def value(self, value):
        self.value_ = value

    def __init__(self):
        super().__init__()
        self.value_ = 0

    def __call__(self, configuration=None):
        return self.value_


class Variable(FormatMixin, ExpressiveMixin, object):

    @property
    def name(self):
        return self.name_

    @name.setter
    def name(self, value):
        self.name_ = value

    def __init__(self):
        super().__init__()
        self.name_ = ""

    def __call__(self, configuration):

        result = configuration.get_variable(self.name)

        f = self.format_functional

        if f is not None:
            f_conf = FunctionalConfiguration()
            f_conf.define_builtins()
            f_conf["x"] = result
            result = f(f_conf)

        return result


class SwitchCase(object):

    @property
    def condition(self):
        return self.condition_

    @condition.setter
    def condition(self, value):
        self.condition_ = value

    @property
    def expression(self):
        return self.expression_

    @expression.setter
    def expression(self, value):
        self.expression_ = value

    def __init__(self):
        self.condition_ = None
        self.expression_ = None


class Switch(ExpressiveMixin, object):

    @property
    def cases(self):
        return self.cases_[:]

    @property
    def variable(self):
        return self.variable_

    @variable.setter
    def variable(self, value):
        self.variable_ = value

    @property
    def default_expression(self):
        return self.default_expression_

    @default_expression.setter
    def default_expression(self, value):
        self.default_expression_ = value

    def __init__(self):
        super().__init__()
        self.cases_ = []
        self.variable_ = None
        self.default_expression_ = None

    def add_case(self, case):
        self.cases_.append(case)

    def __call__(self, configuration):

        value = self.variable_(configuration)

        for case in self.cases_:
            condition_value = case.condition(configuration)

            if value == condition_value:
                expression_value = case.expression(configuration)
                return expression_value

        if callable(self.default_expression_):
            expression_value = self.default_expression_(configuration)
        else:
            expression_value = self.default_expression_

        return expression_value


class Concatenate(ExpressiveMixin, object):

    @property
    def parts(self):
        return self.parts_[:]

    def __init__(self):
        super().__init__()
        self.parts_ = []

    def add_part(self, part):
        self.parts_.append(part)

    def __call__(self, configuration):

        result = ""

        for part in self.parts_:
            part = part(configuration)
            result += part

        return result

