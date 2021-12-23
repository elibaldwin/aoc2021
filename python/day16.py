from aocd.models import Puzzle
from numpy import product
from aoc_util import *

puzzle = Puzzle(year=2021, day=16)

def part1(data):
    s = 0
    i = 0
    while i < len(data) and '1' in data[i:]:
        v = int(data[i:i+3], 2)
        i+=3
        t = int(data[i:i+3], 2)
        i+=3
        if t == 4:
            s += v
            literal = ''
            while data[i] == '1':
                i+=1
                literal += data[i:i+4]
                i+=4
            i+=1
            literal += data[i:i+4]
            literal = int(literal, 2)
            i+=4
        else:
            s += v
            ltype = int(data[i])
            i+=1
            if ltype == 0:
                blen = int(data[i:i+15], 2)
                i+= 15
            else:
                nsub = int(data[i:i+11], 2)
                i+= 11
    return s

def get_literal(data, i):
    literal = ''
    while data[i] == '1':
        i+=1
        literal += data[i:i+4]
        i+=4
    i+=1
    literal += data[i:i+4]
    literal = int(literal, 2)
    i+=4
    return (i, literal)

def get_packet(data, i):
    v = int(data[i:i+3], 2)
    i+=3
    t = int(data[i:i+3], 2)
    i+=3
    if t == 4:
        return get_literal(data, i)
    else:
        ltype = int(data[i])
        i+=1
        subs = []
        if ltype == 0:
            blen = int(data[i:i+15], 2)
            i+= 15
            endsub = i + blen
            while i < endsub:
                i, subval = get_packet(data, i)
                subs.append(subval)
        else:
            nsub = int(data[i:i+11], 2)
            i+= 11
            for _ in range(nsub):
                i, subval = get_packet(data, i)
                subs.append(subval)
        if t == 0:
            return (i, sum(subs))
        elif t == 1:
            return (i, product(subs))
        elif t == 2:
            return (i, min(subs))
        elif t == 3:
            return (i, max(subs))
        elif t == 5:
            rval = 1 if subs[0] > subs[1] else 0
            return (i, rval)
        elif t == 6:
            rval = 1 if subs[0] < subs[1] else 0
            return (i, rval)
        elif t == 7:
            rval = 1 if subs[0] == subs[1] else 0
            return (i, rval)

def part2(data):
    return get_packet(data, 0)[1]

def data(input: str):
    bin_s = ''
    for c in input:
        bs = '{:b}'.format(int(c, 16))
        bin_s += (4-len(bs)) * '0' + bs
    return bin_s

#print(part2(data("C200B40A82")))

ans1 = part1(data(puzzle.input_data))
ans2 = part2(data(puzzle.input_data))

print(f'part 1 = {ans1}')
print(f'part 2 = {ans2}')

#puzzle.answer_a = ans1
#puzzle.answer_b = ans2