import pytest
from praktikum.bun import Bun


@pytest.mark.parametrize("name, price", [
    ("black bun", 100.0),
    ("white bun", 49.9),
    ("Булочка", 0.0),
])
def test_bun_fields_and_getters(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price


