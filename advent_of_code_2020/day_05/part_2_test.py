import pytest

from advent_of_code_2020.day_05.part_2 import execute
from advent_of_code_2020.day_05.part_2 import execute_simple
from advent_of_code_2020.day_05.part_2 import main
from advent_of_code_2020.day_05.part_2 import main_simple

INPUT_S = """\
BBBFFFFRLL
BBBFFFFRLR
BBBFFFFRRL
BBBFFFFRRR
BBBFFFBLLL
BBBFFFBLLR
BBBFFFBLRR
BBBFFFBRLL
BBBFFFBRLR
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 906),),
)
def test_execute_simple(input_s: str, expected: int) -> None:
    assert execute_simple(input_s) == expected


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 906),),
)
def test_execute(input_s: str, expected: int) -> None:
    assert execute(input_s) == expected


def test_main_simple() -> None:
    assert main_simple() == 554


def test_main() -> None:
    assert main() == 554
