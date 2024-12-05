from pathlib import Path
from collections import Counter


def get_sorted_lists(lines: list[str]) -> tuple[list[int], list[int]]:
    return sorted((int(line.split(" ")[0]) for line in lines if line)), sorted((int(line.split(" ")[-1]) for line in lines if line))


def part_1() -> None:
    lines = Path("input.txt").read_text().splitlines()
    list_1, list_2 = get_sorted_lists(lines)
    total_diff = sum((abs(a - b) for a, b in zip(list_1, list_2)))
    print(total_diff)


def part_2() -> None:
    lines = Path("input.txt").read_text().splitlines()
    list_1, list_2 = get_sorted_lists(lines)
    count = Counter(list_2)
    total_relative_diff = sum((a * count[a] for a in list_1))
    print(total_relative_diff)


if __name__ == "__main__":
    part_1()
    part_2()
