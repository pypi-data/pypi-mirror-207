import re

from .tokenizer import FormatTokenizer


class UndefinedError(KeyError):
    pass


class NotAFunctional(RuntimeError):
    pass


def capitalise(str):

    if not str:
        return str

    return str[0].title() + str[1:]


class Configuration(object):

    def __init__(self):
        self.definitions_ = {}

    def __getitem__(self, key):
        try:
            return self.definitions_[key]
        except KeyError:
            raise UndefinedError(key)

    def __setitem__(self, key, value):
        self.definitions_[key]= value

    def define_builtins(self):

        self["join"] = lambda separator, *args: separator.join(*args)
        self["split"] = lambda str, separator: str.split(separator)
        self["uppercase"] = lambda str: str.upper()
        self["lowercase"] = lambda str: str.lower()
        self["capitalise"] = lambda str: capitalise(str)


class ExpressiveMixin(object):

    def format(self):
        return ""

    def __call__(self, environment):
        return None


class Literal(ExpressiveMixin, object):

    @property
    def value(self):
        return self.value_

    def __init__(self, value):
        super().__init__()
        self.value_ = value

    def __eq__(self, other):

        if other is None or not isinstance(other, Literal) or self.__class__ != other.__class__:
            return False

        return self.value_ == other.value_

    def __call__(self, environment):
        return self.value_


def escape_character(m):

    if m.group(0) == "\"":
        return "\\\""
    else:
        return "\\\\"


class String(Literal):

    def __init__(self, value):
        super().__init__(value)

    def format(self):
        result = re.sub("[\"\\\\]", escape_character, self.value_)
        return '"' + result + '"'


class Number(Literal):

    def __init__(self, value):
        super().__init__(value)

    def format(self):
        if int(self.value_) == self.value_:
            return "{:d}".format(self.value_)
        else:
            return "{:.6f}".format(self.value_)


class Identifier(ExpressiveMixin, object):

    @property
    def value(self):
        return self.value_

    def __init__(self, value):
        self.value_ = value

    def __eq__(self, other):

        if other is None or not isinstance(other, Identifier) or self.__class__ != other.__class__:
            return False

        return self.value_ == other.value_

    def __call__(self, configuration):
        result = configuration[self.value_]
        return result

    def format(self):
        return self.value_


