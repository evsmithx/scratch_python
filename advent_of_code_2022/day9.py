from pprint import pprint
from typing import Tuple, Set

input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

with open("input9.txt", "r") as fp:
    input = fp.read()

head: Tuple[int, int] = (0, 0)  # (x,y)
tail: Tuple[int, int] = (0, 0)
tail_positions: Set[Tuple[int, int]] = {tail}


def update_tail(head: Tuple[int, int], tail: Tuple[int, int]) -> Tuple[int, int]:
    diff = (head[0] - tail[0], head[1] - tail[1])
    if -1 <= diff[0] <= 1 and -1 <= diff[1] <= 1:
        return tail
    if diff == (2, 0):
        return tail[0] + 1, tail[1]
    if diff == (-2, 0):
        return tail[0] - 1, tail[1]
    if diff == (0, 2):
        return tail[0], tail[1] + 1
    if diff == (0, -2):
        return tail[0], tail[1] - 1
    if diff in [(2, 1), (1, 2)]:
        return tail[0] + 1, tail[1] + 1
    if diff in [(2, -1), (1, -2)]:
        return tail[0] + 1, tail[1] - 1
    if diff in [(-2, -1), (-1, -2)]:
        return tail[0] - 1, tail[1] - 1
    if diff in [(-2, 1), (-1, 2)]:
        return tail[0] - 1, tail[1] + 1
    raise Exception("missing case {}".format(diff))


for line in input.split('\n'):
    if line.strip() == "":
        continue
    # normal grid - R increases x, U increases y etc.
    direction, steps = line.strip().split(' ')
    steps = int(steps)
    print(direction, steps)
    if direction == 'R':
        for _ in range(steps):
            head = (head[0] + 1, head[1])
            tail = update_tail(head, tail)
            tail_positions.add(tail)
    if direction == 'L':
        for _ in range(steps):
            head = (head[0] - 1, head[1])
            tail = update_tail(head, tail)
            tail_positions.add(tail)
    if direction == 'U':
        for _ in range(steps):
            head = (head[0], head[1] + 1)
            tail = update_tail(head, tail)
            tail_positions.add(tail)
    if direction == 'D':
        for _ in range(steps):
            head = (head[0], head[1] - 1)
            tail = update_tail(head, tail)
            tail_positions.add(tail)

pprint(tail_positions)
print(len(tail_positions))