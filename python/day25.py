from aocd.models import Puzzle
from aoc_util import *

puzzle = Puzzle(year=2021, day=25)

test = '''v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>'''

def part1(data):
    minx, maxx, miny, maxy = point_bounds(data)
    xl = maxx + 1
    yl = maxy + 1
    moved = True
    s = 0
    while moved:
        s += 1
        moved = False
        nextg = dict()
        for (x,y), c in data.items():
            if c == '>':
                nextp = ((x+1)%xl,y)
                if data[nextp] == '.':
                    moved = True
                    nextg[nextp] = '>'
                    nextg[(x,y)] = '.'
                else:
                    nextg[(x,y)] = '>'
            else:
                if (x,y) not in nextg:
                    nextg[(x,y)] = c
        data = nextg
        nextg = dict()
        for (x,y), c in data.items():
            if c == 'v':
                nextp = (x, (y+1)%yl)
                if data[nextp] == '.':
                    moved = True
                    nextg[nextp] = 'v'
                    nextg[(x,y)] = '.'
                else:
                    nextg[(x,y)] = 'v'
            else:
                if (x,y) not in nextg:
                    nextg[(x,y)] = c
        data = nextg
    return s

def data(input: str):
    return mapify_grid(input.split('\n'))

#print(part1(data(test)))

ans1 = part1(data(puzzle.input_data))

print(f'part 1 = {ans1}')

#puzzle.answer_a = ans1
