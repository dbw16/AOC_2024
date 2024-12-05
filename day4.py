from pathlib import Path


def part_1() -> None:
    grid = [[y for y in x] for x in Path("input.txt").read_text().split("\n")]
    cordinate_to_value = {complex(x, y): grid[y][x] for y in range(len(grid)) for x in range(len(grid[0]))}

    masks = (
        (0, 1, 2, 3),  # right
        (0, -1, -2, -3),  # left
        (0, 1j, 2j, 3j),  # up
        (0, -1j, -2j, -3j),  # down
        (0, 1 + 1j, 2 + 2j, 3 + 3j),  # dig right up
        (0, -1 + 1j, -2 + 2j, -3 + 3j),  # dig left up
        (0, 1 - 1j, 2 - 2j, 3 - 3j),  # dig right down
        (0, -1 - 1j, -2 - 2j, -3 - 3j),  # dig left down
    )

    total = 0
    for cordinate in cordinate_to_value:
        if cordinate_to_value[cordinate] != "X":
            continue

        for mask in masks:
            word = []
            for offset in (offset for offset in mask if cordinate + offset in cordinate_to_value):
                word.append(cordinate_to_value[cordinate + offset])

            if word == ["X", "M", "A", "S"]:
                total += 1

    print(total)


def part_2() -> None:
    grid = [[y for y in x] for x in Path("input.txt").read_text().split("\n")]
    cordinate_to_value = {complex(x, y): grid[y][x] for y in range(len(grid)) for x in range(len(grid[0]))}

    mask = (-1 - 1j, 1 + 1j, 1 - 1j, -1 + 1j)

    total = 0
    for cordinate in cordinate_to_value:
        if cordinate_to_value[cordinate] != "A":
            continue

        word = []
        for offset in (offset for offset in mask if cordinate + offset in cordinate_to_value):
            word.append(cordinate_to_value[cordinate + offset])

        if word == ["M", "S", "S", "M"] or word == ["S", "M", "M", "S"] or word == ["S", "M", "S", "M"] or word == ["M", "S", "M", "S"]:
            total += 1

    print(total)


if __name__ == "__main__":
    part_2()
