import os


def execute(s: str) -> int:
    ret = []
    for line in s.splitlines():
        bit_line = line.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0")
        ret.append(int(bit_line, 2))
    return max(ret)


def main() -> int:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, "input.txt")) as f:
        result = execute(f.read())
        return result


if __name__ == "__main__":  # pragma: no cover
    print(main())
