# Wed Dec 11 19:22:16 NZDT 2024
# Wed Dec 11 19:32:5 NZDT 2024 part 1 done
# Wed Dec 11 20:21:48 NZDT 2024 part 2 and 2 glasses of wine

# part 2 is going to take some thinking...
import itertools
import operator
from pathlib import Path
import functools
from collections import Counter


def split_stone(stone: int) -> tuple[int, int]:
    s_stone = str(stone)
    int(s_stone[: int(len(s_stone) / 2)]), int(s_stone[int(len(s_stone) / 2) :])


def part_1():
    stones = [int(x) for x in Path("input.txt").read_text().strip().split()]
    number_of_blinks = 25
    print("start")
    print(stones)
    for i in range(number_of_blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                new_stones.extend(split_stone(stone))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
        print(f"blinks: {i + 1}")
        print(len(stones))


def part_2():
    # it does not really matter the order of the stones
    # and result([x, x, x]) = result([x]) * 3
    stones = [int(x) for x in Path("input.txt").read_text().strip().split()]
    number_of_blinks = 75

    def rule(stone: int) -> tuple[int, int | None]:
        if stone == 0:
            return (1, None)
        elif len(str(stone)) % 2 == 0:
            s_stone = str(stone)
            return int(s_stone[: int(len(s_stone) / 2)]), int(s_stone[int(len(s_stone) / 2) :])
        else:
            return (stone * 2024, None)

    stone_count = Counter(stones)
    for _ in range(number_of_blinks):
        new_stone_count = Counter()
        for stone in stone_count:
            new_stone_a, new_stone_b = rule(stone)
            new_stone_count[new_stone_a] += stone_count[stone]  # we get one of these for each stone of value x
            if new_stone_b is not None:
                new_stone_count[new_stone_b] += stone_count[stone]
        stone_count = new_stone_count
    print(len(stone_count))
    print(sum((count_value for count_value in stone_count.values())))


if __name__ == "__main__":
    # part_1()
    part_2()
#     4329 385 0 1444386 600463 19 1 56615
