from collections import defaultdict
from aocd.models import Puzzle
from aoc_util import *

puzzle = Puzzle(year=2021, day=21)

test = '''Player 1 starting position: 4
Player 2 starting position: 8'''

def roll(i):
    return (i-1)%100 +1

def part1(data):
    s1, s2 = 0, 0
    p1, p2 = data
    r = 1
    while s1 < 1000 and s2 < 1000:
        r1 = sum(roll(i) for i in range(r, r+3))
        r += 3
        p1 = (p1 + r1) % 10
        s1 += (p1+1)
        if s1 >= 1000: break

        r2 = sum(roll(i) for i in range(r, r+3))
        r += 3
        p2 = (p2 + r2) % 10
        s2 += (p2+1)
    lscore = min(s1, s2)
    return lscore * (r-1)

R = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}
def search(p1, s1, p2, s2, p1turn, count):
    if s1 >= 21:
        return count, 0
    elif s2 >= 21:
        return 0, count
    if p1turn:
        c1, c2 = 0, 0
        for r, c in R.items():
            np1 = (p1+r) % 10
            cc1, cc2 = search(np1, s1+(np1+1), p2, s2, False, count*c)
            c1 += cc1
            c2 += cc2
        return c1, c2
    else:
        c1, c2 = 0, 0
        for r, c in R.items():
            np2 = (p2+r) % 10
            cc1, cc2 = search(p1, s1, np2, s2+(np2+1), True, count*c)
            c1 += cc1
            c2 += cc2
        return c1, c2
 
def part2(data):
    p1, p2 = data
    p1_wincount, p2_wincount = search(p1, 0, p2, 0, True, 1)
    return max(p1_wincount, p2_wincount)

def data(input: str):
    p1, p2 = input.split('\n')
    return int(p1[-1])-1, int(p2[-1])-1

#print(part2(data(test)))

ans1 = part1(data(puzzle.input_data))
ans2 = part2(data(puzzle.input_data))

print(f'part 1 = {ans1}')
print(f'part 2 = {ans2}')

#puzzle.answer_a = ans1
#puzzle.answer_b = ans2