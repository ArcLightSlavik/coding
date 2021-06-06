import os
import re

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


HAIR_COLOURS = frozenset(
    (
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth",
    ),
)


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
    count = 0

    for passport in ret:
        if passport.keys() >= REQUIRED:
            if not (1920 <= int(passport["byr"]) <= 2002):
                continue  # pragma: no cover
            if not (2010 <= int(passport["iyr"]) <= 2020):
                continue
            if not (2020 <= int(passport["eyr"]) <= 2030):
                continue

            match = re.match(r"^(\d+)(cm|in)$", passport["hgt"])
            if not match:
                continue

            if match[2] == "in" and not (59 <= int(match[1]) <= 76):
                continue  # # pragma: no cover
            if match[2] == "cm" and not (150 <= int(match[1]) <= 193):
                continue

            if not re.match("^#[a-f0-9]{6}$", passport["hcl"]):
                continue

            if passport["ecl"] not in HAIR_COLOURS:
                continue

            if not re.match("^[0-9]{9}$", passport["pid"]):
                continue

            count += 1
    return count


def main() -> int:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, "input.txt")) as f:
        result = execute(f.read())
        return result


if __name__ == "__main__":  # pragma: no cover
    print(main())
