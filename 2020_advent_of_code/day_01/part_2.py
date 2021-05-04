import itertools


def execute(s: str) -> int:
    numbers = [int(n_s) for n_s in s.split()]
    for a, b, c in itertools.combinations(numbers, 3):
        if a + b + c == 2020:
            return a * b * c
    else:
        raise NotImplementedError


def main() -> None:
    with open("input_1.txt") as f:
        result = execute(f.read())
        print(result)


if __name__ == "__main__":
    main()
