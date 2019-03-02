import re
from itertools import permutations

from common import print_results, readlines


LIST_ARRANGEMENT = re.compile(r'(\w+) would (\w+) (\d+) h.*t to (\w+)\.')

def choose_best(graph, possibilities, number):
    happiness = 0
    for pos in possibilities:
        actual_happiness = 0
        for i in range(number - 1):
            actual_happiness += graph[pos[i], pos[i+1]]
            actual_happiness += graph[pos[i+1], pos[i]]
        actual_happiness += graph[pos[0], pos[-1]]
        actual_happiness += graph[pos[-1], pos[0]]
        happiness = max(happiness, actual_happiness)
    return happiness

#### Main part.

graph = {}
persons = set()
for line in readlines(__file__):
    m = LIST_ARRANGEMENT.match(line)
    if m.group(2) == 'gain':
        graph[m.group(1), m.group(4)] = int(m.group(3))
    else:
        graph[m.group(1), m.group(4)] = -int(m.group(3))
    persons.add(m.group(1))
    persons.add(m.group(4))

# Part One
happiness = choose_best(graph, permutations(persons), len(persons))

# Part Two
graph.update({('me', p): 0 for p in persons})
graph.update({(p, 'me'): 0 for p in persons})
persons.add('me')
happiness_with_me = choose_best(graph, permutations(persons), len(persons))

print_results(happiness, happiness_with_me)
