import os
from dataclasses import dataclass


def execute_simple(s: str) -> int:
    counter = 0
    for line in s.splitlines():
        password_range, character, password = line.split()
        password_range_start_string, password_range_end_string = password_range.split("-")
        range_start, range_end = int(password_range_start_string), int(password_range_end_string)
        character = character[0]

        begin = password[range_start - 1] == character
        end = password[range_end - 1] == character

        # if (begin and not end) or (not begin and end):
        if begin ^ end:
            counter += 1

    return counter


@dataclass
class Password:
    begin: int
    end: int
    char: str
    password: str


def parse_into_password(s: str) -> list[Password]:
    password_list = []

    for line in s.splitlines():
        password_range, character, password = line.split()
        password_range_start_string, password_range_end_string = password_range.split("-")
        password_list.append(
            Password(
                int(password_range_start_string),
                int(password_range_end_string),
                (character[0]),
                password,
            ),
        )
    return password_list


def execute(s: str) -> int:
    total = 0
    parsed_classes = parse_into_password(s=s)

    for password in parsed_classes:
        begin = password.password[password.begin - 1] == password.char
        end = password.password[password.end - 1] == password.char

        # if (begin and not end) or (not begin and end):
        if begin ^ end:
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
