from pprint import pprint
from typing import Tuple, Set

# input = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2
# """

# input = """R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20
# """
#
with open("input9.txt", "r") as fp:
    input = fp.read()

rope = [(0, 0)] * 10
tail_positions: Set[Tuple[int, int]] = {rope[-1]}


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
    if diff in [(2, 1), (1, 2), (2, 2)]:
        return tail[0] + 1, tail[1] + 1
    if diff in [(2, -1), (1, -2), (2, -2)]:
        return tail[0] + 1, tail[1] - 1
    if diff in [(-2, -1), (-1, -2), (-2, -2)]:
        return tail[0] - 1, tail[1] - 1
    if diff in [(-2, 1), (-1, 2), (-2, 2)]:
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
            rope[0] = (rope[0][0] + 1, rope[0][1])
            for i in range(1, len(rope)):
                rope[i] = update_tail(rope[i-1], rope[i])
            tail_positions.add(rope[-1])
    if direction == 'L':
        for _ in range(steps):
            rope[0] = (rope[0][0] - 1, rope[0][1])
            for i in range(1, len(rope)):
                rope[i] = update_tail(rope[i-1], rope[i])
            tail_positions.add(rope[-1])
    if direction == 'U':
        for _ in range(steps):
            rope[0] = (rope[0][0], rope[0][1] + 1)
            for i in range(1, len(rope)):
                rope[i] = update_tail(rope[i-1], rope[i])
            tail_positions.add(rope[-1])
    if direction == 'D':
        for _ in range(steps):
            rope[0] = (rope[0][0], rope[0][1] - 1)
            for i in range(1, len(rope)):
                rope[i] = update_tail(rope[i-1], rope[i])
            tail_positions.add(rope[-1])

pprint(tail_positions)
print(len(tail_positions))