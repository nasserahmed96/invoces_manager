from src.DataObjects.Product import Product
from src.DataAccessObjects.ProductDao import ProductDao

class Invoice:
    """
    The invoice class only generates the required data for the invoice, it doesn't affect the database in any case,
    it gets the employee name, customer name and a list of dictionaries that contain the product id and the required
    quantity, any validation should be put before calling an instance of the class.
    """
    def __init__(self, employee_name, customer_name, products_quantities):
        self.product_dao = ProductDao()
        self.employee_name = employee_name
        self.customer_name = customer_name
        self.products_quantities = products_quantities

    def get_product_by_id(self, product_id):
        product = self.product_dao.get_product_by_id(product_id)

    def get_products_data(self):
        """
        Generate a data frame contains objects and its quantities, it iterates over the products_quantities list and
        get the required product from the database and assign it to the quantity
        :return:
        """