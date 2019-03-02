
import re

from common import print_results, readlines


INPUT_ARRANGEMENT = re.compile(r'(\w+) ([ab]|[+-]\d+)(?:, ([+-]\d+))?')

def run_program(a):
    b = 0
    position = 0
    def update_register(instruction):
        nonlocal a, b, position
        x = a if instruction[1] == 'a' else b
        if instruction[0] == 'hlf':
            x /= 2
            position += instruction[2]
        elif instruction[0] == 'tpl':
            x *= 3
            position += instruction[2]
        elif instruction[0] == 'inc':
            x += 1
            position += instruction[2]
        elif instruction[0] == 'jmp':
            position += instruction[2]
        elif instruction[0] == 'jie':
            position += instruction[2] if x % 2 == 0 else 1
        elif instruction[0] == 'jio':
            position += instruction[2] if x == 1 else 1
        return (x, b) if instruction[1] == 'a' else (a, x)

    while True:
        try:
            a, b = update_register(instructions[position])
        except:
            return b

#### Main part.

instructions = []

for line in readlines(__file__):
    m = INPUT_ARRANGEMENT.match(line)
    if m.group(1) == 'jio' or m.group(1) == 'jie':
        instructions.append((m.group(1), m.group(2), int(m.group(3))))
    elif m.group(1) == 'jmp':
        instructions.append((m.group(1), '', int(m.group(2))))
    else:
        instructions.append((m.group(1), m.group(2), 1))

print_results(run_program(0), run_program(1))
