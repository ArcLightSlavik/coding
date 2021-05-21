from __future__ import annotations

import os
from dataclasses import dataclass


def execute_simple(s: str) -> int:
    counter = 0
    for line in s.splitlines():
        password_range, character, password = line.split()
        password_range_start_string, password_range_end_string = password_range.split("-")
        range_start, range_end = int(password_range_start_string), int(password_range_end_string)
        character = character[0]

        counts = password.count(character)

        if range_start <= counts <= range_end:
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
        counts = password.password.count(password.char)
        if password.begin <= counts <= password.end:
            total += 1
    return total


def main_simple() -> int:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, "input.txt")) as f:
        result = execute_simple(f.read())
        return result


def main() -> int:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, "input.txt")) as f:
        result = execute(f.read())
        return result


if __name__ == "__main__":  # pragma: no cover
    print(main_simple())
    print(main())
