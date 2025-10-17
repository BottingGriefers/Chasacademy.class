import pytest
from calculator import add, subtract, division 
def test_add_two_numbers():
    assert add(2, 3) == 5

    # a // b  // betyder heltalsdivition att det försöker bli en int kort sagt
def test_divide_by_zero():
    with pytest.raises(ValueError):
        division(5, 0)