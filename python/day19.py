from aocd.models import Puzzle
from aoc_util import *
import numpy as np
import itertools

puzzle = Puzzle(year=2021, day=19)

test = '''--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14'''

def cycle(p: Tuple[int, int, int]) -> Tuple[int, int, int]:
    a, b, c = p
    yield (a, b, c)
    yield (b, c, a)
    yield (c, a, b)

def spin(p: Tuple[int, int, int]) -> Tuple[int, int, int]:
    a, b, c = p
    yield (a, b, c)
    yield (-a, -b, c)
    yield (-c, b, a)
    yield (-a, b, -c)
    yield (a, -c, b)
    
    yield (a, c, -b)
    yield (a, -b, -c)
    yield (-c, -b, -a)

def orientations(p: Tuple[int, int, int]) -> Tuple[int, int, int]:
    for cp in cycle(p):
        for scp in spin(cp):
            yield scp

def find_align(s1, s2, match_goal=12):
    for s1root in s1:
        for o in range(24):
            slice = s2[:,o]
            for root in slice:
                diff = s1root - root
                sl_trans = slice + diff
                n_match = sum(p.tolist() in s1.tolist() for p in sl_trans)
                if n_match >= match_goal:
                    return sl_trans, diff
    return None, None

def part1(data):
    found_scanners = [data[0][:,0]]
    scanner_positions = [[0, 0, 0]]
    foundset = set()
    foundset.add(0)
    tried = set()
    while len(foundset) < len(data):
        for i, scanner in enumerate(data):
            if i in foundset: continue
            for j, root in enumerate(found_scanners):
                if (j,i) in tried: continue
                sc, diff = find_align(root, scanner)
                tried.add((j,i))
                if sc is not None:
                    print('found scanner', i, 'at diff', diff.tolist())
                    scanner_positions.append(diff.tolist())
                    found_scanners.append(sc)
                    foundset.add(i)
                    break
    beacons = set()
    for s in found_scanners:
        points = [tuple(x) for x in s.tolist()]
        beacons.update(points)
    
    dists = []
    for a, b in itertools.combinations(scanner_positions, 2):
        dists.append(sum(abs(x-y) for x, y in zip(a, b)))

    return len(beacons), max(dists)

def part2(data):
    return len(data)

def data(input: str):
    scanners = [[list(orientations(tuple(int(n) for n in line.split(',')))) for line in scanner.split('\n')[1:]] for scanner in input.split('\n\n')]
    return [np.array(s) for s in scanners]

#print(data(test)[0][:,0])
#print(data(test)[0][:,0] + data(test)[0][:,0][0])

tdata = data(test)
#print(tdata[0][:,0])
#s1 = find_align(tdata[0][:,0], tdata[1])
#s4 = find_align(s1[0], tdata[4])
#print(s1[0])
#print(s1[1])
#print(s4[0])
#print(s4[1])
#print(find_align(s4[0], tdata[2]))
#print(find_align(s1[0], tdata[3]))

print(part1(tdata))

ans1 = part1(data(puzzle.input_data))

print(f'part 1 = {ans1[0]}')
print(f'part 2 = {ans1[1]}')

#puzzle.answer_a = ans1
#puzzle.answer_b = ans2