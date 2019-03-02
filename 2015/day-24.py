
from itertools import combinations

from numpy import prod

from common import print_results, readlines


def solve_problem(packages, number_boxes):
    def find_minimal_quantum_entaglement(packages):
        nonlocal weight, min_num, completed
        sublists = find_shortest_sublist(packages, weight, min_num)
        sublists.sort(key = prod)
        for sl in sublists:
            if not completed:
                packs = [p for p in packages if p not in sl]
                if packs != []:
                    find_minimal_quantum_entaglement(packs)
                else:
                    completed = True
                    return
            else:
                return prod(sublists[sublists.index(sl) - 1])
        return prod(sublists[-1]) if completed else 'Problem not solvable'

    weight = sum(packages) // number_boxes
    min_num = weight // packages[0] + 1
    completed = False
    return find_minimal_quantum_entaglement(packages)

def find_shortest_sublist(packs, weight, min_num):
    while True:
        sublist = [
            s
            for s in combinations(packs, min_num)
            if sum(s) == weight
        ]
        if sublist == []:
            min_num += 1
        else:
            return sublist

#### Main part.

packages = sorted((int(line) for line in readlines(__file__)), reverse=True)

print_results(solve_problem(packages, 3), solve_problem(packages, 4))
