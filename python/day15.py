from collections import deque
from aocd.models import Puzzle
from aoc_util import *
from queue import PriorityQueue


puzzle = Puzzle(year=2021, day=15)

test = '''1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581'''

def part1(data):
    Q = PriorityQueue()
    Q.put((0, (0, 0)))
    seen = set([(0, 0)])
    endpoint = (max(x for x, _ in data.keys()), max(y for _, y in data.keys()))

    while Q:
        risk, pos = Q.get()

        if pos == endpoint:
            return risk

        for npos in neighbors_4(pos, data):
            if npos not in seen:
                Q.put((risk+data[npos], npos))
                seen.add(npos)

    return None

def part2(data):
    return part1(enlarge(data))

def enlarge(data):
    xmax, ymax = (max(x for x, _ in data.keys()), max(y for _, y in data.keys()))
    res =  {k: v for k, v in data.items()}

    for i in range(0, 5):
        for j in range(0, 5):
            if i == 0 and j == 0: continue
            for x in range(xmax+1):
                for y in range(ymax+1):
                    p = (i * (xmax+1) + x, j * (ymax+1) + y)
                    res[p] = (data[(x,y)] + i + j - 1) % 9 + 1 
    return res

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