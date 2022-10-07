def solution(l):
    pairs = {}
    for i, x in enumerate(l):
        for j, y in enumerate(l[0:i]):
            if x % y == 0:
                if j in pairs:
                    pairs[j].append(i)
                else:
                    pairs[j] = [i]
    triples = 0
    for l2s in pairs.values():
        for l2 in l2s:
            if l2 in pairs:
                triples += len(pairs[l2])
    return triples


print(solution([1, 1, 1]))
print(solution([1, 2, 3, 4, 5, 6]))
# print(solution([1, 1, 1]))


