
def test_category_init(category):
    assert category.name == "Смартфоны"
    assert category.description == ("Смартфоны, "
                                    "как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")
    assert category.list_product == [
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        ]
