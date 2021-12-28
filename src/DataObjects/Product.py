class Product(object):
    def __init__(self, id=None, name=None, description=None, price=None,
                 quantity=None, barcode=None, notes=None, category=None, brand=None, status=None):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.barcode = barcode
        self.notes = notes
        self.category = category
        self.brand = brand
        self.status = status

    def get_id(self):
        return self.id

    def set_id(self, id:int):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description

    def set_description(self, description:str):
        self.description = description

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_barcode(self):
        return self.barcode

    def set_barcode(self, barcode:str):
        self.barcode = barcode

    def get_notes(self):
        return self.notes

    def set_notes(self, notes):
        self.notes = notes

    def get_category(self):
        return self.category

    def set_category(self, category):
        self.category = category

    def get_brand(self):
        return self.brand

    def set_brand(self, brand):
        self.brand = brand

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

