import sys
from collections import defaultdict

infile = sys.argv[1] if len(sys.argv) > 1 else "4.in"
input_data = open(infile).read().strip()
data = input_data.split("\n")


part_1 = 0

part_2 = defaultdict(int)
for i, line in enumerate(data):
    part_2[i] += 1
    temp = 0
    winning, mine = line.split("|")
    game_id, line = winning.split(":")
    winners = line.split()
    mine = mine.split()
    for win in winners:
        if win in mine:
            temp += 1
    if temp > 0:
        part_1 += 2**(temp-1)
    for j in range(temp):
        part_2[i + 1 + j] += part_2[i]





print(part_1)
print(sum(part_2.values()))




