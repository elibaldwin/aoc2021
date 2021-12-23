from collections import deque
from typing import Counter
from aocd.models import Puzzle
from aoc_util import *

puzzle = Puzzle(year=2021, day=14)

test = '''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''

def part1(data):
    seq, rules = data
    seq = deque(seq)
    for i in range(10):
        n = len(seq)-1
        for _ in range(n):
            k = seq[0] + seq[1]
            seq.rotate(-1)
            seq.append(rules[k])
        seq.rotate(-1)
    counts = Counter(seq)
    return counts.most_common()[0][1] - counts.most_common()[-1][1]
 
def part2(data):
    seq, rules = data
    start_pairs = [x+y for x,y in zip(seq, seq[1:])]
    counts = Counter(start_pairs)
    for i in range(40):
        next_counts = Counter()
        for k, v in counts.items():
            next_counts[k[0]+rules[k]] += v
            next_counts[rules[k]+k[1]] += v
        counts = next_counts
    final_count = Counter([seq[0]])
    for k,v in counts.items():
        final_count[k[1]] += v
    return final_count.most_common()[0][1] - final_count.most_common()[-1][1]
        

def data(input: str):
    seq, rules = input.split('\n\n')
    rules = [x.split(' -> ') for x in rules.split('\n')]
    rulemap = {x : y for x,y in rules}
    return (seq, rulemap)

#print(part1(data(test)))
#print(part2(data(test)))

ans1 = part1(data(puzzle.input_data))
ans2 = part2(data(puzzle.input_data))

print(f'part 1 = {ans1}')
print(f'part 2 = {ans2}')

#puzzle.answer_a = ans1
#puzzle.answer_b = ans2