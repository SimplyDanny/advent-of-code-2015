from common import print_results, readline

def find_basement_position(parentheses):
    floor = 0
    for i, p in enumerate(parentheses, start=1):
        floor += 1 if p == '(' else -1
        if floor == -1:
            return i

#### Main part.

parentheses = readline(__file__)

print_results(
    parentheses.count('(') - parentheses.count(')'),
    find_basement_position(parentheses),
)
