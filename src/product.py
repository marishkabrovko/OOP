class Product:
    """Информация о свойтвах продуктах"""

    name: str  # название продукта
    description: str  # описание  продукта
    price: float  # цена  продукта
    quantity: int  # количество продукта

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        return self.__price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, dict_product):
        return cls(
            dict_product["name"],
            dict_product["description"],
            dict_product["price"],
            dict_product["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: int):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price
