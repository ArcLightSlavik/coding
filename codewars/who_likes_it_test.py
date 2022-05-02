import pytest

from codewars.who_likes_it import execute


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (
        ([], "no one likes this"),
        (["Peter"], "Peter likes this"),
        (["Jacob", "Alex"], "Jacob and Alex like this"),
        (["Max", "John", "Mark"], "Max, John and Mark like this"),
        (["Alex", "Jacob", "Mark", "Max"], "Alex, Jacob and 2 others like this"),
    ),
)
def test_basic(input_s: list[str], expected: str) -> None:
    assert execute(input_s) == expected
