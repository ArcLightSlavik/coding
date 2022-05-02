import os
import re

LINE_RE = re.compile(r"^(\w+ \w+) bags contain (.+)$")
CHILD_RE = re.compile(r"(\d+) (\w+ \w+)")


def parse(input_string: str) -> dict[str, list[tuple[int, str]]]:
    colors = {}

    for line in input_string.splitlines():
        line_match = LINE_RE.match(line)
        assert line_match, line
        parent = line_match[1]
        rest = line_match[2]

        children = [(int(n), child) for n, child in CHILD_RE.findall(rest)]

        colors[parent] = children

    return colors


def execute(input_string: str) -> int:
    parsed_string = parse(input_string)

    total = 0
    todo = [(1, "shiny gold")]

    while todo:
        n, colour = todo.pop()
        total += n

        for child_n, child in parsed_string[colour]:
            todo.append((n * child_n, child))

    total -= 1
    return total


def main() -> int:
    __location__ = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(__location__, "input.txt")) as f:
        result = execute(f.read())
        return result


if __name__ == "__main__":  # pragma: no cover
    print(main())
