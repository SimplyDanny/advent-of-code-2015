import re
from itertools import product

from numpy import prod

from common import print_results, readlines


NUMBER_PROPERTIES = 4

INPUT_ARRANGEMENT = re.compile(
    r'.* (-?\d),.* (-?\d),.* (-?\d),.* (-?\d),.* (-?\d)$'
)

Properties = []     # List storing the ingredients with their properties
for line in readlines(__file__):
    m = INPUT_ARRANGEMENT.match(line)
    Properties.append(list(map(int, m.groups())))

number_ingredients = len(Properties)

# Create a list of combinations of four numbers that sum up to 100 by
# creating tripels of the numbers 0 to 97 and adding the fourth one as the
# difference of 100 and the sum of the three preceding ones.
possibilities = list(product(range(0,98), repeat=3))
possibilities = [list(pos) for pos in possibilities if sum(pos) <= 100]
for pos in possibilities:
    pos.append(100 - sum(pos))

# Now go through all combinations.
maximum_1 = 0       # Saves the maximum regarding Part One.
maximum_2 = 0       # Saves the maximum regarding Part Two.
for pos in possibilities:
    # Calculate the total value of each property. Make sure that there is no
    # negative entry.
    value_of_properties = [
        max(0, sum(
            Properties[j][i] * pos[j]
            for j in range(number_ingredients)
        ))
        for i in range(NUMBER_PROPERTIES)
    ]
    # Multiply these values together.
    f = prod(value_of_properties)

    # Part One
    maximum_1 = max(maximum_1, f)

    # Part Two
    calories = sum(Properties[j][4] * pos[j] for j in range(number_ingredients))
    if calories == 500:
        maximum_2 = max(maximum_2, f)

print_results(maximum_1, maximum_2)
