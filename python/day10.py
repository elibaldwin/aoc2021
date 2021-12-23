from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=10)

scoremap = {')': 3, ']': 57, '}': 1197, '>':25137}
charmap = {'(': ')', '[':']', '{':'}', '<':'>'}
def part1(data):
    
    score = 0
    for line in data:
        stack = []
        for c in line:
            if c in '([{<':
                stack.append(c)
            else:
                sc = charmap[stack.pop()]
                if c != sc:
                    score += scoremap[c]
                    break
    return score

scoremap2 = {')': 1, ']': 2, '}': 3, '>':4}
def part2(data):
    scores = []
    for line in data:
        stack = []
        corrupt = False
        for c in line:
            if c in '([{<':
                stack.append(c)
            else:
                sc = charmap[stack.pop()]
                if c != sc:
                    corrupt = True
                    break
        if not corrupt:
            score = 0
            while(stack):
                score *= 5
                score += scoremap2[charmap[stack.pop()]]
            scores.append(score)
    scores.sort()
    return scores[len(scores)//2]

def data(input: str):
    return input.split('\n')

test = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''

print(part1(data(test)))
print(part2(data(test)))

ans1 = part1(data(puzzle.input_data))
ans2 = part2(data(puzzle.input_data))

print(f'part 1 = {ans1}')
print(f'part 2 = {ans2}')

#puzzle.answer_a = ans1
#puzzle.answer_b = ans2