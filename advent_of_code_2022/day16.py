import time
from typing import List, Tuple, FrozenSet

inp = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

flows = {}
adjacency = {}
for line in inp.splitlines():
    if line.strip() == "":
        continue
    line = line.split(' ')
    valve = line[1]
    flow = int(line[4].split('=')[1].strip(';'))
    adjacent = [x.strip(',') for x in line[9:]]
    flows[valve] = flow
    adjacency[valve] = adjacent

print(flows)
print(adjacency)


demo_path: List[str] = ['AA', 'DD', 'DD', 'CC', 'BB', 'BB', 'AA', 'II', 'JJ', 'JJ', 'II', 'AA', 'DD', 'EE', 'FF', 'GG',
                        'HH', 'HH', 'GG', 'FF', 'EE', 'EE', 'DD', 'CC', 'CC']


good_valves = set({x for x, y in flows.items() if y > 0})
print(good_valves)
max_flow = 0
max_path = []
path_counter = 0


# @functools.lru_cache(None)
def visit(path: Tuple[str], open_valves: FrozenSet[str], score):
    global max_flow, max_path, path_counter
    current_flow = sum((flows[x] for x in open_valves))
    score += current_flow
    # print(len(path), current_flow, score)
    if len(path) == 30 or len(open_valves) == len(good_valves):
        if len(path) < 30:
            score += current_flow * (30 - len(path))
        if score > max_flow:
            max_flow = score
            max_path = path
            print("max")
            print(path, score, path_counter)
        # exit(0)
        path_counter += 1
        return
    else:
        current_valve: str = path[-1]
        if current_valve not in open_valves and current_valve in good_valves:
            visit(path + (current_valve,), open_valves.union({current_valve}), score)
        for option in adjacency[path[-1]]:
            visit(path + (option,), open_valves, score)


def count_open(path):
    open_valves = set()
    p = path[0]
    for q in path[1:]:
        # print(q, p)
        if q == p:
            open_valves.add(p)
        p = q
    return frozenset(open_valves)


total_flow = 0
co = set()
flow = 0
i = 0
for i in range(len(demo_path)):
    co = count_open(demo_path[0:i + 1])
    if i > 10:
        print(demo_path[0:i + 1], co)
        time_now = time.process_time()
        visit(tuple(demo_path[0:i + 1]), co, total_flow)
        print(time.process_time() - time_now)
        break
    flow = sum((flows[x] for x in co))
    total_flow += flow
    print(i + 1)
    print(co)
    print(flow)
    print(total_flow)
    print()
