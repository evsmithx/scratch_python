"""
solution(4) returns 2: 4 -> 2 -> 1
solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

14 7 6 3 2 1
"""


def solution(n):
    n = int(n)
    counter = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
            counter += 1
        elif n == 3:
            n -= 1
            n /= 2
            counter += 2
        else:
            # better to move n towards a multiple of 4
            if (n+1) % 4 == 0:
                n += 1
                n /= 4
                counter += 3
            else:
                n -= 1
                n /= 4
                counter += 3
    return counter


previous = 0
for i in range(1,10000):
    new = solution(str(i))
    if abs(new - previous) > 1:
        print(i, new, previous)
        print("error")
        break
    previous = new

print(solution("15"))
print(solution("400"))
