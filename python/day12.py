from collections import defaultdict
from typing import Counter
from aocd.models import Puzzle
from aoc_util import *

puzzle = Puzzle(year=2021, day=12)

test = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end'''

def part1(data):

    Q = [('start', tuple())]
    paths = set()

    while Q:
        pos, path = Q.pop()

        for n in data[pos]:
            ppath = tuple(path + tuple([n]))
            if n == 'start' or ppath in paths: continue
            if n == 'end':
                paths.add(ppath)
            elif (n.islower() and n not in path) or (n.isupper()):
                Q.append((n, ppath))
    return len(paths)

def part2(data):
    Q = [('start', tuple(), False)]
    paths = set()

    while Q:
        pos, path, looped = Q.pop()

        for n in data[pos]:
            ppath = tuple(path + tuple([n]))
            
            if n == 'start' or ppath in paths: continue
            if n == 'end':
                paths.add(ppath)
            elif (n.islower() and (not looped or n not in path)):
                nlooped = looped or n in path
                Q.append((n, ppath, nlooped))
            elif (n.isupper()):
                Q.append((n, ppath, looped))
    return len(paths)

def data(input: str):
    paths = defaultdict(list)
    for l in input.split('\n'):
        start, end = l.split('-')
        paths[start].append(end)
        paths[end].append(start)
    return paths

#print(part1(data(test)))
#print(part2(data(test)))

ans1 = part1(data(puzzle.input_data))
ans2 = part2(data(puzzle.input_data))

print(f'part 1 = {ans1}')
print(f'part 2 = {ans2}')

#puzzle.answer_a = ans1
#puzzle.answer_b = ans2