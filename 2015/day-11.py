import re
from string import ascii_lowercase

from common import print_results, readline


# Define input, input length, necessary digits and letters.
INPUT = readline(__file__)
LENGTH = len(INPUT) - 1
DIGITS = list(range(1, 27))
LETTERS = list(ascii_lowercase)

# Define digit-to-letter and letter-to-digit mappings.
DIGIT_TO_LETTER = dict(zip(DIGITS, LETTERS))
LETTER_TO_DIGIT = dict((v, k) for k, v in DIGIT_TO_LETTER.items())

# Define additional password requirements.
STRAIGHTS = [''.join(LETTERS[i:i + 3]) for i in range(0, 24)]
PAIR_OF_PAIRS = re.compile(r'.*(\w)\1.*(\w)\2.*')

# Increment the password string at given position 'pos'. Note that there may be
# a borrow.
def increment(inp, pos=LENGTH):
    number = LETTER_TO_DIGIT[inp[pos]]
    number += 1
    if number == 27 and pos != 0:
        inp[pos] = 'a'
        increment(inp, pos - 1)
    else:
        inp[pos] = DIGIT_TO_LETTER[number]
    return ''.join(inp)

# Search for the next possible password given the old one 'inp'.
def change_password(inp):
    while True:
        inp = increment(list(inp))

        # Passwords may not contain the LETTERS 'i', 'l' or 'o'.
        if 'i' in inp or 'l' in inp or 'o' in inp:
            continue

        # Passwords must include one increasing straight of at least three
        # LETTERS.
        for t in STRAIGHTS:
            if t in inp:
                break
        else:
            continue

        # Passwords must contain at least two different,
        # non-overlapping pairs of LETTERS.
        for pair1, pair2 in PAIR_OF_PAIRS.findall(inp):
            if pair1 != pair2:
                return inp

#### Main part.

password_1 = change_password(INPUT)
password_2 = change_password(increment(list(password_1)))

print_results(password_1, password_2)
