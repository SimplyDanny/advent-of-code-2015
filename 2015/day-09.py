import re
from itertools import permutations

from common import print_results, readlines


graph = {}              # Dictionary that stores the cost of a path
places = set()          # Set that stores all places
minimum = float('inf')  # Value that stores the current minimum distance
maximum = 0             # Value that stores the current maximum distance

# Fill the dictionary 'graph' with the given data and collect all places.
for line in readlines(__file__):
    m = re.match(r'(\w+) to (\w+) = (\d+)', line)
    graph[m.group(1), m.group(2)] = int(m.group(3))
    graph[m.group(2), m.group(1)] = int(m.group(3))
    places.add(m.group(1))
    places.add(m.group(2))

# Iterate over all possible routes.
for pos in permutations(places):
    distance = sum(graph[p, q] for p, q in zip(pos, pos[1:]))
    minimum = min(distance, minimum)
    maximum = max(distance, maximum)

print_results(minimum, maximum)
