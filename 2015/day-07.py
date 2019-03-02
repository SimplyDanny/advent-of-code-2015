import re

from common import print_results, readlines


class Wire:
    INSTRUCTION = re.compile(r'^(.*) -> ([a-z]+)$')
    NOT = re.compile(r'^NOT ([a-z]+)$')
    BINARY = re.compile(r'^([0-9a-z]+) (AND|OR|LSHIFT|RSHIFT) ([0-9a-z]+)$')
    CONSTANT = re.compile(r'^([0-9a-z]+)$')

    def __init__(self, expression):
        self.signal = None
        self.left_wire = ''
        self.right_wire = ''

        if expression.isdigit():
            self.signal = int(self.CONSTANT.match(expression).group(1))
            self.gate = ''
        elif self.CONSTANT.match(expression):
            self.left_wire = self.CONSTANT.match(expression).group(1)
            self.gate = 'CONST'
        elif self.NOT.match(expression):
            self.right_wire = self.NOT.match(expression).group(1)
            self.gate = 'NOT'
        elif self.BINARY.match(expression):
            (self.left_wire,
             self.gate,
             self.right_wire,
            ) = self.BINARY.match(expression).groups()

    @classmethod
    def createcommon_wire(self, instruction):
        expression, identifier = self.INSTRUCTION.match(instruction).groups()
        return identifier, self(expression)

    @classmethod
    def create_constant_wire(self, constant):
        return {constant: self(constant)}

class Circuit:
    wires = {}

    def add_wire(self, identifier, wire):
        self.wires.update({identifier: wire})
        if wire.left_wire.isdigit():
            self.wires.update(Wire.create_constant_wire(wire.left_wire))
        if wire.right_wire.isdigit():
            self.wires.update(Wire.create_constant_wire(wire.right_wire))

    def __getitem__(self, identifier):
        wire = self.wires[identifier]
        if wire.signal is None:
            wire.signal = {
                'CONST': lambda wire:
                    self[wire.left_wire],
                'NOT': lambda wire:
                    ~self[wire.right_wire],
                'AND': lambda wire:
                    self[wire.left_wire] & self[wire.right_wire],
                'OR': lambda wire:
                    self[wire.left_wire] | self[wire.right_wire],
                'LSHIFT': lambda wire:
                    self[wire.left_wire] << self[wire.right_wire],
                'RSHIFT': lambda wire:
                    self[wire.left_wire] >> self[wire.right_wire],
            }[wire.gate](wire)
        return wire.signal

    def reset(self):
        for wire in self.wires.values():
            if wire.gate:
                wire.signal = None

#### Main part.

circuit = Circuit()
for line in readlines(__file__):
    circuit.add_wire(*Wire.createcommon_wire(line))

# Part One
signal_1 = circuit['a']

# Part Two
circuit.reset()
circuit.wires['b'].signal = signal_1
signal_2 = circuit['a']

print_results(signal_1, signal_2)
