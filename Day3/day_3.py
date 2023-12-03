import string
import sys
from collections import defaultdict
def get_neighbors(grid, i,j, indices=False, default=None):
    neigh = []
    rows = len(grid)
    cols = len(grid[0])

    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if 0 <= x < rows and 0 <= y < cols and (x != i or y != j):
                if indices:
                    neigh.append((x, y))
                else:
                    neigh.append(grid[x][y])
            elif default is not None:
                neigh.append(default)

    return neigh


def check_neighbors_2d(grid, start, end, row):
    neighbors = set()
    rows = len(grid)
    columns = len(grid[0])

    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, start - 1), min(columns, end + 2)):
            if is_valid(i, j, rows, columns):
                if grid[i][j] == "." or grid[i][j].isdigit():
                    continue
                neighbors.add(grid[i][j])
            elif j < start or j > end or i == row:
                continue

            if grid[i][j] == ".": continue
            neighbors.add(grid[i][j])

    return neighbors


def check_neighbors_gears(grid, start, end, row):
    neighbors = set()
    rows = len(grid)
    columns = len(grid[0])

    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, start - 1), min(columns, end + 2)):
            if is_valid(i, j, rows, columns):
                if grid[i][j] == "." or grid[i][j].isdigit() or grid[i][j] != "*":
                    continue
            elif j < start or j > end or i == row:
                continue

            if grid[i][j] != "*":
                continue
            neighbors.add((i, j))

    return neighbors


def is_valid(row, col, max_row, max_col):
    return 0 <= row < max_row and 0 <= col < max_col

def get_numbers(grid, indices=False):
    import re

    numbers_info = []

    for i in range(len(grid)):
        line = ''.join(grid[i])

        for match in re.finditer(r"\d+", line):
            start, end = match.start(), match.end()
            number = match.group()
            if indices:
                numbers_info.append(((i, start), (i, end - 1)))

            else :
                numbers_info.append(int(number))

    return numbers_info

def part_1(grid):
    part_1 :int = 0
    rows = len(grid)
    cols = len(grid[0])

    numbers = get_numbers(grid, indices=True)

    for i in range(rows):
        digits_starts = False
        cislo = ""
        start = 0
        for j in range(cols):
            if grid[i][j].isdigit() and not digits_starts:
                digits_starts = True
                start = j
            elif digits_starts and (not grid[i][j].isdigit() or (grid[i][j].isdigit() and j == cols - 1)):
                end = j - 1
                if j == cols - 1 and grid[i][j].isdigit():
                    end = j
                digits_starts = False
                susedia = check_neighbors_2d(grid, start, end, i)
                if(len(susedia) >= 1):
                    for x in range(start, end + 1):
                        cislo += grid[i][x]

                if(cislo == ""):
                    continue
                part_1 += int(cislo)
                cislo = ""

    return part_1


def part_2(grid):
    cislo: string = ""
    dic = defaultdict(list)
    part_2: int = 0
    rows = len(grid)
    cols = len(grid[0])
    gears = []

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "*":
                gears.append((i, j))

    for i in range(rows):
        digits_starts = False
        for j in range(cols):
            if grid[i][j].isdigit() and not digits_starts:
                digits_starts = True
                start = j
            elif digits_starts and (not grid[i][j].isdigit() or (grid[i][j].isdigit() and j == cols - 1)):
                end = j - 1
                if j == cols - 1 and grid[i][j].isdigit():
                    end = j
                digits_starts = False
                check_gears = check_neighbors_gears(grid, start, end, i)
                if len(check_gears) > 0:
                    for x in range(start, end + 1):
                        cislo += grid[i][x]
                    dic[tuple(check_gears)].append(int(cislo))
                    cislo = ""


    for key, value in dic.items():
        if len(value) == 2:
            part_2 += value[0] * value[1]
    return part_2


if __name__ == "__main__":
    infile = sys.argv[1] if len(sys.argv) > 1 else "3.in"
    input_data = open(infile).read().strip()

    grid = []

    for line in input_data.split("\n"):
        grid.append(list(line))

    print(part_1(grid))
    print(part_2(grid))
