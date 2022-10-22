def find_path(g, start, end):
    path = [start]
    edge_weights = []
    explored = set()

    vertex = start
    while True:
        if vertex == end:
            break
        for next_vertex, weight in g[vertex].items():
            if weight != 0 and next_vertex not in explored and next_vertex not in path:
                path.append(next_vertex)
                edge_weights.append(weight)
                vertex = next_vertex
                break
        else:
            explored.add(vertex)
            if vertex == start:
                return [], 0
            else:
                path.pop()
                edge_weights.pop()
                vertex = path[-1]

    max_flow = min(edge_weights)
    return path, max_flow


def find_path2(g, start, end):
    explored = set()
    current_layer = {start}
    paths = {start: [-1]}

    finished = False
    while not finished:
        # print("path2", explored, current_layer)
        # print(paths)
        next_layer = set()

        if len(current_layer) == 0:
            # no path left
            return [], 0
        for vertex in current_layer:
            if vertex == end:
                finished = True
            for next_vertex, weight in g[vertex].items():
                if weight != 0 and next_vertex not in explored:
                    paths[next_vertex] = paths[vertex] + [next_vertex]
                    next_layer.add(next_vertex)
        explored.update(current_layer)
        current_layer = next_layer

    shortest_path = paths[end]
    max_flow = float("inf")
    for i in range(1, len(shortest_path) - 2):
        max_flow = min(max_flow, g[shortest_path[i]][shortest_path[i + 1]])
    # print(shortest_path, max_flow)
    return shortest_path, max_flow


def solution(entrances, exits, path):
    start = len(path)
    end = len(path) + 1
    graph = [[0 for _ in range(len(path) + 2)] for _ in range(len(path) + 2)]

    for i, flow in enumerate(path):
        for j, weight in enumerate(flow):
            graph[i][j] = weight

    # omni-source
    for i in entrances:
        graph[start][i] = sum(path[i])

    # omni-sink
    for i in exits:
        graph[i][end] = sum(path[x][i] for x in range(len(path)))

    total_flow = MaxFlow(graph, start, end)
    return total_flow


# This code is sourced from https://github.com/anxiaonong/Maxflow-Algorithms/blob/master/Push-Relabel%20Algorithm.py
# In real life I'd use an established library!
def MaxFlow(C, s, t):
    n = len(C)  # C is the capacity matrix
    F = [[0] * n for i in range(n)]

    # the residual capacity from u to v is C[u][v] - F[u][v]
    height = [0] * n  # height of node
    excess = [0] * n  # flow into node minus flow from node
    seen = [0] * n  # neighbours seen since last relabel
    # node "queue"
    nodelist = [i for i in range(n) if i != s and i != t]

    # push operation
    def push(u, v):
        send = min(excess[u], C[u][v] - F[u][v])
        F[u][v] += send
        F[v][u] -= send
        excess[u] -= send
        excess[v] += send

    # relabel operation
    def relabel(u):
        # find smallest new height making a push possible,
        # if such a push is possible at all
        min_height = float('inf')
        for v in range(n):
            if C[u][v] - F[u][v] > 0:
                min_height = min(min_height, height[v])
                height[u] = min_height + 1

    def discharge(u):
        while excess[u] > 0:
            if seen[u] < n:  # check next neighbour
                v = seen[u]
                if C[u][v] - F[u][v] > 0 and height[u] > height[v]:
                    push(u, v)
                else:
                    seen[u] += 1
            else:  # we have checked all neighbours. must relabel
                relabel(u)
                seen[u] = 0

    height[s] = n  # longest path from source to sink is less than n long
    excess[s] = float("inf")  # send as much flow as possible to neighbours of source
    for v in range(n):
        push(s, v)

    p = 0
    while p < len(nodelist):
        u = nodelist[p]
        old_height = height[u]
        discharge(u)
        if height[u] > old_height:
            nodelist.insert(0, nodelist.pop(p))  # move to front of list
            p = 0  # start from front of list
        else:
            p += 1
    return sum(F[s])


print(solution([0], [3],
               [[0, 7, 0, 0],
                [0, 0, 6, 0],
                [0, 0, 0, 8],
                [9, 0, 0, 0]]))

print(solution([0, 1], [4, 5],
               [[0, 0, 4, 6, 0, 0],
                [0, 0, 5, 2, 0, 0],
                [0, 0, 0, 0, 4, 4],
                [0, 0, 0, 0, 6, 6],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]]))

print(solution([0], [3],
               [[0, 7, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 8],
                [9, 0, 0, 0]]))

"""
Python cases --
Input:
solution.solution([0], [3],
    [[0, 7, 0, 0],
    [0, 0, 6, 0],
    [0, 0, 0, 8],
    [9, 0, 0, 0]])
Output:
    6

Input:
solution.solution([0, 1], [4, 5],
    [[0, 0, 4, 6, 0, 0],
    [0, 0, 5, 2, 0, 0],
    [0, 0, 0, 0, 4, 4],
    [0, 0, 0, 0, 6, 6],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]])
Output:
    16

This is a maximum flow problem
Try to implement the ford-fulkerson method
Okay, not good enough. try preflow push

"""
