import os

from collections import defaultdict


def execute(s: str) -> int:
    lines = s.splitlines()
    counts: dict[int, int] = defaultdict(int)

    for line in lines:
        for i, c in enumerate(line):
            if c == '1':
                counts[i] += 1

    num1 = []
    num2 = []

    for i in range(len(lines[0])):
        if counts[i] > len(lines) / 2:
            num1.append("1")
            num2.append("0")
        else:
            num1.append("0")
            num2.append("1")

    return int("".join(num1), 2) * int("".join(num2), 2)


def main() -> int:
    __location__ = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(__location__, "input.txt")) as f:
        result = execute(f.read())
        return result


if __name__ == "__main__":  # pragma: no cover
    print(main())
