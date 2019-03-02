from common import print_results, readlines


class Instruction:
    def __init__(self, command, arg1, arg2=''):
        self.command = command
        self.arg1 = arg1
        self.arg2 = arg2

class Program:
    def __init__(self, instructions, register_c_start=0):
        self.instructions = instructions
        self.position = 0
        self.number_instructions = len(self.instructions)
        self.reg = {'a': 0, 'b': 0, 'c': register_c_start, 'd': 0}
        self.COMMANDS = {
            'cpy': self.__command_cpy,
            'inc': self.__command_inc,
            'dec': self.__command_dec,
            'jnz': self.__command_jnz
        }

    def run(self):
        while True:
            inst = self.instructions[self.position]
            self.COMMANDS[inst.command](inst.arg1, inst.arg2)
            if self.position >= self.number_instructions or self.position < 0:
                break
        return self.reg['a']

    def __command_cpy(self, arg1, arg2):
        self.reg[arg2] = int(arg1) if arg1.isdigit() else self.reg[arg1]
        self.position += 1

    def __command_inc(self, arg1, arg2):
        self.reg[arg1] += 1
        self.position += 1

    def __command_dec(self, arg1, arg2):
        self.reg[arg1] -= 1
        self.position += 1

    def __command_jnz(self, arg1, arg2):
        self.position += int(arg2) if self.__is_not_zero(arg1) else 1

    def __is_not_zero(self, arg):
        return arg.isdigit() and arg != 0 or self.reg[arg] != 0


#### Main Part.

instructions = [Instruction(*line.split()) for line in readlines(__file__)]

print_results(
    Program(instructions, register_c_start=0).run(),
    Program(instructions, register_c_start=1).run()
)
