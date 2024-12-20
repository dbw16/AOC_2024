from pathlib import Path


def part_1() -> None:
    lines = Path("input.txt").read_text().strip().splitlines()

    a = int(lines[0].split(":")[-1].strip())
    b = int(lines[1].split(":")[-1].strip())
    c = int(lines[2].split(":")[-1].strip())
    seq = list(map(int, lines[4].split(":")[-1].strip().split(",")))

    index = 0
    output = []

    combo_operand = {
        0: lambda: 0,
        1: lambda: 1,
        2: lambda: 2,
        3: lambda: 3,
        4: lambda: a,
        5: lambda: b,
        6: lambda: c,
    }

    # for opcode, operand in zip(seq[::2], seq[1::2]):
    while index < len(seq):
        opcode, operand = seq[index], seq[index + 1]
        if opcode == 0:
            a = a // 2 ** combo_operand[operand]()
        elif opcode == 1:
            b = b ^ operand
        elif opcode == 2:
            b = combo_operand[operand]() % 8
        elif opcode == 3:
            if a != 0:
                index = operand - 2
        elif opcode == 4:
            b = b ^ c
        elif opcode == 5:
            output.append(combo_operand[operand]() % 8)
        elif opcode == 6:
            b = a // 2 ** combo_operand[operand]()
        elif opcode == 7:
            c = a // 2 ** combo_operand[operand]()
        else:
            raise Exception()

        index += 2
        print(combo_operand[4](), combo_operand[5](), combo_operand[6]())
        print(a, b, c, index)

    print(",".join([str(x) for x in output]))


def part_2():
    lines = Path("input.txt").read_text().strip().splitlines()
    a_orginal = 0
    while True:
        a = a_orginal
        b = int(lines[1].split(":")[-1].strip())
        c = int(lines[2].split(":")[-1].strip())
        seq = list(map(int, lines[4].split(":")[-1].strip().split(",")))

        index = 0
        output = []

        combo_operand = {
            0: lambda: 0,
            1: lambda: 1,
            2: lambda: 2,
            3: lambda: 3,
            4: lambda: a,
            5: lambda: b,
            6: lambda: c,
        }

        # for opcode, operand in zip(seq[::2], seq[1::2]):
        while index < len(seq):
            opcode, operand = seq[index], seq[index + 1]
            if opcode == 0:
                a = a // 2 ** combo_operand[operand]()
            elif opcode == 1:
                b = b ^ operand
            elif opcode == 2:
                b = combo_operand[operand]() % 8
            elif opcode == 3:
                if a != 0:
                    index = operand - 2
            elif opcode == 4:
                b = b ^ c
            elif opcode == 5:
                output.append(combo_operand[operand]() % 8)
            elif opcode == 6:
                b = a // 2 ** combo_operand[operand]()
            elif opcode == 7:
                c = a // 2 ** combo_operand[operand]()
            else:
                raise Exception()

            index += 2

        if output == seq:
            break

        a_orginal += a_orginal**8
    print(a_orginal)


if __name__ == "__main__":
    # part_1()
    part_2()
