import re

from common import print_results, readlines


SECONDS = 2503

class Reindeer:
    INPUT_ARRANGEMENT = re.compile(r'.+ (\d+) .+ (\d+) .+ (\d+) .+')

    def __init__(self, line):
        (self.km, self.sprint_time, self.rest_time) = map(
            int, self.INPUT_ARRANGEMENT.match(line).groups()
        )
        self.traveled_distance = 0
        self.points = 0

    def do_time_step(self, i):
        i %= self.sprint_time + self.rest_time
        self.traveled_distance += self.km if 0 < i <= self.sprint_time else 0
        return self.traveled_distance

    def winner(self):
        self.points += 1

#### Main part.

reindeers = [Reindeer(line) for line in readlines(__file__)]

# Part Two
for i in range(1, SECONDS + 1):
    distance = max(r.do_time_step(i) for r in reindeers)
    for r in reindeers:
        if r.traveled_distance == distance:
            r.winner()
max_points = max(r.points for r in reindeers)

# Part One
max_distance = max(r.traveled_distance for r in reindeers)

print_results(max_distance, max_points)
