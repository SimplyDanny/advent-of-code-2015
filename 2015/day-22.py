
import re

from common import print_results, readlines


PLAYER_LIVE = 50
PLAYER_MANA = 500

INPUT_REGEX = re.compile(r'^.+: (\d+)$')

# Create class for both the player and the boss.
class Player:
    def __init__(self, life, damage, armor, mana):
        self.life = life
        self.damage = damage
        self.armor = armor
        self.mana = mana

    def attack(self, player):
        player.life -= self.damage - player.armor \
            if self.damage > player.armor \
            else 1
        return player.alive()

    def alive(self):
        return self.life > 0

# Create a 'Spell' class with a 'conjure' method that executes the effects of a
# spell relevant for the player and the boss.
class Spell:
    def __init__(self, name, cost, damage, life, armor, mana, turns):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.life = life
        self.armor = armor
        self.mana = mana
        self.turns = turns

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def conjure(self, player, boss):
        boss.life -= self.damage
        player.life += self.life
        player.armor += self.armor
        player.mana += self.mana
        return boss.alive()

# Create a 'Game' class which describes a whole game with players and a sequence
# of spells. The 'mean' parameter is necessary for 'Part Two'.
class Game:
    def __init__(self, boss, actual_spells, mean=False):
        self.boss = boss
        self.actual_spells = actual_spells
        self.player = Player(PLAYER_LIVE, 0, 0, PLAYER_MANA)
        self.active_spells = {}
        self.mana_spent = 0
        self.mean = mean

    def execute_active_spells(self):
        for spell in self.active_spells:
            spell.conjure(self.player, self.boss)
            self.active_spells[spell] -= 1
        self.active_spells = {spell : turns
            for spell, turns in self.active_spells.items()
            if turns > 0
        }
        return not self.boss.alive()

    def perform_magic(self, spell):
        self.player.mana -= spell.cost
        if self.player.mana < 0:
            return 2
        self.mana_spent += spell.cost
        if spell.turns > 0:
            self.active_spells[spell] = spell.turns
        else:
            if not spell.conjure(self.player, self.boss):
                return 1
        return 0

    # Play the game and return the outcome of the last round.
    def play(self):
        for spell in self.actual_spells[0:-1]:
            self.execute_active_spells()
            self.player.life -= 1 if self.mean else 0
            self.perform_magic(spell)
            self.player.armor = 0
            self.execute_active_spells()
            self.boss.attack(self.player)
        return self.play_last_round()

    # The last round of the game is special. In each step we have to check ...
    #       ... if 'the boss is dead' (then return 1).
    #       ... if 'the player has not enough mana' (then return 2).
    #       ... if 'the player is dead' (then return 3).
    # Is there no end of the game, i. e. nothing of the above is true, 0 is
    # returned.
    def play_last_round(self):
        r = self.execute_active_spells()
        if r:
            return r
        if self.mean:
            self.player.life -= 1
            if not self.player.alive():
                return 3
        r = self.perform_magic(self.actual_spells[-1])
        if r:
            return r
        self.player.armor = 0
        r = self.execute_active_spells()
        if r:
            return r
        r = self.boss.attack(self.player)
        if not r:
            return 3
        return 0

# Define a function that returns 'False' if the arrangement of spells in 'tup'
# is going to be not sucessfull or not allowed.
def is_possible_spell_tuple(tup, minimum):
    # A spell at a specific position is not allowed if there is the same spell
    # before it that is still active. One wrong spell makes the whole tuple of
    # spells unpossible.
    spell = tup[-1]
    l = len(tup)
    if l > 1 and 3 <= spell.turns <= 4 and tup[-2] == spell:
        return False
    elif 5 <= spell.turns <= 6 and (
        (l > 1 and tup[-2] == spell) or
        (l > 2 and tup[-3] == spell)
    ):
        return False
    # Now check whether the amount of necessary mana exceeds the maximal
    # available amount of mana or whether the mana spent for all spells is
    # greater than the actual minimum.
    mana_for_spells = sum([spell.cost for spell in tup])
    mana_from_spells = sum([spell.mana * spell.turns for spell in tup])
    if mana_for_spells > PLAYER_MANA + mana_from_spells or \
       mana_for_spells > minimum:
        return False
    # Is the tuple fine and possible the function returns 'True'.
    return True

def yield_spell_tuple(boss_life):
    # Add possible spells to list.
    spells = [
        Spell('Magic Missile',  53,  4, 0, 0, 0,   0),
        Spell('Drain',          73,  2, 2, 0, 0,   0),
        Spell('Shield',         113, 0, 0, 7, 0,   6),
        Spell('Poison',         173, 3, 0, 0, 0,   6),
        Spell('Recharge',       229, 0, 0, 0, 101, 5)
    ]

    minimum = float('inf')
    nice_tuple = [[]]
    for nt in nice_tuple:
        for spell in spells:
            possible_tuple = nt + [spell]
            if is_possible_spell_tuple(possible_tuple, minimum):
                nice, minimum = yield possible_tuple
            else:
                continue
            if nice:
                nice_tuple.append(possible_tuple)

def play_game(boss_life, boss_damage, mean=False):
    minimum = float('inf')
    generated_spell = yield_spell_tuple(boss_life)
    tup = generated_spell.send(None)
    while True:
        game = Game(
            Player(boss_life, boss_damage, 0, 0),
            tup,
            mean
        )
        result = game.play()
        minimum = min(minimum, game.mana_spent) if result == 1 else minimum
        try:
            tup = generated_spell.send((not result, minimum))
        except:
            return minimum

#### Main part.

# Read boss-data from file.
lines = readlines(__file__)
boss_life = int(INPUT_REGEX.match(lines[0]).group(1))
boss_damage = int(INPUT_REGEX.match(lines[1]).group(1))

print_results(
    play_game(boss_life, boss_damage),
    play_game(boss_life, boss_damage, True)
)
