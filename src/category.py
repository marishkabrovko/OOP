from src.product import Product


class Category:
    """Информация о котегориях"""

    name: str  # название продукта
    description: str  # описание продукта
    list_product: list  # список товаров категории
    category_count = 0
    product_count = 0

    def __init__(self, name, description, list_product):
        self.name = name
        self.description = description
        self.__list_product = list_product
        Category.category_count += 1
        Category.product_count += len(list_product)

    def add_product(self, product: Product):
        self.__list_product.append(product)
        Category.product_count += 1

    @property
    def list_product(self):
        product_str = ""
        for product in self.__list_product:
            product_str += f"\n {product.name}, {product.price} руб. Остаток: {product.quantity} шт."
        return product_str

    @property
    def products_in_list(self):
        return self.__list_product
