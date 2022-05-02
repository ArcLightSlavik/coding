import os


def execute_simple(s: str) -> int:
    numbers = [int(line) for line in s.splitlines()]
    count = 0
    prev = numbers[0]
    for n in numbers[1:]:
        if n > prev:
            count += 1
        prev = n
    return count


def execute(s: str) -> int:
    numbers = [int(line) for line in s.splitlines()]
    return sum(numbers[i] > numbers[i - 1] for i in range(1, len(numbers)))


def main_simple() -> int:
    __location__ = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(__location__, "input.txt")) as f:
        result = execute_simple(f.read())
        return result


def main() -> int:
    __location__ = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(__location__, "input.txt")) as f:
        result = execute(f.read())
        return result


if __name__ == "__main__":  # pragma: no cover
    print(main_simple())
    print(main())
