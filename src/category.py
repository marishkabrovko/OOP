from src.product import Product
from src.exeptions import ZeroQuantityProduct


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        product = 0
        for i in self.__products:
            product += i.quantity
        return f"{self.name}, количество продуктов: {product} шт."

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"\n{str(product)}"
        return product_str

    def add_product(self, product: Product):
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantityProduct('Нельзя добавить товар с нулевым количеством')
            except ZeroQuantityProduct as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print('Продукт добавлен успешно')
            finally:
                print('Обработка добавления продукта завершена')
        else:
            raise TypeError

    @property
    def products_in_list(self):
        return self.__products

    def middle_price(self):
        try:
            return sum([product.price for product in self.products_in_list]) / len(self.products_in_list)
        except ZeroDivisionError:
            return 0
