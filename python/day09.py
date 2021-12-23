from aocd.models import Puzzle
from numpy.core.fromnumeric import prod

puzzle = Puzzle(year=2021, day=9)

moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
test = '''2199943210
3987894921
9856789892
8767896789
9899965678'''

def part1(data):
    s = 0
    for x, line in enumerate(data):
        for y, d in enumerate(line):
            ismin = True
            for dx, dy in moves:
                _x = x + dx
                _y = y + dy
                if (0 <= _x < len(data)) and (0 <= _y < len(line)):
                    if d >= data[_x][_y]:
                        ismin = False
                        break
            if ismin:
                s += 1 + d
    return s

def flood(data, point):
    Q = [point]
    s = 1
    seen = set(Q)

    while Q:
        xp, yp = Q.pop(0)
        d = data[xp][yp]

        for dx, dy in moves:
            x = xp + dx
            y = yp + dy
            if (x,y) not in seen and (0 <= x < len(data)) and (0 <= y < len(data[0])):
                if d < data[x][y] and data[x][y] < 9:
                    seen.add((x,y))
                    Q.append((x,y))
                    s += 1

    return s


def part2(data):
    lowpoints = []
    for x, line in enumerate(data):
        for y, d in enumerate(line):
            ismin = True
            for dx, dy in moves:
                _x = x + dx
                _y = y + dy
                if (0 <= _x < len(data)) and (0 <= _y < len(line)):
                    if d >= data[_x][_y]:
                        ismin = False
                        break
            if ismin:
                lowpoints.append((x, y))
    
    basin_sizes = sorted([flood(data, p) for p in lowpoints])
    basin_sizes.reverse()
    return prod(basin_sizes[:3])


def data(input: str):
    return [[int(y) for y in x] for x in input.split('\n')]

print(part1(data(test)))
print(part2(data(test)))

ans1 = part1(data(puzzle.input_data))
ans2 = part2(data(puzzle.input_data))

print(f'part 1 = {ans1}')
print(f'part 2 = {ans2}')

#puzzle.answer_a = ans1
#puzzle.answer_b = ans2