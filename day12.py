from pathlib import Path
from collections import defaultdict
from collections import Counter


def part_1():
    grid = [[y for y in x] for x in Path("input.txt").read_text().split("\n")]
    coordinate_to_value = {complex(x, y): grid[y][x] for y in range(len(grid)) for x in range(len(grid[0]))}

    value_to_coordinates: dict[int, list[complex]] = defaultdict(list)
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            value_to_coordinates[val].append(complex(x, y))
    total = 0
    visted = set()

    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            cord = complex(x, y)
            if cord in visted:
                continue

            section_value = coordinate_to_value[cord]
            visted.add(cord)

            local_visited = {cord}
            que = [complex(x, y)]
            p = 0
            a = 1

            while que:
                cord = que.pop()
                for direction in (complex(1, 0), complex(-1, 0), complex(0, 1), complex(0, -1)):
                    if cord + direction in local_visited:
                        continue
                    if cord + direction in coordinate_to_value:
                        if coordinate_to_value[cord + direction] == section_value:
                            a += 1
                            que.append(cord + direction)
                            visted.add(cord + direction)
                            local_visited.add(cord + direction)
                        else:
                            p += 1
                    else:
                        p += 1

            print(section_value, a, p)
            total += a * p
    print(total)


def solve_number_of_sides(fences: Counter[complex]) -> int:
    sides_count = 0
    while fences:
        _fence = list(fences.keys())[0]
        fences[_fence] -= 1
        if fences[_fence] <= 0:
            fences.pop(_fence)
        moved_left_right = False

        visited = set()
        search_left_and_right = [_fence]
        while search_left_and_right:
            fence = search_left_and_right.pop()
            visited.add(fence)
            for x in range(-10, 10, 1):
                direction = complex(x, 0)
                if fence + direction in fences and fence + direction not in visited:
                    moved_left_right = True
                    fences[fence + direction] -= 1
                    search_left_and_right.append(fence + direction)
                    if fences[fence + direction] <= 0:
                        fences.pop(fence + direction)
        if moved_left_right:
            sides_count += 1
            continue

        moved_up_down = False
        search_up_and_down = [_fence]
        while search_up_and_down:
            fence = search_up_and_down.pop()
            visited.add(fence)
            for y in range(-10, 10, 1):
                direction = complex(0, y)
                if fence + direction in fences and fence + direction not in visited:
                    moved_up_down = True
                    fences[fence + direction] -= 1
                    search_up_and_down.append(fence + direction)
                    if fences[fence + direction] <= 0:
                        fences.pop(fence + direction)
        if moved_up_down:
            sides_count += 1
            continue

        sides_count += 1
    return sides_count


def part_2():
    grid = [[y for y in x] for x in Path("input.txt").read_text().split("\n")]
    coordinate_to_value = {complex(x, y): grid[y][x] for y in range(len(grid)) for x in range(len(grid[0]))}

    value_to_coordinates: dict[int, list[complex]] = defaultdict(list)
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            value_to_coordinates[val].append(complex(x, y))
    total = 0
    visted = set()

    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            cord = complex(x, y)
            if cord in visted:
                continue

            section_value = coordinate_to_value[cord]
            visted.add(cord)

            local_visited = {cord}
            que = [complex(x, y)]
            p = Counter()
            a = 1
            while que:
                cord = que.pop()
                for direction in (complex(1, 0), complex(-1, 0), complex(0, 1), complex(0, -1)):
                    if cord + direction in local_visited:
                        continue
                    if cord + direction in coordinate_to_value:
                        if coordinate_to_value[cord + direction] == section_value:
                            a += 1
                            que.append(cord + direction)
                            visted.add(cord + direction)
                            local_visited.add(cord + direction)
                        else:
                            p[cord + direction] += 1
                    else:
                        p[cord + direction] += 1
            sides = solve_number_of_sides(p)
            print(section_value, a, sides)
            total += a * sides
            print(total)
    print(total)


if __name__ == "__main__":
    part_2()
    # 821216 to low
    # 834828 is correct
