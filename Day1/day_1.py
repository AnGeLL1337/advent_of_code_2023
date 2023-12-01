import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "1.in"
input_data = open(infile).read().strip()


def part_1(data) -> None:
    temp = 0
    for line in data.split("\n"):
        nums = ""
        for char in line:
            if char.isdigit():
                nums += char
                break
        for char in reversed(line):
            if char.isdigit():
                nums += char
                break
        temp += int(nums)

    print(temp)


def part_2(data) -> None:
    result = 0
    for line in data.split("\n"):
        temp = []
        for i, char in enumerate(line):
            if char.isdigit():
                temp.append(char)
            for j, val in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
                if line[i:].startswith(val):
                    temp.append(str(j+1))
        result += int(temp[0] + temp[-1])

    print(result)


if __name__ == "__main__":
    part_1(input_data)
    part_2(input_data)


