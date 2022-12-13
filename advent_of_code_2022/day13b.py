import functools
from enum import Enum
from pprint import pprint

inp = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""


with open("input13.txt", "r") as fp:
    inp = fp.read()

class CompResult(Enum):
    TRUE = 1
    INCONCLUSIVE = 0
    FALSE = -1


def recursive_comparison(l3, l4) -> CompResult:
    # print(f"l3 {l3} l4 {l4}")
    if isinstance(l3, list) and isinstance(l4, list):
        for i, j in zip(l3, l4):
            rc = recursive_comparison(i, j)
            if rc in [CompResult.TRUE, CompResult.FALSE]:
                return rc
        if len(l3) < len(l4):
            return CompResult.TRUE
        elif len(l3) > len(l4):
            return CompResult.FALSE
        return CompResult.INCONCLUSIVE
    elif isinstance(l3, int) and isinstance(l4, int):
        if l3 < l4:
            return CompResult.TRUE
        elif l3 > l4:
            return CompResult.FALSE
        return CompResult.INCONCLUSIVE
    elif isinstance(l3, list) and isinstance(l4, int):
        return recursive_comparison(l3, [l4])
    elif isinstance(l3, int) and isinstance(l4, list):
        return recursive_comparison([l3], l4)
    raise Exception(f"Bad types {l3} {l4}")


input_iter = iter(inp.split('\n'))
marker1 = [[2]]
marker2 = [[6]]
signals = [marker1, marker2]
while True:
    try:
        line1 = next(input_iter).strip()
        line2 = next(input_iter).strip()
        next(input_iter)

        exec_output = {}
        exec(f"l1 = {line1}", exec_output)  # todo: sanitise inp
        exec(f"l2 = {line2}", exec_output)

        l1 = exec_output["l1"]
        l2 = exec_output["l2"]

        pprint(l1, width=200)
        pprint(l2, width=200)
        signals.append(l1)
        signals.append(l2)

    except StopIteration:
        break


def sorted_by(l5, l6):
    rc = recursive_comparison(l5, l6)
    if rc == CompResult.TRUE:
        return -1
    elif rc == CompResult.FALSE:
        return 1
    raise Exception(f"Comparison of {l5} and {l6} was inconclusive")


cmp = functools.cmp_to_key(sorted_by)

signals.sort(key=cmp)
print("Sorted")
pprint(signals, width=200)
marker1_index = signals.index(marker1) + 1
print(marker1_index)
marker2_index = signals.index(marker2) + 1
print(marker2_index)
print(marker1_index*marker2_index)