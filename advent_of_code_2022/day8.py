from pprint import pprint

trees = []
with open("input8.txt", "r") as fp:
    for line in fp:
        line = line.strip()
        trees.append([int(x) for x in line])

# small_trees = [
#     30373,
#     25512,
#     65332,
#     33549,
#     35390]
#
# for st in small_trees:
#     trees.append([int(x) for x in str(st)])

# pprint(trees)

n_cols = len(trees)
assert n_cols == len(trees[0])
visible = set()
for i in range(n_cols):
    max_height = -1
    for j in range(n_cols):
        if trees[i][j] > max_height:
            max_height = trees[i][j]
            visible.add((i, j))

for i in range(n_cols):
    max_height = -1
    for j in range(n_cols-1, -1, -1):
        if trees[i][j] > max_height:
            max_height = trees[i][j]
            visible.add((i, j))

for j in range(n_cols):
    max_height = -1
    for i in range(n_cols):
        if trees[i][j] > max_height:
            max_height = trees[i][j]
            visible.add((i, j))

for j in range(n_cols):
    max_height = -1
    for i in range(n_cols-1, -1, -1):
        if trees[i][j] > max_height:
            max_height = trees[i][j]
            visible.add((i, j))

print(len(visible))

def check_visibility(i, j):
    tree_height = trees[i][j]
    # print("tree height", tree_height)
    if i == 0 or j == 0 or i == n_cols-1 or j == n_cols-1:
        return 0
    north, south, west, east = i, n_cols-i-1, j, n_cols-j-1
    for k in range(i-1, -1, -1):
        if trees[k][j] >= tree_height:
            north = i - k
            break
    for k in range(i+1, n_cols):
        if trees[k][j] >= tree_height:
            south = k - i
            break
    for k in range(j-1, -1, -1):
        if trees[i][k] >= tree_height:
            west = j - k
            break
    for k in range(j+1, n_cols):
        if trees[i][k] >= tree_height:
            east = k - j
            break
    # print(i, j, north, south, west, east)
    return north*south*west*east

# check_visibility(1, 2)
# check_visibility(3, 2)
# print(check_visibility(1, 4))
#
max_score = 0
for i in range(n_cols):
    for j in range(n_cols):
        score = check_visibility(i, j)
        if score > max_score:
            max_score = score
            print(max_score)
print(max_score)
