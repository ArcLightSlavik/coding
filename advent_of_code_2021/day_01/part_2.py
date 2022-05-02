import os


def execute(s: str) -> int:
    numbers = [int(line) for line in s.splitlines()]
    return sum(numbers[i] > numbers[i - 3] for i in range(1, len(numbers)))


def main() -> int:
    __location__ = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(__location__, "input.txt")) as f:
        result = execute(f.read())
        return result


if __name__ == "__main__":  # pragma: no cover
    print(main())
