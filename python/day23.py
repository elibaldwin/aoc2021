from aocd.models import Puzzle
from aoc_util import *
from collections import defaultdict
from queue import PriorityQueue

puzzle = Puzzle(year=2021, day=23)

test = '''#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########'''

floormap = '''#############
#**.*.*.*.**#
###*#*#*#*###
  #*#*#*#*#
  #########'''

floormap2 = '''#############
#**.*.*.*.**#
###*#*#*#*###
  #*#*#*#*#
  #*#*#*#*#
  #*#*#*#*#
  #########'''

D = mapify_grid(floormap.split('\n'))
D2 = mapify_grid(floormap2.split('\n'))

C = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

G = {'A': {(3, 3), (3, 2)}, 'B': {(5, 3), (5, 2)}, 'C': {(7, 3), (7, 2)}, 'D': {(9, 3), (9, 2)}}
G2 = {'A': {(3, 5), (3, 4), (3, 3), (3, 2)}, 
      'B': {(5, 5), (5, 4), (5, 3), (5, 2)}, 
      'C': {(7, 5), (7, 4), (7, 3), (7, 2)}, 
      'D': {(9, 5), (9, 4), (9, 3), (9, 2)}}

H = {(1,1), (2,1), (4,1), (6,1), (8,1), (10, 1), (11, 1)}

def pod_moves(pod: Tuple[str, Tuple[int, int]], podlocs: Dict[str, Set[Tuple[int, int]]]):
    ptype, loc = pod

    if loc in G[ptype] and (loc[1]==3 or (loc[0], 3) in podlocs[ptype]):
        return

    c = C[ptype]
    podpoints = set()
    for l in podlocs.values():
        podpoints.update(l)
    podpoints.remove(loc)

    Q = [(0, loc)]
    seen = set()
    while Q:
        cost, p = Q.pop(0)
        if p != loc and ((p in G[ptype] and (p[1] == 3  or (p[0], 3) in podlocs[ptype])) or (p in H and loc[1]>1)):
            yield cost, loc, p
        
        for np in neighbors_4(p, D):
            if np not in podpoints and np not in seen and D[np] != '#':
                seen.add(np)
                Q.append((cost + c, np))

def pod_moves2(pod: Tuple[str, Tuple[int, int]], podlocs: Dict[str, Set[Tuple[int, int]]]):
    ptype, loc = pod

    if loc in G2[ptype] and (loc[1]==5 or all((loc[0], i) in podlocs[ptype] for i in range(loc[1]+1,6))):
        return

    c = C[ptype]
    podpoints = set()
    for l in podlocs.values():
        podpoints.update(l)
    podpoints.remove(loc)

    Q = [(0, loc)]
    seen = set()
    while Q:
        cost, p = Q.pop(0)
        if p != loc and ((p in G2[ptype] and (p[1] == 5 or all((p[0], i) in podlocs[ptype] for i in range(p[1]+1,6)))) or (loc[1]>1 and p in H)):
            yield cost, loc, p
        
        for np in neighbors_4(p, D2):
            if np not in podpoints and np not in seen and D2[np] != '#':
                seen.add(np)
                Q.append((cost + c, np))

def map_moves(podlocs: Dict[str, Set[Tuple[int, int]]]):
    moves = []
    for t, locs in podlocs.items():
        for loc in locs:
            moves.extend((t, m) for m in pod_moves((t, loc), podlocs))
    return moves

def map_moves2(podlocs: Dict[str, Set[Tuple[int, int]]]):
    moves = []
    for t, locs in podlocs.items():
        for loc in locs:
            moves.extend((t, m) for m in pod_moves2((t, loc), podlocs))
    return moves

def done_podding(podlocs):
    return all(G[c] == podlocs[c] for c in 'ABCD')

def freeze(locs: Dict[str, Set[Tuple[int, int]]]):
    return tuple(tuple(sorted(locs[k])) for k in 'ABCD')

def unfreeze(locs: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int], Tuple[int, int]]):
    return dict({k:set(v) for k,v in zip('ABCD', locs)})

def part1(podlocs: Dict[str, Set[Tuple[int, int]]]):
    
    fznlocs = freeze(podlocs)
    Q = PriorityQueue()
    Q.put((0, fznlocs))
    costs = {fznlocs: 0}

    while not Q.empty():
        moves, podlocs = Q.get(0)
        cost = costs[podlocs]

        for type, (mcost, p1, p2) in map_moves(unfreeze(podlocs)):
            mpodlocs = unfreeze(podlocs)
            mpodlocs[type].remove(p1)
            mpodlocs[type].add(p2)
            fznlocs = freeze(mpodlocs)
            ncost = cost + mcost
            if fznlocs not in costs or ncost < costs[fznlocs]:
                costs[fznlocs] = ncost
                Q.put((moves + 1, fznlocs))
    return costs[freeze(G)]

def part2(podlocs: Dict[str, Set[Tuple[int, int]]]):
    fznlocs = freeze(podlocs)
    Q = PriorityQueue()
    Q.put((0, fznlocs))
    costs = {fznlocs: 0}

    while not Q.empty():
        moves, podlocs = Q.get(0)
        cost = costs[podlocs]

        for type, (mcost, p1, p2) in map_moves2(unfreeze(podlocs)):
            mpodlocs = unfreeze(podlocs)
            mpodlocs[type].remove(p1)
            mpodlocs[type].add(p2)
            fznlocs = freeze(mpodlocs)
            ncost = cost + mcost
            if fznlocs not in costs or ncost < costs[fznlocs]:
                costs[fznlocs] = ncost
                Q.put((moves + 1, fznlocs))
    return costs[freeze(G2)]

def data(input: str):
    lines = input.split('\n')
    podlocs = defaultdict(set)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in 'ABCD':
                podlocs[c].add((x,y))
    return podlocs

def data2(input: str):
    lines = input.split('\n')
    if (len(lines) == 5):
        lines.insert(3, '  #D#B#A#C#')
        lines.insert(3, '  #D#C#B#A#')
    podlocs = defaultdict(set)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in 'ABCD':
                podlocs[c].add((x,y))
    return podlocs

test2 = '''#############
#AA.....B.BD#
###B#C#.#.###
  #D#C#.#.#
  #D#B#.#C#
  #A#D#C#A#
  #########'''

ans1 = part1(data(puzzle.input_data))
ans2 = part2(data2(puzzle.input_data))

print(f'part 1 = {ans1}')
print(f'part 2 = {ans2}')

#puzzle.answer_a = ans1
#puzzle.answer_b = ans2