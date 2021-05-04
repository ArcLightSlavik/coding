import pytest

from .part_1 import execute
from .part_1 import execute_simple


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (("1721 979 366 299 675 1456", 514579),),
)
def test_simple(input_s: str, expected: int) -> None:
    assert execute_simple(input_s) == expected


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (("1721 979 366 299 675 1456", 5145788),),
)
def test(input_s: str, expected: int) -> None:
    assert execute(input_s) == expected
