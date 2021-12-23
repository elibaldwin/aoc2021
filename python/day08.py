from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=8)

def part1(data):
    s = 0
    for ins, outs in data:
        for x in outs:
            if len(x) in [2, 3, 4, 7]:
                s += 1
    return s


d0 = set('abcefg')
d1 = set('cf')
d2 = set('acdeg')
d3 = set('acdfg')
d4 = set('bcdf')
d5 = set('abdfg')
d6 = set('abdefg')
d7 = set('acf')
d8 = set('abcdefg')
d9 = set('abcdfg')

lenmap = { 2: 1, 4: 4, 3: 7, 7: 8 }

def decode(line):
    digits, disp = line
    ds = [set() for _ in range(10)]
    d9_0_6 = []
    d2_3_5 = []
    for word in digits:
        l = len(word)
        if l in lenmap:
            ds[lenmap[l]] = set(word)
        elif l == 6:
            d9_0_6.append(set(word))
        elif l == 5:
            d2_3_5.append(set(word))
    
    d9_0 = []
    for ws in d9_0_6:
        if ds[1] <= ws:
            d9_0.append(ws)

    segA = (ds[7] - ds[1]).pop()
    segDE = d9_0[0] ^ d9_0[1]
    segD = (ds[4] & segDE).pop()
    segE = (segDE - set([segD])).pop()

    for wset in d2_3_5:
        if set([segA, segD, segE]) <= wset:
            ds[2] = wset
    
    segC = (ds[1] & ds[2]).pop()
    segF = (ds[1] - set([segC])).pop()
    segB = (ds[4] - set([segC, segD, segF])).pop()
    segG = (ds[2] - set([segA, segC, segD, segE])).pop()

    ds[0] = set([segA, segB, segC, segE, segF, segG])
    ds[3] = set([segA, segC, segD, segF, segG])
    ds[5] = set([segA, segB, segD, segF, segG])
    ds[6] = set([segA, segB, segD, segE, segF, segG])
    ds[9] = set([segA, segB, segC, segD, segF, segG])

    digstr = ''
    for word in disp:
        for i in range(10):
            if set(word) == ds[i]:
                digstr += str(i)
                break
    return int(digstr)


def part2(data):
    return sum(decode(line) for line in data)

def data(input: str):
    return [tuple(y.split() for y in x.split(' | ')) for x in input.split('\n')]

ans1 = part1(data(puzzle.input_data))
ans2 = part2(data(puzzle.input_data))

print(f'part 1 = {ans1}')
print(f'part 2 = {ans2}')

#puzzle.answer_a = ans1
#puzzle.answer_b = ans2

#teststr = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
#print(decode(data(teststr)[0]))