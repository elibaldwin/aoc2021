from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2021, day=4)

def isWin(board, drawn):
    for slicing in board:
        for row in slicing:
            if set(row).issubset(drawn):
                return True
    return False

def score(board, drawn):
    rows, _ = board
    s = 0
    for row in rows:
        for x in row:
            if x not in drawn:
                s += int(x)
    return s * int(drawn[-1])

def show(board):
    rows, _ = board
    for row in rows:
        print(' '.join(row))

def part1(data):
    draws, boards = data
    
    for i in range(len(draws)):
        draw = draws[:i+1]
        drawset = set(draw)
        for board in boards:
            if isWin(board, drawset):
                show(board)
                print(draw)
                return score(board, draw)

def part2(data):
    draws, boards = data
    wins = [False for _ in boards]
    
    for i in range(len(draws)):
        draw = draws[:i+1]
        drawset = set(draw)
        for j, board in enumerate(boards):
            if wins[j]: continue
            if isWin(board, drawset):
                wins[j] = True
                if all(wins):
                    return score(board, draw)

def data(puzzle: Puzzle):
    chunks = puzzle.input_data.split('\n\n')
    draws = chunks[0].split(',')
    boards = chunks[1:]
    boards = [[l.split() for l in board.split('\n')] for board in boards]
    boards = [(board, [[row[i] for row in board] for i in range(5)]) for board in boards]
    return draws, boards

ans1 = part1(data(puzzle))
ans2 = part2(data(puzzle))

print(f'part 1 = {ans1}')
print(f'part 2 = {ans2}')

#puzzle.answer_a = ans1
#puzzle.answer_b = ans2