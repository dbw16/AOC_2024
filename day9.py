# start Mon Dec  9 18:21:34 NZDT 2024
# part 1 done at Mon Dec  9 18:45:37 NZDT 2024
from pathlib import Path
from collections import Counter


def part_1_solver(_input: str) -> list[int | str]:
    expaneded = []
    for i in range(len(_input)):
        if i % 2 == 0:
            expaneded.extend([int(i / 2)] * int(_input[i]))
        else:
            expaneded.extend(["."] * int(_input[i]))

    next_free_slot_index = 0
    for back_index in range(len(expaneded) - 1, -1, -1):
        if expaneded[back_index] == ".":
            continue

        while expaneded[next_free_slot_index] != ".":
            next_free_slot_index += 1

            if next_free_slot_index == back_index:
                return expaneded

        expaneded[next_free_slot_index] = expaneded[back_index]
        expaneded[back_index] = "."


def part_1() -> None:
    line = Path("input.txt").read_text().strip()
    solved = part_1_solver(line)
    print(sum([value * n for n, value in enumerate(solved) if value != "."]))


def part_2() -> None:
    _input = Path("input.txt").read_text().strip()
    expaneded = []
    for i in range(len(_input)):
        if i % 2 == 0:
            expaneded.extend([int(i / 2)] * int(_input[i]))
        else:
            expaneded.extend(["."] * int(_input[i]))
    id_to_file_len = Counter(expaneded)
    back_index = len(expaneded) - 1
    already_moved = set()
    while back_index >= 0:
        if back_index % 1000 == 0:
            print(back_index)
        if expaneded[back_index] == "." or expaneded[back_index] in already_moved:
            back_index -= 1
            continue

        start_index = 0
        end_index = 0
        take_action = True
        while True:
            if end_index - start_index >= id_to_file_len[expaneded[back_index]]:
                break

            if (
                end_index >= len(expaneded) or end_index == back_index - id_to_file_len[expaneded[back_index]] + 1
            ):  # This plus 1 cost me 45 mins of my life...
                back_index = back_index - id_to_file_len[expaneded[back_index]]
                take_action = False
                break

            if expaneded[start_index] != ".":
                start_index += 1
                end_index = start_index
                continue

            if expaneded[end_index] == ".":
                end_index += 1
            else:
                start_index = end_index

        if take_action:
            already_moved.add(expaneded[back_index])
            for index in range(start_index, end_index):
                expaneded[index] = expaneded[back_index]

            for index in range(back_index - id_to_file_len[expaneded[back_index]] + 1, back_index + 1):
                expaneded[index] = "."

    Path("out.txt").write_text("".join((str(x) for x in expaneded)))

    print(sum([value * n for n, value in enumerate(expaneded) if value != "."]))


if __name__ == "__main__":
    part_2()
