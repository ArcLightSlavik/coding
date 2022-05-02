import os

REQUIRED = frozenset(
    (
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    ),
)


def execute_simple(s: str) -> int:
    # parsing
    count = 0
    list_of_keywords = []
    for line in s.split("\n\n"):
        for password_line in line.split():
            key, value = password_line.split(":")
            if not key == "cid":
                list_of_keywords.append(key)

        # execution
        if set(REQUIRED).issubset(list_of_keywords):
            count += 1

        list_of_keywords.clear()

    return count


def execute(s: str) -> int:
    # parsing
    ret = []
    for passport_s in s.split("\n\n"):
        dct = {}
        for field in passport_s.split():
            key, value = field.split(":")
            dct[key] = value
        ret.append(dct)

    # execution
    total = 0

    for passport in ret:
        if passport.keys() >= REQUIRED:
            total += 1

    return total


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
