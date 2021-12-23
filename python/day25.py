from aocd.models import Puzzle
from aoc_util import *

puzzle = Puzzle(year=2021, day=25)

def part1(data):
    return len(data)

def part2(data):
    return len(data)

def data(input: str):
    return input.split('\n')

ans1 = part1(data(puzzle.input_data))
ans2 = part2(data(puzzle.input_data))

print(f'part 1 = {ans1}')
print(f'part 2 = {ans2}')

#puzzle.answer_a = ans1
#puzzle.answer_b = ans2