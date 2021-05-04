import itertools


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


def main() -> None:
    with open("input_1.txt") as f:
        result_simple = execute_simple(f.read())
        print("result_simple", result_simple)
        f.seek(0)
        result = execute(f.read())
        print("result", result)


if __name__ == "__main__":
    main()
