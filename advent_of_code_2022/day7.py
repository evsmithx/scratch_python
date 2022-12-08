from dataclasses import dataclass
from pprint import pprint
from typing import List, Dict

@dataclass
class Node:
    name: str
    id: int
    size: int = 0
    dir: bool = True


nodes = [Node(name='/', id=0)]  # id number to Node list
graph: Dict[int, List[int]] = {0: []}
path: List[Node] = []  # list of Nodes
# need a lookup of id to Node
# need an adjacency list of id numbers
# could store the adjacency list in with the node info
# the child_name1 lookup is annoying, but manageable


def name_to_id(child_name1: str, parent_id1: int):
    child_ids = graph[parent_id1]
    for cid in child_ids:
        if nodes[cid].name == child_name1:
            return cid
    raise Exception("Node not found")


with open("input7.txt", "r") as fp:
    for line in fp:
        line = line.strip().split(" ")
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    path.pop()
                    continue
                elif line[2] == '/':
                    path.append(nodes[0])
                    continue

                child_name = line[2]
                parent_id = path[-1].id
                child_id = name_to_id(child_name, parent_id)
                path.append(nodes[child_id])
                continue
            elif line[1] == "ls":
                continue
        else:
            if line[0] == "dir":
                node_num = len(nodes)
                nodes.append(Node(name=line[1], id=node_num))
                graph[path[-1].id].append(node_num)
                graph[node_num] = []
                continue
            elif line[0].isnumeric():
                node_num = len(nodes)
                nodes.append(Node(name=line[1], id=node_num, size=int(line[0]), dir=False))
                graph[path[-1].id].append(node_num)
                graph[node_num] = []
                for node in path:
                    node.size += int(line[0])
                continue
        raise Exception("Shouldn't be here!!")

sizesum = 0
for node in nodes:
    if node.size < 100000 and node.dir:
        sizesum += node.size

pprint(sizesum)

#That's not the right answer; your answer is too high. If you're stuck, make sure you're using the full input data;
# there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute
# before trying again. (You guessed 6209920.) [Return to Day 7]

# check the sizes
for node in nodes:
    child_size_sum = 0
    for cid in graph[node.id]:
        child_size_sum += nodes[cid].size
    if node.size != child_size_sum and node.dir == True:
        print("Error", node, node.size, child_size_sum, graph[node.id])
        for cid in graph[node.id]:
            pprint(nodes[cid])
        print("done")


# 1432936
# That's the right answer! You are one gold star closer to collecting enough star fruit. [Continue to Part Two]

total_disk = 70000000
space_required = 30000000
used = nodes[0].size
extra_required = space_required - (total_disk - used)
print(total_disk, space_required, used, extra_required)
best_deletion = nodes[0]

for node in nodes:
    if node.dir is False:
        continue
    if extra_required < node.size < best_deletion.size:
        best_deletion = node
        pprint(best_deletion)

# That's not the right answer. If you're stuck, make sure you're using the full input data; there are also some general
# tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again.
# (You guessed lmqcbbm.) [Return to Day 7]