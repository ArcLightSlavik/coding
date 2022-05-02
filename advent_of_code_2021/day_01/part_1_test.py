import pytest

from advent_of_code_2021.day_01.part_1 import execute
from advent_of_code_2021.day_01.part_1 import execute_simple
from advent_of_code_2021.day_01.part_1 import main
from advent_of_code_2021.day_01.part_1 import main_simple

INPUT_S = """\
199
200
208
210
200
207
240
269
260
263
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 7),),
)
def test_execute(input_s: str, expected: int) -> None:
    assert execute(input_s) == expected


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 7),),
)
def test_execute_simple(input_s: str, expected: int) -> None:
    assert execute_simple(input_s) == expected


def test_main() -> None:
    assert main() == 1502


def test_main_simple() -> None:
    assert main_simple() == 1502
