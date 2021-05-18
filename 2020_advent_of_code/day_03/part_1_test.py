import pytest

from .part_1 import execute
from .part_1 import main

INPUT_S = """\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 7),),
)
def test_execute(input_s: str, expected: int) -> None:
    assert execute(input_s) == expected


def test_main() -> None:
    assert main() == 148
