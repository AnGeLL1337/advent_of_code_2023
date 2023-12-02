import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "2.in"
input_data = open(infile).read().strip()

part_1 = 0
part_2 = 0
Max = {"red": 12, "green": 13, "blue": 14}


for line in input_data.split("\n"):
    suit = True
    temp = {"red": 0, "green": 0, "blue": 0}
    game_id, line = line.split(":")
    for event in line.split(";"):
        for balls in event.split(","):
            num, color = balls.split()
            num = max(int(num), temp[color])
            temp[color] = num
            if num > Max[color]:
                suit = False

    part_2_temp = 1
    for value in temp.values():
        part_2_temp *= value
    part_2 += part_2_temp

    if suit:
        part_1 += int(game_id.split()[-1])

print(part_1)
print(part_2)


