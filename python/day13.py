from aocd.models import Puzzle
from aoc_util import *

puzzle = Puzzle(year=2021, day=13)

test = '''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5'''

def fold(grid, axis, n):
    newgrid = set()
    if axis == 'x':
        for x,y in grid:
            if x > n:
                newgrid.add((n-(x-n), y))
            else:
                newgrid.add((x,y))
    else:
        for x,y in grid:
            if y > n:
                newgrid.add((x, n-(y-n)))
            else:
                newgrid.add((x,y))
    return newgrid
            
def part1(data):
    grid, folds = data
    axis, n = folds[0]
    folded = fold(grid, axis, n)
    axis, n = folds[1]
    return len(folded)

def part2(data):
    grid, folds = data
    for axis, n in folds:
        grid = fold(grid, axis, n)
    print_pointset(grid)
    return len(data)

def data(input: str):
    grid = set()
    dots, folds = input.split('\n\n')
    for line in dots.split('\n'):
        grid.add(read_point(line))
    folds = [x.split('=') for x in folds.split('\n')]
    folds = [(x[-1], int(y)) for x,y in folds]
    return (grid, folds)

print(part1(data(test)))
    
ans1 = part1(data(puzzle.input_data))
ans2 = part2(data(puzzle.input_data))

print(f'part 1 = {ans1}')
print(f'part 2 = {ans2}')

#puzzle.answer_a = ans1
#puzzle.answer_b = ans2