class Functional(ExpressiveMixin, object):

    def __init__(self, name=None, *args):
        self.name_ = name
        self.arguments_ = list(*args)

    def __eq__(self, other):

        if other is None or not isinstance(other, Functional):
            return False

        if not (self.name_ == other.name_):
            return False

        if len(self.arguments_) != len(other.arguments_):
            return False

        for index, left_arg in enumerate(self.arguments_):
            right_arg = other.arguments_[index]

            if not (left_arg == right_arg):
                return False

        return True

    def __call__(self, configuration):
        f = configuration[self.name_]

        if not callable(f):
            raise NotAFunctional(self.name_)

        arg_values = [arg(configuration) for arg in self.arguments_]
        return f(*arg_values)

    def format(self):
        return "{}({})".format(self.name_, ", ".join([x.format() for x in self.arguments_]))

    @staticmethod
    def parse_text(text):

        tokenizer = FormatTokenizer()
        tokens = tokenizer.tokenize(text)

        tokens = [t for t in tokens if t.type != FormatTokenizer.WHITESPACE_TOKEN and t.type != FormatTokenizer.LINE_BREAK_TOKEN]

        result, _, errors = Functional.parse_functional(text, tokens, strict=True)
        return result, errors

    @staticmethod
    def parse_argument_text(text):

        tokenizer = FormatTokenizer()
        tokens = tokenizer.tokenize(text)

        tokens = [t for t in tokens if t.type != FormatTokenizer.WHITESPACE_TOKEN and t.type != FormatTokenizer.LINE_BREAK_TOKEN]

        result, _, errors = Functional.parse_argument(text, tokens, strict=False)
        return result, errors

    @staticmethod
    def parse_argument(text, tokens, strict, token_base=0):

        PARSE_START = 1
        PARSE_IDENTIFIER_OR_FUNCTIONAL = 2
        PARSE_END = 3

        errors = []
        result = None

        state = PARSE_START
        index = 0

        while index < len(tokens):

            token = tokens[index]
            token_index = index; index += 1

            if state == PARSE_START:

                if token.type == FormatTokenizer.NUMBER_TOKEN:

                    result = Number(token.value)
                    state = PARSE_END
                    continue

                if token.type == FormatTokenizer.STRING_TOKEN:

                    result = String(token.value)
                    state = PARSE_END
                    continue

                if token.type == FormatTokenizer.IDENTIFIER_TOKEN:

                    result = token.value
                    state = PARSE_IDENTIFIER_OR_FUNCTIONAL
                    continue

                errors.append("Unexpected token, expecting number, identifier or functional: " + token.string)
                return None, token_index, errors

            if state == PARSE_IDENTIFIER_OR_FUNCTIONAL:

                if token.type == FormatTokenizer.LEFT_PARENTHESIS_TOKEN:

                    token_index -= 1
                    token = tokens[token_index]

                    result, f_index, f_errors = Functional.parse_functional(
                        text[token.offset:], tokens[token_index:], strict, token.offset)

                    errors.extend(f_errors)

                    if result is None:
                        return None, token_index, errors

                    index = token_index + f_index
                    state = PARSE_END
                    continue

                result = Identifier(result)
                state = PARSE_END

            if state == PARSE_END:

                if not strict:
                    return result, token_index, errors

                errors.append("Unexpected token at end of argument: " + token.string)
                return None, token_index, errors

        if state != PARSE_END:
            errors.append("Empty or incomplete argument: " + text[:len(text) if len(text) < 20 else 20])
            return None, index, errors

        return result, index, errors

    @staticmethod
    def is_argument_start(token):
        return (token.type == FormatTokenizer.IDENTIFIER_TOKEN or token.type == FormatTokenizer.NUMBER_TOKEN or
                token.type == FormatTokenizer.STRING_TOKEN)

    @staticmethod
    def is_functional_start(token):
        return token.type == FormatTokenizer.IDENTIFIER_TOKEN

    @staticmethod
    def parse_functional(text, tokens, strict, token_base=0):

        """

        :param text:
        :param tokens:
        :return:


        functional ::= identifier "(" (argument ("," argument)*)+ ")"
        argument ::= functional | identifier | number

        """

        PARSE_START = 1
        PARSE_OPEN_PARENTHESIS = 2
        PARSE_ARGUMENT = 3
        PARSE_ARGUMENT_OR_CLOSE_PARENTHESIS = 4
        PARSE_ARGUMENT_SEPARATOR_OR_CLOSE_PARENTHESIS = 5
        PARSE_END = 6

        errors = []
        result = Functional()

        state = PARSE_START
        index = 0

        while index < len(tokens):

            token = tokens[index]
            token_index = index; index += 1

            if state == PARSE_START:

                if not Functional.is_functional_start(token):
                    errors.append("Unexpected token, expecting identifier: " + token.string)
                    return None, token_index, errors

                result.name_ = token.value

                state = PARSE_OPEN_PARENTHESIS
                continue

            if state == PARSE_OPEN_PARENTHESIS:

                if token.type != FormatTokenizer.LEFT_PARENTHESIS_TOKEN:
                    errors.append("Unexpected token, expecting (: " + token.string)
                    return None, token_index, errors

                state = PARSE_ARGUMENT_OR_CLOSE_PARENTHESIS
                continue

            if state == PARSE_ARGUMENT or state == PARSE_ARGUMENT_OR_CLOSE_PARENTHESIS:

                if Functional.is_argument_start(token):

                    argument, arg_index, arg_errors = Functional.parse_argument(text[token.offset:],
                                                                                tokens[token_index:], False,
                                                                                token.offset)

                    errors.extend(arg_errors)

                    if argument is None:
                        return None, token_index, errors

                    result.arguments_.append(argument)

                    index = token_index + arg_index
                    state = PARSE_ARGUMENT_SEPARATOR_OR_CLOSE_PARENTHESIS
                    continue

                if state == PARSE_ARGUMENT:
                    errors.append("Unexpected token, expecting argument: " + token.string)
                    return None, token_index, errors

                if token.type != FormatTokenizer.RIGHT_PARENTHESIS_TOKEN:
                    errors.append("Unexpected token, expecting argument or right parenthesis: " + token.string)
                    return None, token_index, errors

                state = PARSE_END
                continue

            if state == PARSE_ARGUMENT_SEPARATOR_OR_CLOSE_PARENTHESIS:

                if token.type == FormatTokenizer.COMMA_TOKEN:

                    state = PARSE_ARGUMENT
                    continue

                if token.type != FormatTokenizer.RIGHT_PARENTHESIS_TOKEN:
                    errors.append("Unexpected token, expecting ): " + token.string)
                    return None, token_index, errors

                state = PARSE_END
                continue

            if state == PARSE_END:

                if not strict:
                    return result, token_index, errors

                errors.append("Unexpected token at end of functional: " + token.string)
                return None, token_index, errors

        if state != PARSE_END and state != PARSE_OPEN_PARENTHESIS:
            errors.append("Empty or incomplete functional: " + text[:len(text) if len(text) < 20 else 20])
            return None, index, errors

        if state == PARSE_OPEN_PARENTHESIS:
            result.arguments_.append(Identifier("x"))
        
        return result, index, errors