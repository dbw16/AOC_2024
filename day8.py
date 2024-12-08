from pathlib import Path
from collections import defaultdict
import itertools

NOTHING = "."


def part_1():
    grid = [[y for y in x] for x in Path("input.txt").read_text().split("\n")]
    cordinate_to_value = {complex(x, y): grid[y][x] for y in range(len(grid)) for x in range(len(grid[0]))}

    value_to_cordinates: dict[str, list[complex]] = defaultdict(list)
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == NOTHING:
                continue
            value_to_cordinates[val].append(complex(x, y))

    node_list = []
    for key, cordinates in value_to_cordinates.items():
        for combination in itertools.combinations(cordinates, 2):
            x_dif = int(combination[0].real - combination[1].real)
            y_dif = int(combination[0].imag - combination[1].imag)
            print(x_dif, y_dif)
            node_1 = combination[0] + complex(x_dif, y_dif)
            node_2 = combination[1] - complex(x_dif, y_dif)

            node_list.append(node_1)
            node_list.append(node_2)
    print(len({node for node in node_list if node in cordinate_to_value}))


def part_2():
    grid = [[y for y in x] for x in Path("input.txt").read_text().split("\n")]
    cordinate_to_value = {complex(x, y): grid[y][x] for y in range(len(grid)) for x in range(len(grid[0]))}

    value_to_cordinates: dict[str, list[complex]] = defaultdict(list)
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == NOTHING:
                continue
            value_to_cordinates[val].append(complex(x, y))

    node_list = []
    for key, cordinates in value_to_cordinates.items():
        for combination in itertools.combinations(cordinates, 2):
            x_dif = int(combination[0].real - combination[1].real)
            y_dif = int(combination[0].imag - combination[1].imag)

            mul = 0
            while True:
                node_1 = combination[0] + complex(x_dif, y_dif) * mul
                if node_1 not in cordinate_to_value:
                    break
                node_list.append(node_1)
                mul += 1

            mul = 0
            while True:
                node_2 = combination[1] - complex(x_dif, y_dif) * mul
                if node_2 not in cordinate_to_value:
                    break
                node_list.append(node_2)
                mul += 1

    print(len({node for node in node_list if node in cordinate_to_value}))


if __name__ == "__main__":
    # I love complex numbers
    part_1()
    part_2()
