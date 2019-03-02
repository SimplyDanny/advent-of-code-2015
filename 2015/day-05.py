import re

from common import print_results, readlines


class RulesPartOne:
    # A nice string ...
    # ... contains at least three vowels.
    rule_1 = re.compile(r'[aeiou].*[aeiou].*[aeiou]')
    # ... contains at least one letter that appears twice in a row.
    rule_2 = re.compile(r'(\w)\1')
    # ... does not contain the strings 'ab', 'cd', 'pq', or 'xy'.
    rule_3 = re.compile(r'(ab|cd|pq|xy)')

    @staticmethod
    def is_nice(string):
        return RulesPartOne.rule_1.search(string) and     \
               RulesPartOne.rule_2.search(string) and not \
               RulesPartOne.rule_3.search(string)

class RulesPartTwo:
    # A nice string ...
    # ... contains a pair of any two letters that appears at least twice in the
    # string without overlapping.
    rule_1 = re.compile(r'(\w\w).*\1')
    # ... contains at least one letter which repeats with exactly one letter
    # between them.
    rule_2 = re.compile(r'(\w)\w\1')

    @staticmethod
    def is_nice(string):
        return RulesPartTwo.rule_1.search(string) and \
               RulesPartTwo.rule_2.search(string)

def count_nice_strings(rules, strings):
    return sum(1 for string in strings if rules.is_nice(string))

#### Main part.

lines = readlines(__file__)

print_results(
    count_nice_strings(RulesPartOne, lines),
    count_nice_strings(RulesPartTwo, lines)
)
