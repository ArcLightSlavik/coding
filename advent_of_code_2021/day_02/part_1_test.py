import pytest

from advent_of_code_2021.day_02.part_1 import execute
from advent_of_code_2021.day_02.part_1 import main

INPUT_S = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 150),),
)
def test_execute(input_s: str, expected: int) -> None:
    assert execute(input_s) == expected


def test_main() -> None:
    assert main() == 1636725
