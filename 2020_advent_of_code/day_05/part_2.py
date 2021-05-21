from __future__ import annotations

import os


def parse(s: str) -> list[int]:
    ret = []
    for line in s.splitlines():
        bit_line = line.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0")
        ret.append(int(bit_line, 2))
    return ret


def execute_simple(s: str) -> int:
    parsed = parse(s)

    all_inputs = set(parsed)

    for n in all_inputs:
        if n + 1 not in all_inputs and n + 2 in all_inputs:
            return n + 1

    raise AssertionError


def execute(s: str) -> int:
    parsed = parse(s)

    all_inputs = set(range(1024))
    for n in parsed:
        all_inputs.discard(n)

    for remaining in all_inputs:
        if remaining - 1 not in all_inputs and remaining + 1 not in all_inputs:
            return remaining

    raise AssertionError


def main_simple() -> int:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, "input.txt")) as f:
        result = execute_simple(f.read())
        return result


def main() -> int:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, "input.txt")) as f:
        result = execute(f.read())
        return result


if __name__ == "__main__":  # pragma: no cover
    print(main_simple())
    print(main())
