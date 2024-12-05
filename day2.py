from pathlib import Path


def safe_1(report: list[int]) -> bool:
    increasing = report[1] > report[0]
    for a, b in zip(report, report[1:]):
        if increasing and a > b:
            return False
        if not increasing and a < b:
            return False
        if not 1 <= abs(a - b) <= 3:
            return False
    return True


def safe_2(report: list[int], buffer: bool = False) -> bool:
    for index, (a, b) in enumerate(zip(report, report[1:])):
        if a > b or not 1 <= abs(a - b) <= 3:
            if buffer:
                return False
            return safe_2(report[:index] + report[index + 1 :], True) or safe_2(report[: index + 1] + report[index + 2 :], True)
    return True


def part_1() -> None:
    lines = Path("input.txt").read_text().splitlines()
    safe_count = 0
    for line in lines:
        report = [int(a) for a in line.split(" ")]
        if not safe_1(report):
            continue
        safe_count += 1
    print(safe_count)


def part_2() -> None:
    lines = Path("input.txt").read_text().splitlines()
    safe_count = 0
    for line in lines:
        report = [int(a) for a in line.split(" ")]
        if safe_2(report) or safe_2(report[::-1]):
            print(f"{report} is safe")
            safe_count += 1
    print(safe_count)


if __name__ == "__main__":
    # part_1()
    part_2()
