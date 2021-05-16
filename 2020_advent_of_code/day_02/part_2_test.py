import pytest

from .part_2 import execute
from .part_2 import execute_simple
from .part_2 import main
from .part_2 import main_simple

INPUT_S = """\
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 1),),
)
def test_execute_simple(input_s: str, expected: int) -> None:
    assert execute_simple(input_s) == expected


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 2),),
)
def test_execute(input_s: str, expected: int) -> None:
    assert execute(input_s) == expected


def test_main_simple() -> None:
    assert main_simple() == 690


def test_main() -> None:
    assert main() == 690
