from pathlib import Path
import re


def part_1(line: str = ""):
    if not line:
        line = Path("input.txt").read_text().strip()
    matches = re.findall(pattern=r"mul\([0-9]{1,3},[0-9]{1,3}\)", string=line)
    [print(match) for match in matches]

    total = 0
    for match in matches:
        a = int(match.split("(")[1].split(",")[0])
        b = int(match.split(",")[1].split(")")[0])
        total += a * b
    print(total)


def part_2():
    line = Path("input.txt").read_text().strip()

    semi_processed_blocks = line.split("don't()")
    blocks = [semi_processed_blocks[0]]
    for block in semi_processed_blocks[1:]:
        split = block.split("do()")
        if len(split) != 1:
            blocks.append("".join(split[1:]))
    part_1("".join(blocks))


if __name__ == "__main__":
    part_2()
