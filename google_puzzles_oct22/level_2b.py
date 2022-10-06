"""
the remainders
L may have 9 digits
ugh, go simple and then improve
123456789

add the numbers to see if they divisible by

"""


def solution(l):
    sorted_l = sorted(l, reverse=True)
    modulos = [x % 3 for x in sorted_l]
    # if sum(modulos) % 3 == 0 we're already sorted
    if sum(modulos) % 3 == 1:
        if 1 in modulos:
            # remove item with modulo 1
            to_remove = [i for i, x in enumerate(modulos) if x == 1]
            sorted_l.pop(to_remove[-1])
        else:
            # remove two 2s instead
            to_remove = [i for i, x in enumerate(modulos) if x == 2]
            sorted_l.pop(to_remove[-1])
            sorted_l.pop(to_remove[-2])

    elif sum(modulos) % 3 == 2:
        if 2 in modulos:
            # remove item with modulo 2
            to_remove = [i for i, x in enumerate(modulos) if x == 2]
            sorted_l.pop(to_remove[-1])
        else:
            # remove two 1s instead
            to_remove = [i for i, x in enumerate(modulos) if x == 1]
            sorted_l.pop(to_remove[-1])
            sorted_l.pop(to_remove[-2])

    if len(sorted_l) == 0:
        return 0
    result = ""
    for x in sorted_l:
        result += str(x)
    return int(result)


print(solution([3, 1, 4, 1]))
print(solution([3, 1, 4, 1, 5, 9]))
print(solution([3, 1, 4, 1, 5, 9, 1]))
print(solution([3, 1, 4, 1, 5, 9, 2]))
print(solution([3, 1, 4, 1, 5, 9, 3]))
print(solution([3, 1, 4, 1, 5, 9, 4]))