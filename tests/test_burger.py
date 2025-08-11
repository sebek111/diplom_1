from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient

try:
    from praktikum.ingredient_types import IngredientType
except Exception:
    try:
        from praktikum.ingredient_types import IngredientTypes as IngredientType
    except Exception:
        class IngredientType:
            SAUCE = "SAUCE"
            FILLING = "FILLING"


def test_set_buns_sets_price_from_bun():
    burger = Burger()
    bun = Bun("black bun", 100.0)
    burger.set_buns(bun)
    # булка учитывается дважды
    assert burger.get_price() == 200.0


def test_add_remove_move_and_price():
    burger = Burger()
    burger.set_buns(Bun("black bun", 100.0))

    i1 = Ingredient(IngredientType.SAUCE, "BBQ", 20.0)
    i2 = Ingredient(IngredientType.FILLING, "Beef", 150.0)
    i3 = Ingredient(IngredientType.FILLING, "Cheese", 30.0)

    burger.add_ingredient(i1)  # 0
    burger.add_ingredient(i2)  # 1
    burger.add_ingredient(i3)  # 2

    # переставим Cheese (2) на позицию 0
    burger.move_ingredient(2, 0)
    assert burger.ingredients[0] is i3
    assert burger.ingredients[1] is i1
    assert burger.ingredients[2] is i2

    # удалим BBQ (теперь индекс 1)
    burger.remove_ingredient(1)
    assert burger.ingredients == [i3, i2]

    # цена: 2*100 + 30 + 150 = 380
    assert burger.get_price() == 380.0


def test_get_receipt_contains_bun_type_lower_and_price():
    burger = Burger()
    burger.set_buns(Bun("white bun", 50.0))
    ing = Ingredient(IngredientType.SAUCE, "Mustard", 5.0)
    burger.add_ingredient(ing)

    receipt = burger.get_receipt()
    # верх/низ булки
    assert "(==== white bun ====)" in receipt
    # тип ингредиента приводится к строке и к нижнему регистру внутри метода
    assert "= sauce Mustard =" in receipt
    # финальная цена отражена
    assert f"Price: {burger.get_price()}" in receipt


def test_burger_price_with_simple_mocks():
    """Моки без библиотек: объекты с нужными методами get_price/get_name/get_type."""
    class Fake:
        def __init__(self, price, name="X", itype="SAUCE"):
            self._p = price
            self._n = name
            self._t = itype
        def get_price(self): return self._p
        def get_name(self): return self._n
        def get_type(self): return self._t

    burger = Burger()
    burger.set_buns(Fake(10))      # булка учитывается дважды
    burger.add_ingredient(Fake(3))
    burger.add_ingredient(Fake(7))

    assert burger.get_price() == 20 + 3 + 7
