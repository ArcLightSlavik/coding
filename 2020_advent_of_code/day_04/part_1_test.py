import pytest

from .part_1 import execute
from .part_1 import execute_simple
from .part_1 import main
from .part_1 import main_simple

INPUT_S = """\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 2),),
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
    assert main_simple() == 239


def test_main() -> None:
    assert main() == 239
