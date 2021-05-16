import itertools
import os


def execute_simple(s: str) -> int:
    numbers = [int(n_s) for n_s in s.split()]
    for x, y in itertools.combinations(numbers, 2):
        if x + y == 2020:
            return x * y
    else:
        raise NotImplementedError


def execute(s: str) -> int:
    numbers = set()
    for n_s in s.split():
        n = int(n_s)
        numbers.add(n)
        if 2020 - n in numbers:
            return (2020 - n) * n
    else:
        raise NotImplementedError


def main_simple() -> int:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, "input_1.txt")) as f:
        result = execute_simple(f.read())
        return result


def main() -> int:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, "input_1.txt")) as f:
        result = execute(f.read())
        return result


if __name__ == "__main__":
    print(main_simple())
    print(main())
