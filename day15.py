# maybe someday i will clean this up (he lied to him self...)
from pathlib import Path
from collections import defaultdict
from collections import Counter

ROBOT = "@"


def print_grid(coordinate_to_value: dict[complex, str], x_len: int, y_len: int):
    for j in range(y_len):
        for i in range(x_len):
            print(coordinate_to_value[complex(i, j)], end="")
        print("")


def part_1():
    grid, directions = Path("input.txt").read_text().strip().split("\n\n")
    directions = "".join(directions.splitlines())
    direction_to_mask = {">": complex(1), "<": complex(-1), "^": complex(0, -1), "v": complex(0, 1)}
    grid = [[y for y in x] for x in grid.split("\n")]
    x_len, y_len = len(grid[0]), len(grid)
    coordinate_to_value = {complex(x, y): grid[y][x] for y in range(len(grid)) for x in range(len(grid[0]))}

    value_to_coordinates: dict[int, complex] = {}
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            value_to_coordinates[val] = complex(x, y)

    robot_cord = value_to_coordinates[ROBOT]

    for direction in directions:
        # print_grid(coordinate_to_value, x_len, y_len)
        new_cord = robot_cord + direction_to_mask[direction]

        if coordinate_to_value[new_cord] == ".":
            coordinate_to_value[new_cord] = "@"
            coordinate_to_value[robot_cord] = "."
            robot_cord = new_cord
            continue
        elif coordinate_to_value[new_cord] == "#":
            continue
        elif coordinate_to_value[new_cord] == "O":
            n = 1
            free_space = False
            while True:
                if coordinate_to_value[new_cord + direction_to_mask[direction] * n] == ".":
                    free_space = True
                    break
                elif coordinate_to_value[new_cord + direction_to_mask[direction] * n] == "O":
                    n = n + 1
                elif coordinate_to_value[new_cord + direction_to_mask[direction] * n] == "#":
                    break

            if free_space:
                coordinate_to_value[new_cord] = "@"
                coordinate_to_value[robot_cord] = "."
                robot_cord = new_cord
                coordinate_to_value[new_cord + direction_to_mask[direction] * n] = "O"

    print_grid(coordinate_to_value, x_len, y_len)
    score = 0
    for j in range(y_len):
        for i in range(x_len):
            if coordinate_to_value[complex(i, j)] == "O":
                score += i
                score += j * 100
    print(score)


def part_2():
    grid, directions = Path("input.txt").read_text().strip().replace(".", "..").replace("@", "@.").replace("#", "##").replace("O", "[]").split("\n\n")
    directions = "".join(directions.splitlines())
    direction_to_mask = {">": complex(1), "<": complex(-1), "^": complex(0, -1), "v": complex(0, 1)}
    grid = [[y for y in x] for x in grid.split("\n")]
    x_len, y_len = len(grid[0]), len(grid)
    coordinate_to_value = {complex(x, y): grid[y][x] for y in range(len(grid)) for x in range(len(grid[0]))}

    print_grid(coordinate_to_value, x_len, y_len)

    value_to_coordinates: dict[int, complex] = {}
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            value_to_coordinates[val] = complex(x, y)

    robot_cord = value_to_coordinates[ROBOT]

    for d_n, direction in enumerate(directions):
        print(d_n)
        print_grid(coordinate_to_value, x_len, y_len)
        new_cord = robot_cord + direction_to_mask[direction]

        if coordinate_to_value[new_cord] == ".":
            coordinate_to_value[new_cord] = "@"
            coordinate_to_value[robot_cord] = "."
            robot_cord = new_cord
            continue
        elif coordinate_to_value[new_cord] == "#":
            continue
        elif coordinate_to_value[new_cord] in {"[", "]"}:
            n = 1
            free_space = False
            if direction in {"<", ">"}:
                while True:
                    if coordinate_to_value[new_cord + direction_to_mask[direction] * n] == ".":
                        free_space = True
                        break
                    elif coordinate_to_value[new_cord + direction_to_mask[direction] * n] in {"[", "]"}:
                        n = n + 1
                    elif coordinate_to_value[new_cord + direction_to_mask[direction] * n] == "#":
                        break

                if free_space:
                    for i in range(n):
                        if direction == "<":
                            if i % 2 == 0:
                                coordinate_to_value[new_cord + direction_to_mask[direction] * (i + 1)] = "]"
                            else:
                                coordinate_to_value[new_cord + direction_to_mask[direction] * (i + 1)] = "["
                        else:
                            if i % 2 == 0:
                                coordinate_to_value[new_cord + direction_to_mask[direction] * (i + 1)] = "["
                            else:
                                coordinate_to_value[new_cord + direction_to_mask[direction] * (i + 1)] = "]"
                    coordinate_to_value[new_cord] = "@"
                    coordinate_to_value[robot_cord] = "."
                    robot_cord = new_cord
            elif direction in {"^", "v"}:
                n = 1
                free_space = True

                cords_need_shifting = []
                cords_to_checked = {robot_cord}

                while cords_to_checked:
                    box = cords_to_checked.pop()
                    cords_need_shifting.append(box)
                    if coordinate_to_value[box + direction_to_mask[direction]] == ".":
                        continue
                    elif coordinate_to_value[box + direction_to_mask[direction]] == "#":
                        free_space = False
                        break
                    elif coordinate_to_value[box + direction_to_mask[direction]] in {"[", "]"}:
                        if coordinate_to_value[box + direction_to_mask[direction]] == "[":
                            cords_to_checked.add(box + direction_to_mask[direction])
                            cords_to_checked.add(box + direction_to_mask[direction] + complex(1, 0))
                        else:
                            cords_to_checked.add(box + direction_to_mask[direction])
                            cords_to_checked.add(box + direction_to_mask[direction] + complex(-1, 0))
                    # elif coordinate_to_value[new_cord + direction_to_mask[direction] * n] == "#":
                    else:
                        raise Exception()

                if free_space:
                    coordinate_to_value_new = coordinate_to_value.copy()
                    touched_cords = set()
                    for cord in reversed(cords_need_shifting):
                        coordinate_to_value_new[cord + direction_to_mask[direction]] = coordinate_to_value[cord]
                        # print_grid(coordinate_to_value_new, x_len, y_len)
                        if coordinate_to_value_new[cord + direction_to_mask[direction]] == "@":
                            robot_cord = cord + direction_to_mask[direction]

                        if cord not in touched_cords:
                            coordinate_to_value_new[cord] = "."
                            touched_cords.add(cord)
                        # print_grid(coordinate_to_value_new, x_len, y_len)

                    coordinate_to_value = coordinate_to_value_new

    print_grid(coordinate_to_value, x_len, y_len)
    score = 0
    for j in range(y_len):
        for i in range(x_len):
            if coordinate_to_value[complex(i, j)] == "[":
                score += i
                score += j * 100
    print(score)


if __name__ == "__main__":
    part_2()
