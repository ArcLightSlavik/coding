import pytest

from advent_of_code_2021.day_03.part_2 import execute
from advent_of_code_2021.day_03.part_2 import main

INPUT_S = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 230),),
)
def test_execute(input_s: str, expected: int) -> None:
    assert execute(input_s) == expected


def test_main() -> None:
    assert main() == 5736383
