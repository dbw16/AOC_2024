from pathlib import Path

from operator import mul, add
import itertools
from math import log10


def concatenation(a: int, b: int) -> int:
    return (a * 10 ** ((log10(b).__floor__()) + 1)) + b  # maths is hard... is this faster I wounder... 12.23s
    # return int(str(a) + str(b))  # 16.95s yes maths is faster


def part() -> None:
    lines = Path("input.txt").read_text().strip().splitlines()

    total = 0
    # OPERATORS = [mul, add]  # part 1
    OPERATORS = [mul, add, concatenation]
    itertools.permutations(OPERATORS)

    for line in lines:
        target = float(line.split(":")[0].strip())  # slightly faster as floats
        numbers = [float(number) for number in line.split(":")[1].strip().split(" ")]

        operators_list = tuple(itertools.product(OPERATORS, repeat=len(numbers) - 1))

        for operators in operators_list:
            current_value = numbers[0]

            for number, operator in zip(numbers[1:], operators):
                current_value = operator(current_value, number)
            if current_value > target:  # since we are never getting smaller... this and pypy now are at 2.30s
                break
            elif current_value == target:
                total += current_value
                break

    print(int(total))


if __name__ == "__main__":
    part()
