from pathlib import Path
from collections import defaultdict
import re
from collections import Counter


def print_particales(particals, x_size, y_size):
    grid = [["-" for _ in range(x_size)] for _ in range(y_size)]
    for partical in particals:
        x, y, i, j = partical
        grid[y][x] = "X"

    for line in grid:
        print("".join(line))


def part_1():
    x_size = 101
    y_size = 103

    number_of_turns = 7569
    particals = []

    for line in [line for line in Path("input.txt").read_text().strip().splitlines() if line]:
        x, y, i, j = map(int, re.search(r"p=(-?\d+),(-?\d+)\s*v=(-?\d+),(-?\d+)", line).groups())
        particals.append(
            (
                x,
                y,
                i,
                j,
            )
        )

    for turn in range(number_of_turns, number_of_turns + 1):
        q1, q2, q3, q4 = 0, 0, 0, 0

        for p in particals:

            x, y, i, j = p
            x = (x + i * turn) % x_size
            y = (y + j * turn) % y_size

            if x < x_size // 2 and y < y_size // 2:
                q1 += 1
            elif x > x_size // 2 and y < y_size // 2:
                q2 += 1
            elif x < x_size // 2 and y > y_size // 2:
                q3 += 1
            elif x > x_size // 2 and y > y_size // 2:
                q4 += 1
            else:
                pass

        print(turn)
        print(q1 * q2 * q3 * q4)
        print(Counter([(x, y) for x, y, _, _ in particals]))
        # print_particales(particals, x_size, y_size)


if __name__ == "__main__":
    part_1()
    # part_2()
