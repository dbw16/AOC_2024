from pathlib import Path
from typing import Generator
from functools import cache


def generate_prefix_suffix_pairs(pattern: str) -> Generator[tuple[str, str], None, None]:
    return ((pattern[:i], pattern[i:]) for i in range(1, len(pattern) + 1))


@cache
def can_make(towels: set[str], pattern: [str]) -> bool:
    if not pattern:
        return True

    for prefix, suffix in generate_prefix_suffix_pairs(pattern):
        if prefix in towels and can_make(towels, suffix):
            return True

    return False


@cache
def how_many(towels: set[str], pattern: [str]) -> int:
    if not pattern:
        return 1

    count = 0
    for prefix, suffix in generate_prefix_suffix_pairs(pattern):
        if prefix in towels:
            count += how_many(towels, suffix)

    return count


def part_1():
    lines = Path("input.txt").read_text().strip().splitlines()
    towels = frozenset((towel.strip() for towel in lines[0].split(",")))
    patterns = lines[2:]

    print(sum((can_make(towels, pattern) for pattern in patterns)))


def part_2():
    lines = Path("input.txt").read_text().strip().splitlines()
    towels = frozenset((towel.strip() for towel in lines[0].split(",")))
    patterns = lines[2:]

    print(sum((how_many(towels, pattern) for pattern in patterns)))


if __name__ == "__main__":
    part_1()
    part_2()
