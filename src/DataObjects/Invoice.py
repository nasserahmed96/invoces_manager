import copy
class Invoice(object):
    def __init__(self, invoice_id=None, date=None, time=None, employee=None, customer=None,
                 serial_number=None, products=[], employees_shares=[]):
        self.invoice_id = invoice_id
        self.date = date
        self.time = time
        self.employee = employee
        self.customer = customer
        self.serial_number = serial_number
        self.products = copy.deepcopy(products)
        self.employees_shares = copy.deepcopy(employees_shares)

    def get_employees_shares(self):
        return self.employees_shares

    def set_employees_shares(self, employees_shares:list):
        self.employees_shares = copy.deepcopy(employees_shares)

    def get_products(self):
        return self.products

    def set_products(self, products: list):
        self.products = copy.deepcopy(self.products)

    def append_product(self, product):
        self.products.append(product)

    def append_employee_share(self, employee_share: dict()):
        self.employees_shares.append(employee_share)

    def get_invoice_id(self):
        return self.invoice_id

    def set_invoice_id(self, invoice_id):
        self.invoice_id = invoice_id

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_employee(self):
        return self.employee

    def set_employee(self, employee):
        self.employee = employee

    def get_customer(self):
        return self.customer

    def set_customer(self, customer):
        self.customer = customer

    def get_serial_number(self):
        return self.serial_number

    def set_serial_number(self, serial_number):
        self.serial_number = serial_number

    def __str__(self):
        return self.serial_number
