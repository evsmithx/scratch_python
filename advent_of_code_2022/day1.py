cals_list = []
with open("input1.txt", "r") as fp:
    cals = 0
    for line in fp:
        line = line.strip()
        if line == "":
            cals_list.append(cals)
            cals = 0
        else:
            cals += int(line)

print(max(cals_list))
cals_list.sort()
print(cals_list[-3:])
print(sum(cals_list[-3:]))