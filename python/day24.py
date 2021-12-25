from aocd.models import Puzzle
from aoc_util import *

puzzle = Puzzle(year=2021, day=24)

test = '''inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2'''

class ALU:

    def __init__(self, program) -> None:
        self.program = program
        self.reset()
    
    def reset(self):
        self.in_queue = []
        self.vars = {'w':0, 'x':0, 'y':0, 'z':0}
    
    def resolve(self, c: str):
        try:
            r = int(c)
            return r
        except ValueError:
            return self.vars[c]
    
    def run(self, model_num: int):
        self.reset()
        self.in_queue.extend(str(model_num))
        for line in self.program:
            eval('self.'+line[0])(line[1:])
        return self.vars['z']
    
    def inp(self, args: List[str]):
        self.vars[args[0]] = int(self.in_queue.pop(0))
    
    def add(self, args: List[str]):
        self.vars[args[0]] += self.resolve(args[1])
    
    def mul(self, args: List[str]):
        self.vars[args[0]] *= self.resolve(args[1])
    
    def div(self, args: List[str]):
        self.vars[args[0]] //= self.resolve(args[1])
    
    def mod(self, args: List[str]):
        self.vars[args[0]] %= self.resolve(args[1])
    
    def eql(self, args: List[str]):
        self.vars[args[0]] = int(self.vars[args[0]] == self.resolve(args[1]))

# x = z
# x %= 26
# x += 14
# if x != w:
#    y = 26
#    z *= y
#    y = w + 12
#    z += y
def runprog(s):
    w = x = y = z = 0
    q = list(s)

    # 1 goes with 14
    w = int(q.pop(0))
    x = 14
    z = w + 12

    # 2 goes with 13
    w = int(q.pop(0))
    z *= 26
    z += w + 6

    # 3 goes with 12
    w = int(q.pop(0))
    z *= 26
    z += w + 4

    # 4 goes with 7
    w = int(q.pop(0))
    z *= 26
    z += w + 5

    # 5 goes with 6
    w = int(q.pop(0))
    z *= 26
    z += w

    # 6
    w = int(q.pop(0))
    x = z % 26 - 7
    z //= 26
    if x != w:
        z *= 26
        z += w + 4
    
    # 7
    w = int(q.pop(0))
    x = z % 26 - 13
    z //= 26
    if x != w:
        z *= 26
        z += w + 15
    
    # 8 goes with 9
    w = int(q.pop(0))
    z *= 26
    z += w + 14

    # 9
    w = int(q.pop(0))
    x = z % 26 - 7
    z //= 26
    if x != w:
        z *= 26
        z += w + 6
    
    # 10 goes with 11
    w = int(q.pop(0))
    z *= 26
    z += w + 14

    # 11
    w = int(q.pop(0))
    x = z % 26 - 9
    z //= 26
    if x != w:
        z *= 26
        z += w + 8
    
    # 12
    w = int(q.pop(0))
    x = z % 26 - 2
    z //= 26
    if x != w:
        z *= 26
        z += w + 5
    
    # 13
    w = int(q.pop(0))
    x = z % 26 - 9
    z //= 26
    if x != w:
        z *= 26
        z += w + 14
    
    # 14
    w = int(q.pop(0))
    x = z % 26 - 14
    z //= 26
    if x != w:
        z *= 26
        z += w + 4

    return z
    
def part1(data):
    alu = ALU(data)
    #    12345678901234
    s = '99799212949967'
    print(alu.run(s))
    print(runprog(s))
    return len(data)

def part2(data):
    alu = ALU(data)
    #    12345678901234
    s = '34198111816311'
    print(alu.run(s))
    print(runprog(s))
    return len(data)

def data(input: str):
    return [l.split(' ') for l in input.split('\n')]

ans1 = part1(data(puzzle.input_data))
ans2 = part2(data(puzzle.input_data))

print(f'part 1 = {ans1}')
print(f'part 2 = {ans2}')

#puzzle.answer_a = ans1
#puzzle.answer_b = ans2





