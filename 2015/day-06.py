import re

import numpy as np

from common import print_results, readlines


class Instruction:
    arrangement = re.compile(
        r'^(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)$'
    )

    def __init__(self, x0, y0, x1, y1, action):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.action = action

    @classmethod
    def from_line(cls, line):
        m = cls.arrangement.match(line)
        return cls(
            int(m.group(2)),
            int(m.group(3)),
            int(m.group(4)) + 1,
            int(m.group(5)) + 1,
            cls.instruction_to_function[m.group(1)]
        )

class InstructionPartOne(Instruction):
    instruction_to_function = {
        'turn on':  np.vectorize(lambda _: 1),
        'turn off': np.vectorize(lambda _: 0),
        'toggle':   np.vectorize(lambda x: not x),
    }

class InstructionPartTwo(Instruction):
    instruction_to_function = {
        'turn on':  np.vectorize(lambda x: x + 1),
        'turn off': np.vectorize(lambda x: max(0, x - 1)),
        'toggle':   np.vectorize(lambda x: x + 2),
    }

class LightField:
    def __init__(self):
        self.lights = np.zeros((1000, 1000), dtype=int)

    def act_on_lights(self, instruction):
        x_slice = slice(instruction.x0, instruction.x1)
        y_slice = slice(instruction.y0, instruction.y1)
        self.lights[x_slice, y_slice] = \
            instruction.action(self.lights[x_slice, y_slice])

    def get_brightness(self):
        return sum(sum(self.lights))

#### Main part.

instructions = readlines(__file__)

field_1 = LightField()
field_2 = LightField()

for instruction in instructions:
    field_1.act_on_lights(InstructionPartOne.from_line(instruction))
    field_2.act_on_lights(InstructionPartTwo.from_line(instruction))

print_results(
    field_1.get_brightness(),
    field_2.get_brightness()
)
