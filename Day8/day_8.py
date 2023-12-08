import math
import sys
from collections import defaultdict
from itertools import cycle


def part_1(input_file) -> int:
    part1 = 0
    dic = defaultdict(tuple)
    input_data = open(input_file).read().strip()
    instructions, plan = input_data.split("\n\n")
    instructions = [x for x in instructions]

    for i, line in enumerate(plan.split("\n")):
        key, values = line.split(" = ")
        key = key[-3:]
        values = tuple(map(str.strip, values.strip("()").split(",")))
        dic[key] = values

    curr = "AAA"
    for i, d in enumerate(cycle(instructions), start=1):
        if d == "L":
            curr = dic[curr][0]
        elif d == "R":
            curr = dic[curr][1]
        if curr == "ZZZ":
            return i

def part_2(input_file) -> int:
    part2 = []
    curr = []
    dic = defaultdict(tuple)
    input_data = open(input_file).read().strip()
    instructions, plan = input_data.split("\n\n")
    instructions = [x for x in instructions]

    for i, line in enumerate(plan.split("\n")):
        key, values = line.split(" = ")
        key = key[-3:]
        values = tuple(map(str.strip, values.strip("()").split(",")))
        dic[key] = values

    for dst in dic.keys():
        if dst.endswith("A"):
            curr.append(dst)

    for dst in curr:
        print(dst)
        for i, d in enumerate(cycle(instructions), start=1):
            if d == "L":
                dst = dic[dst][0]
            elif d == "R":
                dst = dic[dst][1]
            if dst.endswith("Z"):
                part2.append(i)
                break

    return math.lcm(*part2)


if __name__ == "__main__":
    file = sys.argv[1] if len(sys.argv) > 1 else "8.in"
    #print(part_1(file))
    print(part_2(file))