from django.test import SimpleTestCase, TestCase
from wagtail.tests.utils import WagtailTestUtils

from ..tokenizer import *


class TestFormatTokenizer(WagtailTestUtils, SimpleTestCase):

    def test_tokens(self):

        tokenizer = FormatTokenizer()

        tokens = [(" ", "\t"), ("\r\n", "\n"), ("Abc", "_xyz", "klm"), ("0983", "3.5", ".4"),("\"hello\"", r'"gg\\"'), ("(",), (")",), (",",)]

        for index, test_tokens in enumerate(tokens):

            token_type = index + 1

            for token in test_tokens:
                result = tokenizer.tokenize(token)

                if not result or result[0].type == FormatTokenizer.ERROR_TOKEN or result[0].string != token or result[0].type != token_type:
                    self.fail("Error parsing individual token: " + token)

    def test_random_sequences(self):

        tokenizer = FormatTokenizer()
        generator = FormatTokenGenerator()

        validated_tokens = []

        index = 0
        limit = 10000
        text_length = 0

        while index < limit:

            token = generator(text_length)
            result = tokenizer.tokenize(token.string)

            if not result or result[0].type == FormatTokenizer.ERROR_TOKEN or result[0].string != token.string:
                self.fail("Error parsing synthesized token: " + token.string)

            if (token.type not in generator.delimiters_) and (validated_tokens and (validated_tokens[-1].type not in generator.delimiters_)):
                continue

            if validated_tokens and validated_tokens[-1].type == FormatTokenizer.WHITESPACE_TOKEN and token.type == FormatTokenizer.WHITESPACE_TOKEN:
                continue

            if validated_tokens and validated_tokens[-1].type == FormatTokenizer.LINE_BREAK_TOKEN and token.type == FormatTokenizer.LINE_BREAK_TOKEN:
                continue

            self.assertEqual(token.offset, text_length)

            validated_tokens.append(token)
            text_length = token.offset + len(token.string)
            index += 1

        text = "".join([token.string for token in validated_tokens])
        tokens = tokenizer.tokenize(text)

        index = 0

        while index < limit:

            if index >= len(tokens):
                self.fail("Number of parsed tokens does not match number of expected tokens: {:d} vs {:d}".format(len(tokens), limit))

            validated_token = validated_tokens[index]
            token = tokens[index]

            if validated_token.type != token.type:
                self.assertEqual(validated_token.type, token.type)

            if validated_token.string != token.string:
                self.assertEqual(validated_token.string, token.string)

            self.assertEqual(validated_token.offset, token.offset)

            index += 1
