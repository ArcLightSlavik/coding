import pytest

from .part_2 import execute
from .part_2 import main


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (("1721 979 366 299 675 1456", 241861950),),
)
def test_execute(input_s: str, expected: int) -> None:
    assert execute(input_s) == expected


def test_execute_exception() -> None:
    with pytest.raises(NotImplementedError):
        execute("")


def test_main() -> None:
    assert main() == 165795564
