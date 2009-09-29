from instructions.math import *

class Statement(object):
    def __init__(self, instruction, arguments, rung):
        self.instruction = instruction.strip()
        self.arguments = [arg.strip() for arg in arguments]
        self.rung = rung
    def __str__(self):
        return "%s %s" % (self.instruction, self.arguments)
    def __repr__(self):
        return self.__str__()

class Program(object):
    def __init__(self, statements):
        self.statements = statements

    def rung(self, n):
        return [s for s in self.statements if s.rung == n]

class Parser(object):
    def parse(self,file):
        lines = file.readlines()
        statements = []
        rung = 0
        for line in lines:
            start = line[0]
            if "Rung" in line:
                rung += 1
            elif start == '#' or start == '/':
                #comment
                pass
            elif start == '\r':
                #empty 
                pass
            elif start == '"':
                #string literal
                pass
            else:
                arr = line.split(' ')
                instruction = arr[0]
                arguments = arr[1:]
                statements.append(Statement(instruction, arguments, rung))
        return Program(statements)


if __name__ == '__main__':
    parser = Parser()
    f = open("/Users/nathan/Desktop/test.txt", "r")
    program = parser.parse(f)
    for stmt in program.rung(1):
        print stmt
    f.close()

