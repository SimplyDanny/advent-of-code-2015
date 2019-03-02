import re

from common import print_results, readlines


value_1, value_2 = 0, 0

lines = readlines(__file__)

for line in lines:
    characters = len(line)

    # Part One
    temp_line = re.sub(r'\\x[a-f0-9][a-f0-9]', 'z', line)
    temp_line = re.sub(r'\\\\', 'z', temp_line)
    temp_line = re.sub(r'\\"', 'z', temp_line)

    memory = len(temp_line) - 2
    value_1 += characters - memory

    # Part Two
    temp_line = re.sub('^"', 'zzz', line)
    temp_line = re.sub('"$', 'zzz', temp_line)
    temp_line = re.sub(r'\\x[a-f0-9][a-f0-9]', 'zzzzz', temp_line)
    temp_line = re.sub(r'\\"', 'zzzz', temp_line)
    temp_line = re.sub(r'\\\\', 'zzzz', temp_line)

    value_2 += len(temp_line) - characters

print_results(value_1, value_2)
