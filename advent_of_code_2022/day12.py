from pprint import pprint
from typing import Tuple, Set, List

input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

with open("input12.txt", "r") as fp:
    input = fp.read()

grid: List[List[int]] = []

start = (-1, 0)
end = (-1, 0)
norm = 96  # normalise heights to the range 0-27
for i, line in enumerate(input.split('\n')):
    line = [ord(x) - norm for x in line.strip()]
    if len(line) == 0:
        continue
    try:
        s_ind = line.index(ord('S')-norm)
        start = (i, s_ind)
        line[s_ind] = ord("a") - 1 - norm
    except ValueError:
        pass
    try:
        e_ind = line.index(ord('E') - norm)
        end = (i, e_ind)
        line[e_ind] = ord("z") + 1 - norm
    except ValueError:
        pass
    grid.append(line)

assert(start[0] != -1)
assert(end[0] != -1)

pprint(grid, width=400)
print(start, end)

gridx = len(grid)
gridy = len(grid[0])
print("dimensions", gridx, gridy)

current_set: Set[Tuple[int, int]] = {start}
next_set: Set[Tuple[int, int]]  = set()
max_possible_steps = gridx * gridy
min_steps_grid = [[max_possible_steps] * gridy for _ in range(gridx)]
min_steps_grid[start[0]][start[1]] = 0
r = 1
not_done = True
while not_done:
    print("new round", r)
    pprint(current_set)
    while len(current_set):
        cx, cy = current_set.pop()
        ch = grid[cx][cy]

        # look at everything reachable from current location (four squares)
        for square in [(cx+1, cy), (cx, cy+1), (cx-1, cy), (cx, cy-1)]:
            sx, sy = square
            if sx < 0 or sx > gridx - 1  or sy < 0 or sy > gridy - 1:
                print("bad index", square)
                continue
            height = grid[sx][sy]
            if height <= ch + 1:
                if min_steps_grid[sx][sy] > r:
                    # then hasn't been seen yet
                    min_steps_grid[sx][sy] = r
                    next_set.add(square)
                    if height == 27:
                        print(f"Reached end in {r} steps")
                        not_done = False
                        break

    if len(next_set) == 0:
        break
    current_set = next_set.copy()
    next_set = set()
    r += 1
    pprint(min_steps_grid, width=400)
