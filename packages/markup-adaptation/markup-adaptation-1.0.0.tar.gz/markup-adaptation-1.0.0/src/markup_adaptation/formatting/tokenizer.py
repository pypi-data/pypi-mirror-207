import re

from .regen import *


class FormatToken(object):

    __slots__ = "type_", "string_", "value_", "offset_"

    @property
    def type(self):
        return self.type_

    @property
    def string(self):
        return self.string_

    @property
    def value(self):
        return self.value_

    @property
    def offset(self):
        return self.offset_

    @property
    def limit(self):
        return self.offset_ + len(self.string_)

    def __init__(self, type, string, value, offset):
        self.type_ = type
        self.string_ = string
        self.value_ = value
        self.offset_ = offset


class FormatTokenizer(object):

    ERROR_TOKEN = 0
    WHITESPACE_TOKEN = 1
    LINE_BREAK_TOKEN = 2
    IDENTIFIER_TOKEN = 3
    NUMBER_TOKEN = 4
    STRING_TOKEN = 5
    LEFT_PARENTHESIS_TOKEN = 6
    RIGHT_PARENTHESIS_TOKEN = 7
    COMMA_TOKEN = 8

    LAST_TOKEN = 8

    WHITESPACE_RE_GROUP = 1
    LINE_BREAK_RE_GROUP = 3
    IDENTIFIER_RE_GROUP = 4

    NUMBER_RE_GROUP = 5
    STRING_RE_GROUP = 10

    LEFT_PARENTHESIS_RE_GROUP = 13
    RIGHT_PARENTHESIS_RE_GROUP = 14
    COMMA_RE_GROUP = 15

    RE_GROUPS_PER_TOKEN = [None, WHITESPACE_RE_GROUP, LINE_BREAK_RE_GROUP, IDENTIFIER_RE_GROUP, NUMBER_RE_GROUP,
                           STRING_RE_GROUP, LEFT_PARENTHESIS_RE_GROUP, RIGHT_PARENTHESIS_RE_GROUP, COMMA_RE_GROUP]

    STRING_ESCAPE_RE = re.compile(r"\\(.)", re.UNICODE)

    def __init__(self):

        def identifier_converter(x):
            return x.lower()

        def number_converter(x):

            f = float(x)
            i = int(f)

            if f == i:
                return i

            return f

        def replace_escape_seq(m):
            return m.group(1)

        def string_converter(x):

            x = x[1:-1]
            x = re.sub(FormatTokenizer.STRING_ESCAPE_RE, replace_escape_seq, x)
            return x

        self.token_specifiers_ = [("( |\\t)+", None),
                                  ("\\r?\\n", None),
                                  ("[A-Za-z_][A-Za-z_\\-0-9]*", identifier_converter),
                                  ("(([0-9]+(\\.[0-9]+)?)|(\\.[0-9]+))", number_converter),
                                  ("\"([^\"]|(\\.))*\"", string_converter),
                                  ("\\(", None),
                                  ("\\)", None),
                                  (",", None),]

        token_re = "|".join(["(" + r[0] + ")" for r in self.token_specifiers_])
        self.token_re_ = re.compile(token_re, re.UNICODE)

    def tokenize(self, text):

        tokens = []
        pos = 0

        while pos < len(text):

            match = self.token_re_.match(text, pos)

            if not match:
                tokens.append(FormatToken(self.ERROR_TOKEN, text, None, pos))
                return tokens

            string = None

            for token_type, group in enumerate(self.RE_GROUPS_PER_TOKEN):

                if not group:
                    continue

                string = match.group(group)

                if not string:
                    continue

                converter = self.token_specifiers_[token_type - 1][1]

                if converter:
                    value = converter(string)
                else:
                    value = string

                tokens.append(FormatToken(token_type, string, value, pos))
                break

            if not string:
                tokens.append(FormatToken(self.ERROR_TOKEN, string, None, pos))
                return tokens

            pos += len(string)

        return tokens


class FormatTokenGenerator(object):

    def __init__(self):

        whitespace_generator = ChoiceGenerator([" ", "\t"], 1, 10)
        line_break_generator = ChoiceGenerator(["\r\n", "\n"], 1, 1)
        identifier_generator = SequenceGenerator([AlphabetGenerator("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_", 1, 1), AlphabetGenerator("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_0123456789", 1, None)], 1, 1)
        number_generator = ChoiceGenerator([SequenceGenerator([AlphabetGenerator("0123456789", 1, None), SequenceGenerator([AtomicGenerator(".", 1, 1), AlphabetGenerator("0123456789", 1, None)], 0, 1)], 1, 1),
                                            SequenceGenerator([AtomicGenerator(".", 1, 1), AlphabetGenerator("0123456789", 1, None)], 1, 1)], 1, 1)

        string_generator = SequenceGenerator([AlphabetGenerator("\"", 1, 1), ChoiceGenerator(["\\", AlphabetGenerator("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_", 1, 1)], 0, None), AlphabetGenerator("\"", 1, 1)], 1, 1)

        self.token_generators_ = \
                          [whitespace_generator,
                           line_break_generator,
                           identifier_generator,
                           number_generator,
                           string_generator,
                           AtomicGenerator("(", 1, 1),
                           AtomicGenerator(")", 1, 1),
                           AtomicGenerator(",", 1, 1),]

        self.delimiters_ = [FormatTokenizer.WHITESPACE_TOKEN,
                            FormatTokenizer.LINE_BREAK_TOKEN,
                            FormatTokenizer.LEFT_PARENTHESIS_TOKEN,
                            FormatTokenizer.RIGHT_PARENTHESIS_TOKEN,
                            FormatTokenizer.COMMA_TOKEN,]

        self.tokenizer_ = FormatTokenizer()

    def __call__(self, offset=0, type=None):

        if not type or type >= FormatTokenizer.LAST_TOKEN:
            type = random.randint(1, FormatTokenizer.LAST_TOKEN)

        token_generator = self.token_generators_[type - 1]
        string = token_generator.generate()
        tokens = self.tokenizer_.tokenize(string)

        if not tokens or tokens[0].type != type:
            raise BaseException("Implementation error in markup_adaptation/format_tokenizer/FormatTokenGenerator")

        tokens[0].offset_ = offset
        return tokens[0]

