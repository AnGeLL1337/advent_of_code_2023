import sys


def part_1(input_file) -> int:
    input_data = open(input_file).read().strip()
    seeds, *plan = input_data.split("\n\n")

    _, seeds = seeds.split(":")
    seeds = list(map(int, seeds.split()))

    for part in plan:
        intervals = []
        for i in part.split("\n")[1:]:
            intervals.append(list(map(int, i.split())))
        new_seeds = []
        for seed in seeds:
            for dest, source, increment in intervals:
                if source <= seed <= source + increment:
                    new_seeds.append(seed - source + dest)
                    break
            else:
                new_seeds.append(seed)
        seeds = new_seeds

    return min(seeds)


def part_2(input_file) -> int:
    input_data = open(input_file).read().strip()
    tmp, *plan = input_data.split("\n\n")
    _, tmp = tmp.split(":")
    tmp = list(map(int, tmp.split()))
    seeds = []
    for i in range(0, len(tmp) - 1, 2):
        seeds.append((tmp[i], tmp[i] + tmp[i + 1]))


    for part in plan:
        intervals = []
        for i in part.split("\n")[1:]:
            intervals.append(list(map(int, i.split())))
        new_seeds = []
        while seeds:
            start, end = seeds.pop()
            for start_desc, start_source, increment in intervals:
                overlap_start = max(start, start_source)
                overlap_end = min(end, start_source + increment)
                if overlap_start < overlap_end:
                    new_seeds.append(
                        (overlap_start - start_source + start_desc, overlap_end - start_source + start_desc))
                    if overlap_start > start:
                        seeds.append((start, overlap_start))
                    if overlap_end < end:
                        seeds.append((overlap_end, end))
                    break
            else:
                new_seeds.append((start, end))
        seeds = new_seeds

    t = min(seeds, key=lambda x: x[0])

    return t[0]


if __name__ == "__main__":
    file = sys.argv[1] if len(sys.argv) > 1 else "5.in"
    print(part_1(file))
    print(part_2(file))