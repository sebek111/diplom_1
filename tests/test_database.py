from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


def test_database_returns_lists_of_models():
    db = Database()
    buns = db.available_buns()
    ings = db.available_ingredients()

    assert isinstance(buns, list) and all(isinstance(x, Bun) for x in buns)
    assert isinstance(ings, list) and all(isinstance(x, Ingredient) for x in ings)
    assert buns and ings  # ожидаем не пустые коллекции
