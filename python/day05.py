from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2021, day=5)

test = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''

def part1(data):
    grid = np.zeros((1000, 1000), dtype=np.int32)
    for (x1, y1), (x2, y2) in data:
        if x1 == x2:
            if y1 <= y2:
                grid[x1, y1:y2+1] += 1
            else:
                grid[x1, y2:y1+1] += 1
        elif y1 == y2:
            if x1 <= x2:
                grid[x1:x2+1, y1] += 1
            else:
                grid[x2:x1+1, y1] += 1
    return np.sum(grid >= 2)

def part2(data):
    grid = np.zeros((1000, 1000), dtype=np.int32)
    for (x1, y1), (x2, y2) in data:
        if x1 == x2:
            if y1 <= y2:
                grid[x1, y1:y2+1] += 1
            else:
                grid[x1, y2:y1+1] += 1
        elif y1 == y2:
            if x1 <= x2:
                grid[x1:x2+1, y1] += 1
            else:
                grid[x2:x1+1, y1] += 1
        else:
            if x1 <= x2:
                for i in range(0, x2-x1+1):
                    if (y1 < y2):
                        grid[x1+i, y1+i] += 1
                    else:
                        grid[x1+i, y1-i] += 1
            else:
                for i in range(0, x1-x2+1):
                    if (y1 < y2):
                        grid[x1-i, y1+i] += 1
                    else:
                        grid[x1-i, y1-i] += 1
    return np.sum(grid >= 2)

def data(s: str):
    lines = s.split('\n')
    pairs = [x.split(' -> ') for x in lines]
    segments = [((int(y) for y in p.split(',')) for p in x) for x in pairs]
    return segments

print(part2(data(test)))

ans1 = part1(data(puzzle.input_data))
ans2 = part2(data(puzzle.input_data))

print(f'part 1 = {ans1}')
print(f'part 2 = {ans2}')

#puzzle.answer_a = ans1
#puzzle.answer_b = ans2