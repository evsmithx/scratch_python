from pprint import pprint
from typing import List, Tuple

inp = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""
lines = inp.splitlines()
query_row = 10

lines = open("input15.txt", "r").read().splitlines()
query_row = 2000000

exclusion_zones: List[Tuple[int, int]] = []
sb_set = set()  # x positions of sensors/beacons in query row

for line in lines:
    if line == "":
        continue
    line = line.strip().split(' ')
    sx = int(line[2].split('=')[1].strip(',:'))  # todo: regex
    sy = int(line[3].split('=')[1].strip(',:'))
    bx = int(line[8].split('=')[1].strip(',:'))
    by = int(line[9].split('=')[1].strip(',:'))
    print((sx, sy), (bx, by))
    if sy == query_row:
        sb_set.add(sx)
    if by == query_row:
        sb_set.add(bx)
    # find manhattan distance
    md = abs(sx - bx) + abs(sy - by)
    print(md)
    # if it intersects y, find by how much
    overlap = md - abs(query_row - sy)
    print(overlap)
    if overlap >= 0:
        ez = (sx - overlap, sx + overlap + 1)  # left end is included, right end isn't
        exclusion_zones.append(ez)
        print(ez)

exclusion_zones.sort()
pprint(exclusion_zones)
pprint(sb_set)

pointer = exclusion_zones[0][0] - 1
exclusion_sum = 0
for ez in exclusion_zones:
    start, end = ez
    pointer = max(pointer, start)
    next_pointer = max(end, pointer)
    print(start, end, pointer, next_pointer)
    exclusion_sum += next_pointer - pointer
    pointer = next_pointer

excluded = exclusion_sum - len(sb_set)
print(excluded)
# Part 1: 5112034
