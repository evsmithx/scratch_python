def get_parent(minnode, maxnode, node, prevmax):
    if node == maxnode:
        return prevmax
    halfway = minnode + (maxnode - minnode) / 2 - 1
    if node > halfway:
        return get_parent(halfway + 1, maxnode - 1, node, maxnode)
    else:
        return get_parent(minnode, halfway, node, maxnode)


def solution(h, q):
    # Your code here
    output = [int(get_parent(1, 2**h-1, x, -1)) for x in q]
    return output


print(solution(3, [1, 2, 3, 4, 5, 6, 7]))
print(solution(3, [7, 3, 5, 1]))
print(solution(5, [19, 14, 28]))

"""
need to make these trees
nodes in tree of height n = 2^0 + 2^1 + ... + 2^n-1
== 2^n - 1
 
1   2
3   4
7   8
15  16
31  32
63  64
127


15                  
7         14              
3   6     10   13       
1 2 4 5   8 9  11 12     

h is max 30
that is a lot of nodes haha

can work out which side of the tree...

15
7
gt
offset = 7

head = 15, tail = 1
head = 14, tail = 8
head = 10, tail = 8



"""
