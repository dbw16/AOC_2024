from pathlib import Path
import numpy as np
import re


def is_int(f: float):
    return f.__round__(2).__floor__() == f.__round__(2) and f >= 0


def part(increment=0):
    blocks = Path("input.txt").read_text().strip().split("\n\n")
    total_cost = 0

    for block in blocks:
        x_a, y_a = map(int, re.search(r"Button A: X\+(\d+), Y\+(\d+)", block).groups())
        x_b, y_b = map(int, re.search(r"Button B: X\+(\d+), Y\+(\d+)", block).groups())
        x_goal, y_goal = map(int, re.search(r"Prize: X=(\d+), Y=(\d+)", block).groups())

        result = np.linalg.solve([[x_a, x_b], [y_a, y_b]], [x_goal + increment, y_goal + increment])
        if is_int(result[0]) and is_int(result[1]):
            total_cost += result[0] * 3 + result[1]

    print(total_cost)
    # 31552


if __name__ == "__main__":
    part()  # 31552.0
    part(10000000000000)  # 95273925552482.0
