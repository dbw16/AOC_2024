from pathlib import Path
from itertools import cycle


GUARD = "^"
UP = "u"
RIGHT = "r"
DOWN = "d"
LEFT = "l"
BLOCKED = "#"


def find_guard(grid) -> tuple[int, int]:
    for y, line in enumerate(grid):
        for x, value in enumerate(line):
            if value == GUARD:
                return x, y


def print_grid(grid) -> None:
    for line in grid:
        print(line)
    print("")


def part_1_a(grid) -> None:

    guard_cords = find_guard(grid)
    cords_walked: set[tuple[int, int, str]] = {(guard_cords[0], guard_cords[1], UP)}
    guard_directions = cycle([UP, RIGHT, DOWN, LEFT])
    guard_direction = next(guard_directions)

    while True:
        # print(len(cords_walked), guard_cords)
        try:
            if guard_cords[0] <= 0 or guard_cords[1] <= 0:
                raise IndexError
            # print_grid(grid)
            if guard_direction == UP:
                if grid[guard_cords[1] - 1][guard_cords[0]] == BLOCKED:
                    guard_direction = next(guard_directions)
                    continue
                else:
                    guard_cords = guard_cords[0], guard_cords[1] - 1
                    grid[guard_cords[1]][guard_cords[0]] = "^"
                    if (guard_cords[0], guard_cords[1], guard_direction) in cords_walked:
                        return -1
                    cords_walked.add((guard_cords[0], guard_cords[1], guard_direction))

            if guard_direction == DOWN:
                if grid[guard_cords[1] + 1][guard_cords[0]] == BLOCKED:
                    guard_direction = next(guard_directions)
                    continue
                else:
                    guard_cords = guard_cords[0], guard_cords[1] + 1
                    grid[guard_cords[1]][guard_cords[0]] = "^"
                    if (guard_cords[0], guard_cords[1], guard_direction) in cords_walked:
                        return -1
                    cords_walked.add((guard_cords[0], guard_cords[1], guard_direction))

            if guard_direction == RIGHT:
                if grid[guard_cords[1]][guard_cords[0] + 1] == BLOCKED:
                    guard_direction = next(guard_directions)
                    continue
                else:
                    guard_cords = guard_cords[0] + 1, guard_cords[1]
                    grid[guard_cords[1]][guard_cords[0]] = "^"
                    if (guard_cords[0], guard_cords[1], guard_direction) in cords_walked:
                        return -1
                    cords_walked.add((guard_cords[0], guard_cords[1], guard_direction))

            if guard_direction == LEFT:
                if grid[guard_cords[1]][guard_cords[0] - 1] == BLOCKED:
                    guard_direction = next(guard_directions)
                    continue
                else:
                    guard_cords = guard_cords[0] - 1, guard_cords[1]
                    grid[guard_cords[1]][guard_cords[0]] = "^"
                    if (guard_cords[0], guard_cords[1], guard_direction) in cords_walked:
                        return -1
                    cords_walked.add((guard_cords[0], guard_cords[1], guard_direction))
        except IndexError:
            return len(cords_walked)


def part_1():
    grid = [[y for y in x] for x in Path("input.txt").read_text().split("\n")]
    print(part_1_a(grid))


def part_2():
    grid = [[y for y in x] for x in Path("input.txt").read_text().split("\n")]
    guard_cords = find_guard(grid)
    count = 0
    for y, row in enumerate(grid):
        for x, slot in enumerate(row):
            grid = [[y for y in x] for x in Path("input.txt").read_text().split("\n")]
            print(x, y)
            if guard_cords == (x, y):
                print(f"skipping {guard_cords}")
                continue
            grid[y][x] = "#"
            if part_1_a(grid) == -1:
                count += 1
    print(count)


if __name__ == "__main__":
    part_2()
