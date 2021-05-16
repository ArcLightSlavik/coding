import pytest

from .part_1 import execute
from .part_1 import execute_simple
from .part_1 import main
from .part_1 import main_simple


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (("1721 979 366 299 675 1456", 514579),),
)
def test_execute_simple(input_s: str, expected: int) -> None:
    assert execute_simple(input_s) == expected


def test_execute_simple_exception() -> None:
    with pytest.raises(NotImplementedError):
        execute_simple("")


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (("1721 979 366 299 675 1456", 514579),),
)
def test_execute(input_s: str, expected: int) -> None:
    assert execute(input_s) == expected


def test_execute_exception() -> None:
    with pytest.raises(NotImplementedError):
        execute("")


def test_main_simple() -> None:
    assert main_simple() == 158916


def test_main() -> None:
    assert main() == 158916
