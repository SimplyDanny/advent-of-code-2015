import re

from common import print_results, readline


sequence = readline(__file__)

DIGIT_GROUP = re.compile(r'((\d)\2*)')

def play_game(times):
    global sequence
    for _ in range(times):
        res = ''
        for group, digit in DIGIT_GROUP.findall(sequence):
            res += '{}{}'.format(len(group), digit)
        sequence = res
    return len(sequence)

print_results(play_game(40), play_game(10))
