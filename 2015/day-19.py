import re

from common import print_results, readlines


REPLACEMENT_REGEX = re.compile(r'(\w+) => (\w+)')

replace = lambda s, i, rep: s[:i] + rep[1] + s[i + len(rep[0]):]

#### Main part.

lines = readlines(__file__)
replacements = [REPLACEMENT_REGEX.match(line).groups() for line in lines[:-2]]
medicine = lines[-1]
LENGTH = len(medicine)

# Part One
Molecules = set()
for rep in replacements:
     for occ in [n for n in range(LENGTH) if medicine.find(rep[0], n) == n]:
         Molecules.add(replace(medicine, occ, rep))

# Part Two (using a Greedy-like algorithm)
replacements.sort(key=lambda repl: repl[1], reverse=True)
step = 0
while medicine != 'e':
    for repl in replacements:
        if medicine.replace(repl[1], repl[0], 1) == medicine:
            continue
        medicine = medicine.replace(repl[1], repl[0], 1)
        step += 1
        break

print_results(len(Molecules), step)
