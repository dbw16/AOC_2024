from pathlib import Path
from collections import defaultdict
import itertools

NOTHING = "."


def part_1():
    grid = [[y for y in x] for x in Path("input.txt").read_text().split("\n")]
    cordinate_to_value = {complex(x, y): grid[y][x] for y in range(len(grid)) for x in range(len(grid[0]))}
    cord_to_distsnce_from_end = {}
    masks = [complex(1, 0), complex(-1, 0), complex(0, 1), complex(0, -1)]

    value_to_cordinates: dict[str, complex] = {}
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == NOTHING:
                continue
            value_to_cordinates[val] = complex(x, y)

    start_cord = value_to_cordinates["S"]
    cord = value_to_cordinates["E"]
    cord_to_distsnce_from_end[cord] = 0
    visisted = {cord}
    while cord != start_cord:
        for mask in masks:
            if cordinate_to_value[cord + mask] in ".ES" and cord + mask not in visisted:
                cord_to_distsnce_from_end[cord + mask] = cord_to_distsnce_from_end[cord] + 1
                cord = cord + mask
                visisted.add(cord)

    threshhold = 100
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            cord = complex(x, y)
            if cordinate_to_value[cord] != "#":
                continue
            valid_masks = [mask for mask in masks if cordinate_to_value.get(cord + mask, "/") in ".ES"]

            if len(valid_masks) < 2:
                continue
            elif len(valid_masks) == 2:
                saved_time = abs(cord_to_distsnce_from_end[cord + valid_masks[0]] - cord_to_distsnce_from_end[cord + valid_masks[1]]) - 2
                if saved_time >= threshhold:
                    print(saved_time)
                    count += 1
                continue
            elif len(valid_masks) == 3:
                continue
            else:
                raise

    print(count)

    # print(cord_to_distsnce_from_end[start_cord])


if __name__ == "__main__":
    part_1()
