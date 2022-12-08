from pprint import pprint
from typing import List, Dict

input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

with open("input5.txt", "r") as fp:
    input = fp.read()

stacks: Dict[int, List[str]] = {}
setup = True
for line in input.split('\n'):
    print(line)
    if line == '\n' or line == "" or line.startswith(' 1'):
        setup = False
        print("initial:")
        pprint(stacks)
        continue
    if setup:
        for i, j in enumerate(range(0, len(line), 4)):
            stacknum = i + 1
            container = line[j:j+4].strip(' []')
            if container == "":
                continue
            else:
                if stacknum in stacks:
                    stacks[stacknum] = [container] + stacks[stacknum]
                else:
                    stacks[stacknum] = [container]
    else:
        line = line.split(' ')
        crates = int(line[1])
        fromstack = int(line[3])
        tostack = int(line[5])

        movers = stacks[fromstack][-crates:]
        stacks[fromstack] = stacks[fromstack][0:-crates]
        # movers.reverse()
        stacks[tostack].extend(movers)


pprint(stacks)
tops = ""
for i in range(len(stacks)):
    tops += stacks[i+1][-1]

print(tops)