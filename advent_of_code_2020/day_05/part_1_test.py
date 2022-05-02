import pytest

from advent_of_code_2020.day_05.part_1 import execute
from advent_of_code_2020.day_05.part_1 import main

INPUT_S = """\
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 820),),
)
def test_execute(input_s: str, expected: int) -> None:
    assert execute(input_s) == expected


def test_main() -> None:
    assert main() == 944
