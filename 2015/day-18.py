from common import print_results, readlines


def count_activated_neighbors(x, y, activated_lights):
    return sum(
        (i, j) in activated_lights
        for i in (x - 1, x, x + 1)
        for j in (y - 1, y, y + 1)
        if (i, j) != (x, y)
    )

def do_steps(activated_lights):
    return {
        (x, y)
        for x in range(100)
        for y in range(100)
        if (x, y) in activated_lights
        and 2 <= count_activated_neighbors(x, y, activated_lights) <= 3
        or (x, y) not in activated_lights
        and count_activated_neighbors(x, y, activated_lights) == 3
    }

initial_condition = {
    (x, y)
    for y, line in enumerate(readlines(__file__))
    for x, indicator in enumerate(line)
    if indicator == '#'
}

# Part One
activated_lights_1 = initial_condition
for _ in range(100):
    activated_lights_1 = do_steps(activated_lights_1)

# Part Two
activated_lights_2 = initial_condition
activated_lights_2.update({(0, 0), (0, 99), (99, 0), (99, 99)})
for _ in range(100):
    activated_lights_2 = do_steps(activated_lights_2)
    activated_lights_2.update({(0, 0), (0, 99), (99, 0), (99, 99)})

print_results(len(activated_lights_1), len(activated_lights_2))
