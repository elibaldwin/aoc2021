from aocd.models import Puzzle
from collections import deque, Counter, defaultdict

puzzle = Puzzle(year=2021, day=6)

def part1(data):
    timers = deque(data)
    for _ in range(80):
        next = deque()
        for timer in timers:
            if timer == 0:
                next.append(8)
                next.append(6)
            else:
                next.append(timer-1)
        timers = next
    return len(timers)

def part2(data):
    counts = Counter(data)
    for _ in range(256):
        next = defaultdict(int)
        for timer, count in counts.items():
            if timer == 0:
                next[6] += count
                next[8] += count
            else:
                next[timer-1] += count
        counts = next
    return sum(v for k,v in counts.items())
                
def data(input):
    return [int(x) for x in input.split(',')]

ans1 = part1(data(puzzle.input_data))
ans2 = part2(data(puzzle.input_data))

print(f'part 1 = {ans1}')
print(f'part 2 = {ans2}')

#puzzle.answer_a = ans1
puzzle.answer_b = ans2