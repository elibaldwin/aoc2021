from aocd.models import Puzzle
from numpy import add
from aoc_util import *
from math import ceil, floor
import itertools

puzzle = Puzzle(year=2021, day=18)

test = '''[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]'''

test1 = '''[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]'''

test2 = '''[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]'''

def can_explode(n, depth=0):
    if isinstance(n, int):
        return depth > 4
    return can_explode(n[0], depth+1) or can_explode(n[1], depth+1)

def can_split(n):
    if isinstance(n, int):
        return n >= 10
    return can_split(n[0]) or can_split(n[1])

def explode(n, add_in_l=0, add_in_r=0, depth=0, done=False):
    if isinstance(n, int):
        return n+add_in_l+add_in_r, 0, 0, done
    if depth == 4 and not done:
        return 0, n[0], n[1], True
    l_res, add_l, add_r, done_l = explode(n[0], add_in_l, 0, depth+1, done)
    r_res, add_rl,add_r, done_r = explode(n[1], add_r, add_in_r, depth+1, done_l)
    if add_rl:
        l_res, add_l, _, done_l = explode(n[0], 0, add_rl, depth+1, done_r)
    return [l_res, r_res], add_l, add_r, done_l or done_r

def split(n, done=False):
    if isinstance(n, int):
        if n >= 10 and not done:
            return [floor(n/2), ceil(n/2)], True
        else: return n, done
    lres, ldone = split(n[0], done)
    rres, rdone = split(n[1], done or ldone)
    return [lres, rres], done or rdone

def magnitude(snailn):
    if isinstance(snailn, int):
        return snailn
    return magnitude(snailn[0])*3 + magnitude(snailn[1])*2

def reduce(n):
    while True:
        if can_explode(n):
            n = explode(n)[0]
        elif can_split(n):
            n = split(n)[0]
        else: break  
    return n

def part1(data):
    sum = data[0]
    for snailn in data[1:]:
        sum = [sum, snailn]
        sum = reduce(sum)
    return magnitude(sum)

def part2(data):
    return max(magnitude(reduce([a, b])) for a, b in itertools.permutations(data, 2))

def data(input: str):
    return [eval(l) for l in input.split('\n')]

#print(explode([[[[[9,8],1],2],3],4]))
#print(explode([7,[6,[5,[4,[3,2]]]]]))
#print(explode([[6,[5,[4,[3,2]]]],1]))
#print(explode([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]))
#print(explode([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]))

#print(split([[[[0,7],4],[15,[0,13]]],[1,1]]))

#print(magnitude([[[[0,7],4],[[7,8],[6,0]]],[8,1]]))

#print(explode([[[[[9,8],1],2],3],4]))
#print(explode([7,[6,[5,[4,[3,2]]]]]))
#print(explode([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]))

#s = [[[[0,7],4],[15,[0,13]]],[1,1]]
#print(split(s))

#print(reduce([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]))
#print(explode([[[[0, 7], 4], [7, [[8, 4], 9]]], [1, 1]]))
#print(explode([[[[4,0],[5,0]],[[[4,5],[2,6]],[9,5]]],1]))

#print(reduce([[[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]], [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]]))

print(part1(data(test)))
print(part2(data(test)))

ans1 = part1(data(puzzle.input_data))
ans2 = part2(data(puzzle.input_data))

print(f'part 1 = {ans1}')
print(f'part 2 = {ans2}')

#puzzle.answer_a = ans1
#puzzle.answer_b = ans2