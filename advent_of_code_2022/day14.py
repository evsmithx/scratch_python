from pprint import pprint
from typing import Tuple, List

inp = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

with open("input14.txt", "r") as fp:
    inp = fp.read()

# NB: x goes rightwards, y goes downwards
minx, miny, maxx, maxy = 500, 0, 500, 0  # sand comes from (500, 0)
rocks: List[List[Tuple[int, int]]] = []
for line in inp.split("\n"):
    if line.strip() == "":
        continue
    path = []
    line = line.strip().split('->')
    for l in line:
        x, y = l.split(',')
        x = int(x)
        y = int(y)
        path.append((x, y))
        minx, maxx = min(minx, x), max(maxx, x)
        miny, maxy = min(miny, y), max(maxy, y)

    rocks.append(path)

pprint(rocks, width=400)
print(minx, miny, maxx, maxy)
# add extra line on the left, right and bottom
minx -= 1
maxx += 1
maxy += 1
print(minx, miny, maxx, maxy)
assert miny == 0, f"grid arithmetic from here on assumes miny==0 but it is {miny}"

grid = [['.'] * (maxx - minx + 1) for _ in range(maxy + 1)]

for path in rocks:
    px, py = path[0]
    grid[py][px - minx] = '#'
    for (qx, qy) in path[1:]:
        grid[qy][qx - minx] = '#'
        if qx == px:
            if qy < py:
                for y in range(qy, py):
                    grid[y][qx - minx] = '#'
            else:
                for y in range(py, qy):
                    grid[y][qx - minx] = '#'
        elif qy == py:
            if qx < px:
                for x in range(qx, px):
                    grid[py][x - minx] = '#'
            else:
                for x in range(px, qx):
                    grid[py][x - minx] = '#'
        else:
            raise Exception("Assumed that paints would be colinear - bad assumption!")
        px, py = qx, qy


def print_grid(g):
    for row in grid:
        print(''.join(row))
    print()

counter = 0
sand_start = (500, 0)
grid[sand_start[1]][sand_start[0] - minx] = '+'
print_grid(grid)
done = False
while not done:
    # print_grid(grid)
    sandx, sandy = sand_start
    while True:
        if sandx == minx or sandx == maxx or sandy == maxy:
            print("sand reached end of grid")
            done = True
            break
        if grid[sandy + 1][sandx - minx] == '.':
            sandy += 1
        elif grid[sandy + 1][sandx - 1 - minx] == '.':
            sandy += 1
            sandx -= 1
        elif grid[sandy + 1][sandx + 1 - minx] == '.':
            sandy += 1
            sandx += 1
        else:
            counter += 1
            grid[sandy][sandx - minx] = 'o'
            print(f"Block {counter} came to rest at {sandx} {sandy}")
            break

print_grid(grid)
print(counter)

# 728 is correct
