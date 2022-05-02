import os
from typing import Any


def execute(s: str) -> int:
    lines = s.splitlines()

    columns = list(zip(*lines))

    path: list[str] = []
    included = set(range(len(lines)))
    while len(included) != 1:
        column = columns[len(path)]
        ones = sum(column[pos] == "1" for pos in included)
        if ones >= len(included) / 2:
            path.append("1")
        else:
            path.append("0")

        included = {pos for pos in included if column[pos] == path[-1]}

    best = lines[next(iter(included))]

    path = []
    included = set(range(len(lines)))
    while len(included) != 1:
        column = columns[len(path)]
        ones = sum(column[pos] == "1" for pos in included)
        if ones < len(included) / 2:
            path.append("1")
        else:
            path.append("0")

        included = {pos for pos in included if column[pos] == path[-1]}

    worst = lines[next(iter(included))]

    return int(best, 2) * int(worst, 2)


def execute_haxy_dicts(s: str) -> int:
    lines = s.splitlines()

    root: dict[str, Any] = {"count": 0}
    for line in lines:
        current = root
        for c in line:
            current["count"] += 1
            current.setdefault(c, {"count": 0})
            current = current[c]
        current["count"] += 1

    path = []
    current = root
    while True:
        if current.get("1", {}).get("count", 0) >= current.get("0", {}).get("count", 0):
            current = current["1"]
            path.append("1")
        else:
            current = current["0"]
            path.append("0")

        if current["count"] == 1:
            prefix = "".join(path)
            break

    path = []
    current = root
    while True:
        if current.get("1", {}).get("count", 0) < current.get("0", {}).get("count", 0):
            current = current["1"]
            path.append("1")
        else:
            current = current["0"]
            path.append("0")

        if current["count"] == 1:
            prefix2 = "".join(path)
            break

    (best,) = (line for line in lines if line.startswith(prefix))
    (worst,) = (line for line in lines if line.startswith(prefix2))

    return int(best, 2) * int(worst, 2)


def main() -> int:
    __location__ = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(__location__, "input.txt")) as f:
        result = execute(f.read())
        return result


if __name__ == "__main__":  # pragma: no cover
    print(main())
