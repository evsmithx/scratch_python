input = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

with open("input10.txt", "r") as fp:
    input = fp.read()

amounts = [1]
for line in input.split('\n'):
    line = line.strip()
    print(line)
    if line == "":
        continue
    if line.startswith("noop"):
        amounts.append(0)
    else:
        _, a = line.split(' ')
        amounts.append(0)
        amounts.append(int(a))

print(amounts)
print(len(amounts))

total = 0
for i in [20, 60, 100, 140, 180, 220]:
    total += i* sum(amounts[0:i])
    print(sum(amounts[0:i]))

print(total)

# screen is 40 * 6
width = 40
height = 6

position_iter = iter(amounts)
position = next(position_iter)
for i in range(height):
    row = ""
    for j in range(width):
        if position - 1 <= j <= position +1:
            row += "#"
        else:
            row += "."
        position += next(position_iter)
    print(row)

# ZGCJZJFL