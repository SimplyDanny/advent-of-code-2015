from numpy import prod

from common import print_results, readlines

def get_wrapping_paper(present):
    sides = (
        present[0] * present[1],
        present[0] * present[2],
        present[1] * present[2],
    )
    return 2 * sum(sides) + min(sides)

def get_ribbon(present):
    return 2 * (present[0] + present[1]) + prod(present)

#### Main part.

wrapping_paper = 0
ribbon = 0

for line in readlines(__file__):
    present = sorted(map(int, line.split('x')))
    wrapping_paper += get_wrapping_paper(present)
    ribbon += get_ribbon(present)

print_results(wrapping_paper, ribbon)
