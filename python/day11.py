from aocd.models import Puzzle
from numpy import true_divide
from aoc_util import *

puzzle = Puzzle(year=2021, day=11)

test = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''

def part1(data):
    n_flashed = 0
    for step in range(1, 101):
        for x in range(10):
            for y in range(10):
                data[(x,y)] += 1
        flashed = set()
        done = False
        while not done:
            done = True
            for p, n in data.items():
                if p not in flashed and n > 9:
                    done = False
                    n_flashed += 1
                    flashed.add(p)
                    for pn in neighbors_8(p, data):
                        data[pn] += 1
        for p in flashed:
            data[p] = 0
    return n_flashed

def part2(data):
    n_flashed = 0
    finished = False
    step = 0
    while not finished:
        step += 1
        for x in range(10):
            for y in range(10):
                data[(x,y)] += 1
        flashed = set()
        done = False
        while not done:
            done = True
            for p, n in data.items():
                if p not in flashed and n > 9:
                    done = False
                    n_flashed += 1
                    flashed.add(p)
                    for pn in neighbors_8(p, data):
                        data[pn] += 1
        for p in flashed:
            data[p] = 0
        if len(flashed) == len(data):
            finished = True
    return step

def data(input: str):
    return mapify_grid(input.split('\n'), int)

#print(part1(data(test)))
#print(part2(data(test)))

ans1 = part1(data(puzzle.input_data))
ans2 = part2(data(puzzle.input_data))

print(f'part 1 = {ans1}')
print(f'part 2 = {ans2}')

#puzzle.answer_a = ans1
#puzzle.answer_b = ans2