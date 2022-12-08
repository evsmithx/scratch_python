from pprint import pprint

strategy = []
with open("input2.txt", "r") as fp:
    for line in fp:
        strategy.append(line.strip())

# strategy = ['A Y',
#             'B X',
#             'C Z']

#A for Rock, B for Paper, and C for Scissors
#X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
#1 for Rock, 2 for Paper, and 3 for Scissors
pprint(strategy)

score = {
    'A X': 3+0,
    'A Y': 1+3,
    'A Z': 2+6,
    'B X': 1+0,
    'B Y': 2+3,
    'B Z': 3+6,
    'C X': 2+0,
    'C Y': 3+3,
    'C Z': 1+6,
}

total = 0
for game in strategy:
    total += score[game]

print(total)