from src.product import Product
class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0


def __init__(self, name, description, products):
    self.name = name
    self.description = description
    self.products = products
    Category.category_count += 1
    Category.product_count += len(products)


if __name__ == "__main__":
    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         ["product1", "product2", "product3"])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)