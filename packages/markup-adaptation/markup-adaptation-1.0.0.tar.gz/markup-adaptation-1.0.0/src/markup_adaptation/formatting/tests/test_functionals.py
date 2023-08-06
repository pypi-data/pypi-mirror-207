from django.test import SimpleTestCase, TestCase
from wagtail.tests.utils import WagtailTestUtils

import sys

from ..functional import *
from ..tokenizer import *

TOKEN_GENERATOR = FormatTokenGenerator()


def generate_number():
    token = TOKEN_GENERATOR(offset=0, type=FormatTokenizer.NUMBER_TOKEN)
    value = token.value

    if int(value) != value:
        value = float("{:.6f}".format(value))

    return Number(value)


def generate_boolean():

    value = Number(random.randint(0, 1))
    return value


def generate_integer():

    value = Number(int(sys.maxsize * random.random()))
    return value


def generate_identifier():

    token = TOKEN_GENERATOR(offset=0, type=FormatTokenizer.IDENTIFIER_TOKEN)
    return Identifier(token.value)


def generate_string():
    token = TOKEN_GENERATOR(offset=0, type=FormatTokenizer.STRING_TOKEN)
    return String(token.value)


FACTOR_GENERATORS = [generate_number, generate_boolean, generate_integer, generate_identifier, generate_string]


class FunctionalGenerator(object):

    def __init__(self):
        pass

    def generate_factor(self):
        p = random.randint(0, len(FACTOR_GENERATORS) - 1)
        g = FACTOR_GENERATORS[p]
        return g()

    def __call__(self):

        t = random.randint(1, 15)

        edge = [self.generate_factor()]

        for _ in range(t):

            k = random.randint(0, len(edge) - 1)

            fnal = Functional()
            fnal.name_ = generate_identifier().value

            r = random.randint(1, 5)
            fnal.arguments_ = [self.generate_factor() for _ in range(r)]

            p = random.randint(0, r - 1)

            fnal.arguments_[p] = edge[k]

            edge[k] = fnal
            edge = edge[:k + 1] + [fnal.arguments_[-1]]

        return edge[0]


class TestFunctional(WagtailTestUtils, SimpleTestCase):

    def test_functional_parsing(self):

        generator = FunctionalGenerator()

        for index in range(10000):

            fnal = generator()
            text = fnal.format()

            # print("TestExpression.test_expression_parsing() [{:d}]: ".format(index + 1) + text)

            parsed_fnal, errors = Functional.parse_text(text)

            if parsed_fnal is None:
                errors.insert(0, "Couldn't parse functional: ")

            if errors:
                msg = "\n".join(errors)
                parsed_fnal, _, errors = Functional.parse_text(text)
                self.fail(msg)

            if not (fnal == parsed_fnal):
                _ = fnal == parsed_fnal
                self.assertEqual(fnal, parsed_fnal)
