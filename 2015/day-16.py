import re

from common import print_results, readlines


INPUT_ARRANGEMENT = re.compile(
    r'^Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)$'
)

TICKER_TAPE = {
    ('children',    3),
    ('cats',        7),
    ('samoyeds',    2),
    ('pomeranians', 3),
    ('akitas',      0),
    ('vizslas',     0),
    ('goldfish',    5),
    ('trees',       3),
    ('cars',        2),
    ('perfumes',    1)
}

class TickerTape:
    def __init__(self, ticker_tape):
        self.ticker_tape_set = ticker_tape
        self.ticker_tape_dict = dict(ticker_tape)

    def add_things_greater_than(self, thing, border):
        value_of_thing = self.ticker_tape_dict[thing]
        for i in range(value_of_thing + 1, border + 1):
            self.ticker_tape_set.add((thing, i))
        self.ticker_tape_set.discard((thing, value_of_thing))

    def add_things_less_than(self, thing):
        value_of_thing = self.ticker_tape_dict[thing]
        for i in range(value_of_thing):
            self.ticker_tape_set.add((thing, i))
        self.ticker_tape_set.discard((thing, value_of_thing))

    def is_subset_of_tape(self, sue):
        return sue <= self.ticker_tape_set

def get_real_sue():
    return sues.index([sue for sue in sues if tt.is_subset_of_tape(sue)][0]) + 1

#### Main part.

sues = []
for line in readlines(__file__):
    m = INPUT_ARRANGEMENT.match(line)
    sues.append({
        (m.group(2), int(m.group(3))),
        (m.group(4), int(m.group(5))),
        (m.group(6), int(m.group(7)))
    })

tt = TickerTape(TICKER_TAPE)

# Part One
sue_1 = get_real_sue()

# Part Two
max_value = max(max(thing[1] for thing in sue) for sue in sues)
tt.add_things_greater_than('cats', max_value)
tt.add_things_greater_than('trees', max_value)
tt.add_things_less_than('pomeranians')
tt.add_things_less_than('goldfish')

sue_2 = get_real_sue()

print_results(sue_1, sue_2)
