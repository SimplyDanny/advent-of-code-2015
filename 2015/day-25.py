import re

from common import print_results, readline


ROW_COLUMN_REGEX = re.compile(r'Enter the code at row (\d+), column (\d+)\.')

ROW, COLUMN = map(int, ROW_COLUMN_REGEX.search(readline(__file__)).groups())

A_0 = 20151125
FACTOR = 252533
DIVISOR = 33554393

# First, calculate how many steps are necessary.
b = ROW + COLUMN - 2
number_steps = b * (b + 1) // 2 + b + 2 - ROW

def do_step(a_n):
    while True:
        yield a_n
        a_n = FACTOR * a_n % DIVISOR

#### Main part.

sequence = do_step(A_0)
for _ in range(number_steps - 1):
    sequence.__next__()

print_results(sequence.__next__(), 'Merry Christmas!')
