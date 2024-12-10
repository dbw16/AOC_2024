# Tue Dec 10 19:13:25 NZDT 2024
# Tue Dec 10 19:35:22 NZDT 2024 part 1
# Tue Dec 10 19:46:12 NZDT 2024 part 2 (seems suss that this was easier?)
from pathlib import Path
from collections import defaultdict


def part_1():
    grid = [[int(y) if y.isdigit() else -1 for y in x] for x in Path("input.txt").read_text().split("\n")]
    coordinate_to_value = {complex(x, y): grid[y][x] for y in range(len(grid)) for x in range(len(grid[0]))}

    value_to_coordinates: dict[int, list[complex]] = defaultdict(list)
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            value_to_coordinates[int(val)].append(complex(x, y))

    directions = [complex(1, 0), complex(-1, 0), complex(0, 1), complex(0, -1)]
    nine_count = 0

    for start_cord in value_to_coordinates[0]:
        cords = [start_cord]
        visited = set()
        while cords:
            cord = cords.pop()
            for direction in directions:
                new_cord = cord + direction
                if coordinate_to_value.get(new_cord, None) == coordinate_to_value[cord] + 1 and new_cord not in visited:

                    cords.append(new_cord)
                    visited.add(new_cord)

                    if coordinate_to_value[new_cord] == 9:
                        nine_count += 1
    print(nine_count)


def part_2():
    grid = [[int(y) if y.isdigit() else -1 for y in x] for x in Path("input.txt").read_text().split("\n")]
    coordinate_to_value = {complex(x, y): grid[y][x] for y in range(len(grid)) for x in range(len(grid[0]))}

    value_to_coordinates: dict[int, list[complex]] = defaultdict(list)
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            value_to_coordinates[int(val)].append(complex(x, y))

    directions = [complex(1, 0), complex(-1, 0), complex(0, 1), complex(0, -1)]
    nine_count = 0

    for start_cord in value_to_coordinates[0]:
        cords = [start_cord]
        while cords:
            cord = cords.pop()
            for direction in directions:
                new_cord = cord + direction
                if coordinate_to_value.get(new_cord, None) == coordinate_to_value[cord] + 1:
                    cords.append(new_cord)

                    if coordinate_to_value[new_cord] == 9:
                        nine_count += 1
    print(nine_count)


if __name__ == "__main__":
    part_1()
    part_2()
