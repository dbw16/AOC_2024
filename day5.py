from pathlib import Path
from collections import defaultdict


def get_rules(text: str) -> defaultdict[str, str]:
    rules: defaultdict[str, list[str]] = defaultdict(list)
    for line in text.splitlines():
        if not line.strip():
            return rules
        a, b = line.split("|")
        rules[b].append(a)


def get_updates(text: str) -> list[str]:
    return [line.split(",") for line in text.strip().split("\n\n")[-1].strip().splitlines()]


def part_1() -> None:
    _input = Path("input.txt").read_text().strip()
    rules = get_rules(_input)
    total = 0
    updates = get_updates(_input)
    for update in updates:
        bad = False
        seen: set[str] = set()
        for page in update:
            for rule in rules[page]:
                if rule not in seen and rule in update:
                    bad = True
            seen.add(page)
        if not bad:
            total += int(update[len(update) // 2])

    print(total)


def part_2() -> None:
    _input = Path("input.txt").read_text().strip()
    rules = get_rules(_input)
    total = 0
    updates = get_updates(_input)
    for update in updates:
        completed = False
        fixed = False
        while not completed:
            bad = False
            seen: set[str] = set()
            for page in update:
                for rule in rules[page]:
                    if rule not in seen and rule in update:
                        # Corrected swap operation
                        page_index = update.index(page)
                        rule_index = update.index(rule)
                        update[page_index], update[rule_index] = update[rule_index], update[page_index]
                        bad = True
                        fixed = True
                        break
                if bad:
                    break
                seen.add(page)
            if not bad:
                if fixed:
                    total += int(update[len(update) // 2])
                completed = True

    print(total)


if __name__ == "__main__":
    # part_1()
    part_2()
