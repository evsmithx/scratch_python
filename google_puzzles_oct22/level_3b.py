def solution2(x, y):
    x = int(x)
    y = int(y)
    if y < x:
        x, y = y, x

    if (x, y) == (1, 1):
        return "0"
    elif (x, y) == (1, 2):
        return "1"

    depth = 1
    nodes = [(1, 2)]
    while len(nodes):
        depth += 1
        new_layer = []
        for m, f in nodes:
            left = (m, f + m)
            right = (m + f, f)
            if left == (x, y) or right == (x, y):
                return str(depth)
            if left[1] <= y:
                new_layer.append(left)
            if right[0] <= x:
                new_layer.append(right)
        nodes = new_layer
    return "impossible"


def solution3(x, y):
    x = int(x)
    y = int(y)

    depth = -1
    while x > 0 and y > 0:
        if x > y:
            x = x - y
        else:
            y = y - x
        depth += 1

    if x == 1 and y == 0:
        return str(depth)
    return "impossible"


def solution(x, y):
    x = int(x)
    y = int(y)

    depth = -1
    while x > 0 and y > 0:
        if x > y:
            x, y = y, x
        multiples = y // x
        y = y - multiples * x
        depth += multiples

    if x == 1 and y == 0:
        return str(depth)
    return "impossible"


test_cases = [("1", "1"), ("2", "1"), ("4", "7"), ("2", "4"), ("100", "6000")]

for tc in test_cases:
    print(tc, solution(*tc), solution2(*tc))

"""
How does 4,7 work?
1,1
1,2
1,3
4,3
4,7

Two options at each step, so could just search...
And add the results to a lookup. Big lookup though...
Shrink using fact that x and y are symmetrical

why is it failing...
could be time limit
current solution - time O(d), memory O(1)
Previous solution was worse in both respects!

Maybe it's possible I'm getting something wrong?
I don't think so though


"""
