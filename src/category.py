class Category:
    name: str
    description: str
    list_category: list
    category_count = 0
    product_count = 0


def __init__(self, name, description, products):
    self.name = name
    self.description = description
    self.list_products = products
    Category.category_count += 1
    Category.product_count += len(products)
