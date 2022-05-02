import pytest

from advent_of_code_2020.day_01.part_1 import execute
from advent_of_code_2020.day_01.part_1 import execute_simple
from advent_of_code_2020.day_01.part_1 import main
from advent_of_code_2020.day_01.part_1 import main_simple


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (("1721 979 366 299 675 1456", 514579),),
)
def test_execute_simple(input_s: str, expected: int) -> None:
    assert execute_simple(input_s) == expected


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (("1721 979 366 299 675 1456", 514579),),
)
def test_execute(input_s: str, expected: int) -> None:
    assert execute(input_s) == expected


def test_main_simple() -> None:
    assert main_simple() == 158916


def test_main() -> None:
    assert main() == 158916
