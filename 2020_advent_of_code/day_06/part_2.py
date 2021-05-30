import os


def execute(s: str) -> int:
    ret = []
    for group_string in s.split("\n\n"):
        group = []
        for user_string in group_string.splitlines():
            group.append(set(user_string))
        ret.append(group)

    total = 0
    for group in ret:
        accumulator = group[0]
        for user in group:
            accumulator &= user
        total += len(accumulator)
    return total


def main() -> int:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, "input.txt")) as f:
        result = execute(f.read())
        return result


if __name__ == "__main__":  # pragma: no cover
    print(main())
