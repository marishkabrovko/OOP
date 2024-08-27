import pytest

from src.category import Category


@pytest.fixture
def category():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для "
                    "удобства жизни",
                    1)


def test_category(category):
    assert category.name == "Смартфоны"
    assert category.description == ("Смартфоны, как средство не только коммуникации, но и получения дополнительных "
                                    "функций для удобства жизни")
    assert category.products == 1