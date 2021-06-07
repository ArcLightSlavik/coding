import collections
import os
import re
from typing import DefaultDict


LINE_RE = re.compile(r"^(\w+ \w+) bags contain (.+)$")
CHILD_RE = re.compile(r"(\d+) (\w+ \w+)")


def parse(input_string: str) -> DefaultDict[str, list[str]]:
    parents = collections.defaultdict(list)
    for line in input_string.splitlines():
        line_match = LINE_RE.match(line)
        assert line_match, line
        parent = line_match[1]
        rest = line_match[2]

        for _, child in CHILD_RE.findall(rest):
            parents[child].append(parent)
    return parents


def execute(input_string: str) -> int:
    parsed_string = parse(input_string)

    seen_colours = set()
    todo = ["shiny gold"]

    while todo:
        colour = todo.pop()
        seen_colours.add(colour)
        todo.extend(parsed_string[colour])

    return len(seen_colours - {"shiny gold"})


def main() -> int:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, "input.txt")) as f:
        result = execute(f.read())
        return result


if __name__ == "__main__":  # pragma: no cover
    print(main())
