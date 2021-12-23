from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=1)

def part1(lines):
    return sum(int(x) < int(y) for x, y in zip(lines, lines[1:]))

def part2(lines):
    return sum(int(x) < int(y) for x, y in zip(lines, lines[3:]))

ans1 = part1(puzzle.input_data.split('\n'))
ans2 = part2(puzzle.input_data.split('\n'))

print(f'part 1 = {ans1}')
print(f'part 2 = {ans2}')

#puzzle.answer_a = ans1
#puzzle.answer_b = ans2