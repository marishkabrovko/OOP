class Product:
    """Информация о свойтвах продуктах"""

    name: str  # название продукта
    description: str  # описание  продукта
    price: float  # цена  продукта
    quantity: int  # количество продукта

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
