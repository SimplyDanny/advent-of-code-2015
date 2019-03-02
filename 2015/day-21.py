
import re
from itertools import combinations, product

from common import print_results, readlines


INPUT_REGEX = re.compile(r'^.+: (\d+)$')

# Create class for both the player and the boss.
class Player:
    def __init__(self, live, damage, armor):
        self.live = int(live)
        self.damage = int(damage)
        self.armor = int(armor)

    def attack(self, player):
        player.live -= self.damage - player.armor \
            if self.damage > player.armor \
            else 1

    def is_alive(self):
        return self.live > 0

# Items which can be bought.
Shop = {
    'Weapons': {
        'Dagger':       (8,  4, 0),
        'Shortsword':   (10, 5, 0),
        'Warhammer':    (25, 6, 0),
        'Longsword':    (40, 7, 0),
        'Greataxe':     (74, 8, 0)
    },
    'Armor': {
        'Leather':      (13,  0, 1),
        'Chainmail':    (31,  0, 2),
        'Splintmail':   (53,  0, 3),
        'Bandedmail':   (75,  0, 4),
        'Platemail':    (102, 0, 5)
    },
    'Rings': {
        'Damage +1':    (25,  1, 0),
        'Damage +2':    (50,  2, 0),
        'Damage +3':    (100, 3, 0),
        'Defense +1':   (20,  0, 1),
        'Defense +2':   (40,  0, 2),
        'Defense +3':   (80,  0, 3)
    }
}

# Add possible but ridiculous goods to the shop. So it is possible to have no
# armor (buying only underpants), no rings (buying plastic and wooden ring) or
# just one ring (buying either a plastic or wooden ring and one useful ring).
Shop['Armor']['Underpants'] = (0, 0, 0)
Shop['Rings']['Plastic']    = (0, 0, 0)
Shop['Rings']['Wood']       = (0, 0, 0)

# Define a function that adds up a property tripel in 'Shop'.
addTupels = lambda t1, t2: tuple(map(lambda x, y: x + y, t1, t2))

# Now collect all possible combinations of items.
Possibilities = list(product(
    Shop['Weapons'].values(),
    Shop['Armor'].values(),
    [c for c in combinations(Shop['Rings'].values(), 2) if c[0] != c[1]]
))

# Go over to property tripel only.
Possibilities = [
    addTupels(addTupels(pos[0], pos[1]), addTupels(pos[2][0], pos[2][1]))
    for pos in Possibilities
]

#### Main part.

# Create the boss reading the data from the file.
lines = readlines(__file__)
boss_live = INPUT_REGEX.match(lines[0]).group(1)
boss_damage = INPUT_REGEX.match(lines[1]).group(1)
boss_armor = INPUT_REGEX.match(lines[2]).group(1)

minimum = float('inf')
maximum = 0
for pos in Possibilities:
    boss = Player(boss_live, boss_damage, boss_armor)
    player = Player(100, pos[1], pos[2])
    while player.is_alive() and boss.is_alive():
        player.attack(boss)
        boss.attack(player)
    if not boss.is_alive():
        minimum = min(minimum, pos[0])
    if not player.is_alive() and boss.is_alive():
        maximum = max(maximum, pos[0])

print_results(minimum, maximum)
