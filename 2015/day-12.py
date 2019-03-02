import json
import re

from common import print_results, read


NUMBER_REGEX = re.compile(r'-?\d+')

json_string = read(__file__)

# Part One
count_1 = sum(int(s) for s in NUMBER_REGEX.findall(json_string))

# Part Two
red = lambda x: {} if 'red' in x.values() else x
json_string = json.dumps(json.loads(json_string, object_hook=red))
count_2 = sum(int(s) for s in NUMBER_REGEX.findall(json_string))

print_results(count_1, count_2)
