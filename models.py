class Product(object):
    """
    name, description, price, quantity, category.name. brand.name
    """
    def __init__(self, name, description, price, quantity, category_name, brand_name):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.category_name = category_name
        self.brand_name = brand_name

    def __str__(self):
        return self.name