input = ['2-4,6-8',
         '2-3,4-5',
         '5-7,7-9',
         '2-8,3-7',
         '6-6,4-6',
         '2-6,4-8',
         ]


input = []
with open("input4.txt", "r") as fp:
    for line in fp:
        input.append(line.strip())

badpairs = 0
for pairing in input:
    # print(pairing)
    l, r = pairing.split(',')
    l1, l2 = [int(x) for x in l.split('-')]
    r1, r2 = [int(x) for x in r.split('-')]

    # if (l1 <= r1 and l2 >= r2) or (l1 >= r1 and l2 <= r2):
    #     badpairs+=1
    #     print("badpair", pairing)
    if l1 <= r1 <= l2 or l1 <= r2 <= l2 or (r1 <= l1 and r2 >= l2):
        badpairs+=1
        print("badpair", pairing)

print(badpairs)