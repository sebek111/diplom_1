import pytest
from praktikum.ingredient import Ingredient

try:
    from praktikum.ingredient_types import IngredientType  # Enum/класс
except Exception:
    try:
        from praktikum.ingredient_types import IngredientTypes as IngredientType  # иной нейминг
    except Exception:
        class IngredientType:  # fallback на константы
            SAUCE = "SAUCE"
            FILLING = "FILLING"


@pytest.mark.parametrize("itype, name, price", [
    (IngredientType.SAUCE, "Ketchup", 10.0),
    (IngredientType.FILLING, "Cutlet", 120.0),
])
def test_ingredient_getters(itype, name, price):
    ing = Ingredient(itype, name, price)
    assert ing.get_type() == itype
    assert ing.get_name() == name
    assert ing.get_price() == price



