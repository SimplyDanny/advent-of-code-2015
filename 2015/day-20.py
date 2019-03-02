from functools import reduce
from math import ceil, sqrt

from common import print_results, readline


INPUT = int(readline(__file__))

def get_factors(n):
    return set(reduce(
        list.__add__, (
            [i, n//i]
            for i in range(1, ceil(sqrt(n)) + 1)
            if n % i == 0
        )
    ))

def get_factors_with_limitation(Factors):
    for factor in Factors:
        Elves[factor] = Elves[factor] + 1 if factor in Elves else 1
    return {factor for factor in Factors if Elves[factor] <= 50}

#### Main part.

Elves = {}
house = 0
house_1 = 0
house_2 = 0
while True:
    house += 1
    Factors = get_factors(house)

    # Part One
    if 10 * sum(Factors) >= INPUT and house_1 == 0:
        house_1 = house

    # Part Two
    if 11 * sum(get_factors_with_limitation(Factors)) >= INPUT and house_2 == 0:
        house_2 = house

    if house_1 * house_2 != 0:
        break

print_results(house_1, house_2)
