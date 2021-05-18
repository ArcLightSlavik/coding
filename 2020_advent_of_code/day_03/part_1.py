import os


def execute(s: str) -> int:
    lines = s.splitlines()
    x = 0
    count = 0

    for line in lines:
        if line[x] == "#":
            count += 1
        x += 3

        # if x is bigger than the line we need to shift it back so it is within bound
        #
        # i = 0
        # [1, 1, 1, 1, 1]
        #  ^
        #
        # i = 3
        # [1, 1, 1, 1, 1]
        #           ^
        #
        # i = 6 (-5 ==> 1)
        # [1, 1, 1, 1, 1] (OVERFLOW)
        #     ^

        if x >= len(line):
            x -= len(line)

    return count


def main() -> int:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, "input.txt")) as f:
        result = execute(f.read())
        return result


if __name__ == "__main__":  # pragma: no cover
    print(main())
