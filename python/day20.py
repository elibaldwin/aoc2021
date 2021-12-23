from re import S
from aocd.models import Puzzle
from aoc_util import *
from collections import defaultdict

puzzle = Puzzle(year=2021, day=20)

test = '''..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###'''

def conv(image, x, y):
    s = ''
    for i in range(-1, 2):
        for j in range(-1, 2):
            s += image[(x+j,y+i)]
    return s

def enhance(image: defaultdict, alg):
    minx, maxx, miny, maxy = point_bounds(image)
    prevdefault = image[(minx-1, miny-1)]
    newdefault = alg[int(prevdefault*9, 2)]
    newimage = defaultdict(lambda: newdefault)
    for x in range(minx-1, maxx+2):
        for y in range(miny-1, maxy+2):
            newimage[(x,y)] = alg[int(conv(image, x, y), 2)]
    return newimage

def part1(data):
    alg, image = data
    convert = {'0':' ', '1':'#'}
    for i in range(2):
        image = enhance(image, alg)
    return sum(x == '1' for x in image.values())

def part2(data):
    alg, image = data
    convert = {'0':' ', '1':'#'}
    for i in range(50):
        image = enhance(image, alg)
    return sum(x == '1' for x in image.values())

def data(input: str):
    alg, image = input.split('\n\n')
    convert = {'.':'0', '#':'1'}
    image = defaultdict(lambda: '0', mapify_grid(image.split('\n'), lambda x: convert[x]))
    alg = [convert[c] for c in alg]
    return alg, image

#print(part1(data(test)))
#print(part2(data(test)))

ans1 = part1(data(puzzle.input_data))
ans2 = part2(data(puzzle.input_data))

print(f'part 1 = {ans1}')
print(f'part 2 = {ans2}')

#puzzle.answer_a = ans1
#puzzle.answer_b = ans2