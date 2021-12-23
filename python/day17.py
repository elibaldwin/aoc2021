from aocd.models import Puzzle
from aoc_util import *
from parse import parse
import numpy as np
import functools

puzzle = Puzzle(year=2021, day=17)

test = '''target area: x=20..30, y=-10..-5'''

@functools.cache
def summ(n):
    return n + summ(n-1) if n else 0

def stepy(p):
    y, vy = p
    return (y-vy, )

def part1(data):
    (tx1, ty1), (tx2, ty2) = data
    return summ(abs(ty1)-1)

def check_valid(v, bounds):
    vx, vy = v
    (tx1, ty1), (tx2, ty2) = bounds
    x, y = vx, vy
    while x <= tx2 and y >= ty1:
        if vx > 0:
            vx -= 1
        vy -= 1
        if x >= tx1 and y <= ty2:
            return True
        x += vx
        y += vy
    return False

def part2(data):
    (tx1, ty1), (tx2, ty2) = data
    minvx = min([x for x in range(tx2) if tx1 <= summ(x) <= tx2])
    maxvx = tx2
    minvy = ty1
    maxvy = abs(ty1)-1
    valid = []
    for x in range(minvx, maxvx+1):
        for y in range(minvy, maxvy+1):
            if check_valid((x,y), data):
                valid.append((x,y))
    return len(valid)

def data(input: str):
    r = parse("target area: x={x1:d}..{x2:d}, y={y1:d}..{y2:d}", input)
    return ((r['x1'], r['y1']), (r['x2'], r['y2']))

print(part1(data(test)))
print(part2(data(test)))

ans1 = part1(data(puzzle.input_data))
ans2 = part2(data(puzzle.input_data))

print(f'part 1 = {ans1}')
print(f'part 2 = {ans2}')

#puzzle.answer_a = ans1
#puzzle.answer_b = ans2