from typing import Any, Callable, Iterable, List, Set, Tuple, Dict

def neighbors_4(p: Tuple[int, int], m: Dict[Tuple[int, int], Any]):
    x1, y1 = p
    for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        x = x1+dx
        y = y1+dy 
        if (x,y) in m:
            yield (x,y)

def neighbors_8(p: Tuple[int, int], m: Dict[Tuple[int, int], Any]):
    x1, y1 = p
    for dx, dy in [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]:
        x = x1+dx
        y = y1+dy 
        if (x,y) in m:
            yield (x,y)

def mapify_grid(grid: List[str], typefn: Callable = lambda x: x) -> Dict[Tuple[int, int], Any]:
    res = dict()
    for y, line in enumerate(grid):
        for x, item in enumerate(line):
            res[(x,y)] = typefn(item)
    return res

def point_bounds(grid):
    xs = [x for x, _ in grid]
    ys = [y for _, y in grid]
    return min(xs), max(xs), min(ys), max(ys)
    
def print_pointset(data: Set[Tuple[int, int]], in_char = '#', not_in_char = ' '):
    xs = [x for x, _ in data]
    ys = [y for _, y in data]
    for y in range(min(ys), max(ys)+1):
        for x in range(min(xs), max(xs)+1):
            c = in_char if ((x,y) in data) else not_in_char
            print(c, end='')
        print()
        
def print_pointdict(data: Dict[Tuple[int, int], Any], char_fn = lambda x: x):
    xs = [x for x, _ in data]
    ys = [y for _, y in data]
    for y in range(min(ys), max(ys)+1):
        for x in range(min(xs), max(xs)+1):
            c = char_fn(data[(x,y)])
            print(c, end='')
        print()

def read_point(s: str) -> Tuple[int, int]:
    x, y = s.split(',')
    return (int(x), int(y))