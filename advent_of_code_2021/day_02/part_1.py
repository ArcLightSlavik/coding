import os


def execute(val: str) -> int:
    position = 0
    depth = 0

    for line in val.splitlines():
        cmd, numbr_s = line.split()
        numbr = int(numbr_s)
        if cmd == "forward":
            position += numbr
        elif cmd == "down":
            depth += numbr
        elif cmd == "up":
            depth -= numbr

    return position * depth


def main() -> int:
    __location__ = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(__location__, "input.txt")) as f:
        result = execute(f.read())
        return result


if __name__ == "__main__":  # pragma: no cover
    print(main())
