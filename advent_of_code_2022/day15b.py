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
max_range = 20

# lines = open("input15.txt", "r").read().splitlines()
# max_range = 4000000

beacons, sensors, mds = [], [], []
for line in lines:
    if line == "":
        continue
    line = line.strip().split(' ')
    sx = int(line[2].split('=')[1].strip(',:'))  # todo: regex
    sy = int(line[3].split('=')[1].strip(',:'))
    bx = int(line[8].split('=')[1].strip(',:'))
    by = int(line[9].split('=')[1].strip(',:'))
    sensors.append((sx, sy))
    beacons.append((bx, by))
    md = abs(sx - bx) + abs(sy - by)
    mds.append(md)

for query_row in range(max_range):
    exclusion_zones: List[Tuple[int, int]] = []

    for ((sx, sy), md) in zip(sensors, mds):
        # if it intersects y, find by how much
        overlap = md - abs(query_row - sy)
        if overlap >= 0:
            ez = (sx - overlap, sx + overlap + 1)  # left end is included, right end isn't
            exclusion_zones.append(ez)

    exclusion_zones.sort()
    # pprint(exclusion_zones)

    pointer = 0
    ez_iter = iter(exclusion_zones)
    ez = next(ez_iter)
    while True:
        try:
            if pointer < ez[0]:
                break
            if ez[0] <= pointer < ez[1]:
                pointer = ez[1]
                ez = next(ez_iter)
            elif pointer >= ez[1]:
                ez = next(ez_iter)
            if pointer >= max_range:
                break
        except StopIteration:
            break

    print(pointer, query_row)
    if pointer < max_range:
        print("Yay, got it")
        print(pointer * 4000000 + query_row)
        break

# Part 2: 13172087230812
