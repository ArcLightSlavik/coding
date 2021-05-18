import os


def execute(s: str) -> int:
    return (
        execute_helper(1, 1, s)
        * execute_helper(3, 1, s)
        * execute_helper(5, 1, s)
        * execute_helper(7, 1, s)
        * execute_helper(1, 2, s)
    )


def execute_helper(x_difference: int, y_difference: int, s: str) -> int:
    total = 0
    x = 0
    y = 0

    lines = s.splitlines()

    while y < len(lines):
        line = lines[y]

        if line[x] == "#":
            total += 1

        x += x_difference

        if x >= len(line):
            x -= len(line)

        y += y_difference

    return total


def main() -> int:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, "input.txt")) as f:
        result = execute(f.read())
        return result


if __name__ == "__main__":  # pragma: no cover
    print(main())
