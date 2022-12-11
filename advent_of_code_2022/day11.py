from pprint import pprint
from typing import List

input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

# with open("input11.txt", "r") as fp:
#     input = fp.read()

monkey_items: List[List[int]] = []
monkey_functions: List[callable] = []

input_iter = iter(input.split('\n'))
while True:
    try:
        line = next(input_iter)
        line = line.strip()
        if line == "":
            continue
        line = line.split(' ')
        if line[0] == "Monkey":
            line = next(input_iter).strip().split(' ')  # line[0] == "Starting":
            items = [int(x.strip(',')) for x in line[2:]]
            monkey_items.append(items)

            line = next(input_iter).strip().split(' ') # line[0] == "Operation":
            op = line[4]  # gonna exec, need to sanitise input
            assert(op=="*" or op=="+")
            right = line[5]
            try:
                int(right)
            except ValueError:
                assert(right == "old")

            line = next(input_iter).strip().split(' ')  # line[0] == "Test":
            divisor = int(line[3])

            line = next(input_iter).strip().split(' ')  # True
            monkey_true = int(line[5])
            line = next(input_iter).strip().split(' ')  # False
            monkey_false = int(line[5])

            func = f"""
def monkeyfunc(old):
    new = old {op} {right}
    if new % {divisor} == 0:
        return new, {monkey_true}
    else:
        return new, {monkey_false}
"""
            exec_output = {}
            exec(func, exec_output)
            monkey_functions.append(exec_output["monkeyfunc"])
    except StopIteration:
        break


counts = [0] * len(monkey_items)
for r in range(10000):
    print(r)
    for i in range(len(monkey_items)):
        mi = monkey_items[i]
        mf = monkey_functions[i]
        for item in mi:
            new, monkey_index = mf(item)
            monkey_items[monkey_index].append(new)
            counts[i] += 1
        monkey_items[i] = []
    # pprint(monkey_items)
pprint(counts)
counts.sort(reverse=True)
print(counts[0]*counts[1])

#part 1: 113220
