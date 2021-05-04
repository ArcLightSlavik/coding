import pytest

from .part_2 import execute


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (("1721 979 366 299 675 1456", 241861950),),
)
def test(input_s: str, expected: int) -> None:
    assert execute(input_s) == expected
