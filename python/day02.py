from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=2)

def part1(lines):
    x = 0
    y = 0
    for action, n in lines:
        if action == 'forward':
            x += n
        elif action == 'up':
            y -= n
        elif action == 'down':
            y += n
    return x * y

def part2(lines):
    x = 0
    y = 0
    aim = 0
    for action, n in lines:
        if action == 'forward':
            x += n
            y += aim * n
        elif action == 'up':
            aim -= n
        elif action == 'down':
            aim += n
    return x * y

def data(puzzle: Puzzle):
    return [(y[0], int(y[1])) for y in [x.split() for x in puzzle.input_data.split('\n')]]

ans1 = part1(data(puzzle))
ans2 = part2(data(puzzle))

print(f'part 1 = {ans1}')
print(f'part 2 = {ans2}')

#puzzle.answer_a = ans1
#puzzle.answer_b = ans2