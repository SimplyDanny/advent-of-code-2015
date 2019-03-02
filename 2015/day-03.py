from common import print_results, readline

class Runner:
    STR2VEC = {
        '^': ( 0,  1),
        'v': ( 0, -1),
        '<': (-1,  0),
        '>': ( 1,  0),
    }

    def __init__(self):
        self.x = 0
        self.y = 0
        self.visited_locations = {(0, 0)}

    def update_location(self, direction):
        dx, dy = self.STR2VEC[direction]
        self.x += dx
        self.y += dy
        self.visited_locations.add((self.x, self.y))

#### Main part.

directions = readline(__file__)

# Part One
santa_only = Runner()
for d in directions:
    santa_only.update_location(d)

# Part Two
santa = Runner()
robo_santa = Runner()
for d, e in zip(directions[0::2], directions[1::2]):
    santa.update_location(d)
    robo_santa.update_location(e)

print_results(
    len(santa_only.visited_locations),
    len(santa.visited_locations | robo_santa.visited_locations)
)
