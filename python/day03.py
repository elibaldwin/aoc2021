from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2021, day=3)

test = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''.split('\n')

def part1(lines):
    grid = np.array([[int(y) for y in list(x)] for x in lines])
    s = ''.join([str(int(sum(grid[:, i]) > (len(grid) / 2))) for i in range(len(grid[0]))])
    print(s)
    gamma = int(s, 2)
    epsilon = ~gamma % (2**12)
    return gamma * epsilon

def part1b(lines):
    nums = [int(x, 2) for x in lines]
    blen = len(lines[0])
    nlines = len(lines)
    sbin = ''.join([str(int(sum((x >> (blen-i)) & 1 for x in nums) > nlines/2)) for i in range(1, blen+1)])
    gamma = int(sbin, 2)
    epsilon = ~gamma % 2**12
    return gamma * epsilon

def part2(lines):
    grid = np.array([[int(y) for y in list(x)] for x in lines])

    reduced1 = grid
    reduced2 = grid

    for i in range(len(grid[0])):
        if (len(reduced1) > 1):
            s = sum(reduced1[:, i])
            inds1 = int(s >= (len(reduced1) - s)) == reduced1[:, i]
            reduced1 = reduced1[inds1]

        if (len(reduced2) > 1):
            s = sum(reduced2[:, i])
            inds2 = int(s >= (len(reduced2) - s)) != reduced2[:, i]
            reduced2 = reduced2[inds2]

    ox = int(''.join(str(x) for x in reduced1[0]), 2)
    co2 = int(''.join(str(x) for x in reduced2[0]), 2)

    return ox * co2

def data(puzzle: Puzzle):
    return puzzle.input_data.split('\n')

ans1 = part1b(data(puzzle))
ans2 = part2(data(puzzle))

print(f'part 1 = {ans1}')
print(f'part 2 = {ans2}')

#puzzle.answer_a = ans1
#puzzle.answer_b = ans2