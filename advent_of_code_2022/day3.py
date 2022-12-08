import string

# bags = ['vJrwpWtwJgWrhcsFMMfFFhFp',
#         'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
#         'PmmdzqPrVvPwwTWBwg',
#         'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
#         'ttgJtRGJQctTZtZT',
#         'CrZsJsPPZsGzwwsLwLmpwMDw']

bags = []
with open("input3.txt", "r") as fp:
    for line in fp:
        bags.append(line.strip())

alphalookup = {x: i for i, x in enumerate(string.ascii_letters)}
def get_histo(bag: str):
    histo = [0] * 52
    for x in bag:
        histo[alphalookup[x]] +=1
    print(histo)
    return histo

# total = 0
# for bag in bags:
#     top = bag[0:len(bag)//2]
#     bottom = bag[len(bag)//2:]
#     mistake = [y!=0 and x!=0 for x, y in zip(get_histo(top), get_histo(bottom))].index(True)
#     print(mistake, string.ascii_letters[mistake])
#     total += mistake+1
# print(total)

bagiter = iter(bags)

total = 0
while True:
    try:
        bag1 = next(bagiter)
        bag2 = next(bagiter)
        bag3 = next(bagiter)

        hist1 = get_histo(bag1)
        hist2 = get_histo(bag2)
        hist3 = get_histo(bag3)

        common = [x!=0 and y!=0 and z!=0 for x, y, z in zip(hist1, hist2, hist3)].index(True)
        print(common)
        total += common+1
    except StopIteration:
        break
print(total)