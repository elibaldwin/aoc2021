from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=7)

def part1(data):
    best = 999999999999999
    for i in range(min(data), max(data)+1):
        s = 0
        for point in data:
            s += abs(i-point)
        best = min(s, best)
    return best 

def part2(data):
    best = 999999999999999
    for i in range(min(data), max(data)+1):
        s = 0
        for point in data:
            s += sum(range(0, abs(i-point)+1))
        best = min(s, best)
    return best 

def data(input: str):
    return [int(x) for x in input.split(',')]

ans1 = part1(data(puzzle.input_data))
ans2 = part2(data(puzzle.input_data))

print(f'part 1 = {ans1}')
print(f'part 2 = {ans2}')

#puzzle.answer_a = ans1
#puzzle.answer_b = ans2