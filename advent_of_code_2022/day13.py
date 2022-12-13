from enum import Enum
from pprint import pprint

input = """[1,1,3,1,1]
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
    input = fp.read()

input_iter = iter(input.split('\n'))
index = 1
total = 0
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

        print(index)
        pprint(l1, width=200)
        pprint(l2, width=200)


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


        result = recursive_comparison(l1, l2)
        print(result)
        assert result in [CompResult.TRUE, CompResult.FALSE]
        if result == CompResult.TRUE:
            total += index
        index += 1
    except StopIteration:
        break

print("total", total)
