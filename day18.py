from pathlib import Path
from collections import deque
import bisect


def part_1() -> int:
    block_cords = [complex(int(line.split(",")[0]), int(line.split(",")[1])) for line in Path("input.txt").read_text().strip().splitlines()][:1024]
    size = 70
    start = complex(0, 0)
    end = complex(size, size)
    to_visit = deque([(start, 0)])
    visited = set()
    while to_visit:
        current_cord, current_steps = to_visit.popleft()
        masks = [complex(1, 0), complex(-1, 0), complex(0, -1), complex(0, 1)]
        if current_cord == end:
            return current_steps
        for mask in masks:
            new_cord = current_cord + mask
            if new_cord in block_cords:
                continue
            if 0 <= new_cord.real <= size and 0 <= new_cord.imag <= size:
                if new_cord not in visited:
                    visited.add(new_cord)
                    to_visit.append((new_cord, current_steps + 1))
        visited.add(current_cord)


def part_2() -> int:
    _block_cords = [complex(int(line.split(",")[0]), int(line.split(",")[1])) for line in Path("input.txt").read_text().strip().splitlines()]

    size = 70
    start = complex(0, 0)
    end = complex(size, size)
    for n in range(len(_block_cords), 0, -1):
        print(n)
        block_cords = _block_cords[:n]
        to_visit = deque([(start, 0)])
        visited = set()
        reset = False
        while to_visit:
            if reset:
                break
            current_cord, current_steps = to_visit.popleft()
            masks = [complex(1, 0), complex(-1, 0), complex(0, -1), complex(0, 1)]
            if current_cord == end:
                reset = True
                break
            for mask in masks:
                new_cord = current_cord + mask
                if new_cord in block_cords:
                    continue
                if 0 <= new_cord.real <= size and 0 <= new_cord.imag <= size:
                    if new_cord not in visited:
                        visited.add(new_cord)
                        to_visit.append((new_cord, current_steps + 1))
            visited.add(current_cord)

        if not reset:
            print(block_cords[-1])


if __name__ == "__main__":
    # print(part_1())
    print(part_2())
