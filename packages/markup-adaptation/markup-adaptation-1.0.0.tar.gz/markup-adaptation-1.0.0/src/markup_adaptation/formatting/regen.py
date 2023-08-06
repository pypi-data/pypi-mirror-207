import random

class AtomicGenerator(object):

    def __init__(self, value, min, max):

        self.value_ = value
        self.min_ = min
        self.max_ = max

    def generate(self):

        result = ""
        r = random.randint(self.min_, self.max_ if self.max_ else 10)

        for r in range(r):

            result += self.value_

        return result


class SequenceGenerator(object):

    def __init__(self, sequence, min, max):

        self.sequence_ = sequence
        self.min_ = min
        self.max_ = max

    def generate(self):

        result = ""
        r = random.randint(self.min_, self.max_ if self.max_ else 10)

        for r in range(r):

            for s in self.sequence_:
                result += s.generate()

        return result


class AlphabetGenerator(object):

    def __init__(self, alphabet, min, max):

        self.alphabet_ = alphabet
        self.min_ = min
        self.max_ = max

    def generate(self):

        result = ""
        r = random.randint(self.min_, self.max_ if self.max_ else 10)

        for r in range(r):

            c = random.randint(0, len(self.alphabet_) - 1)
            result += self.alphabet_[c]

        return result


class ChoiceGenerator(object):

    def __init__(self, choices, min, max):

        self.choices_ = choices
        self.min_ = min
        self.max_ = max

    def generate(self):

        result = ""
        r = random.randint(self.min_, self.max_ if self.max_ else 10)

        for r in range(r):

            c = random.randint(0, len(self.choices_) - 1)
            choice = self.choices_[c]

            if isinstance(choice, str):
                result += choice
            else:
                result += choice.generate()

        return result
