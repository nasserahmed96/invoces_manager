import csv
from src.DataAccessObjects.ProductDao import ProductDao
from src.DataObjects.Product import Product
from src.DataObjects.Category import Category
from src.DataObjects.Brand import Brand
from src.DataAccessObjects.CategoryDao import CategoryDao
from src.DataAccessObjects.BrandDao import BrandDao
import config

class ProductDaoTesting(object):
    def __init__(self):
        self.FILE_PATH = f'{config.PROJECT_ROOT_PATH}/Testing_Data/products_data_testing.csv'
        self.product_dao = ProductDao()
        self.category_dao = CategoryDao()
        self.brand_dao = BrandDao()

    def print_product(self, product: Product):
        print(f"Product name: {product.name}\nProduct description: {product.description}")

    def read_file(self):
        data = []
        with open(self.FILE_PATH) as data_file:
            reader = csv.DictReader(data_file)
            for row in reader:
                data.append(row)
        return data

    def test_create_product(self):
        for product in self.read_file():
            print('Category: ', self.category_dao.get_category_by_id(product['category']))
            self.product_dao.create_product(Product(name=product['name'], description=product['description'], price=product['price'],
                            quantity=product['quantity'], barcode=product['bracode'],
                    category=self.category_dao.get_category_by_id(product['category']),
                    brand=self.brand_dao.get_brand_by_id(product['brand'])))

    def test_get_all_products(self):
        print('Getting all products')
        [self.print_product(product) for product in self.product_dao.get_all_products()]

    def test_get_product_by_id(self):
        print('Getting product by ID')
        self.print_product(self.product_dao.get_product_by_id(1))

    def test_get_product_by_name(self):
        print('Getting product by name')
        self.print_product(self.product_dao.get_product_by_name('Cyrus Simpson'))

    def test_update_product(self):
        print('Updating product')
        values = {
            'name': 'Nasser ORM New'
        }
        self.product_dao.update_product(product_id=1, values=values)
        self.print_product(self.product_dao.get_product_by_name('Nasser ORM New'))

    def test_delete_product(self):
        print('Deleting product')
        self.product_dao.delete_product(product_id=1)
        print('Deleted') if not self.product_dao.get_product_by_id(1) else self.print_product(self.product_dao.get_product_by_id(1))

    def run_tests(self):
        self.test_create_product()
        self.test_get_all_products()
        self.test_get_product_by_id()
        self.test_get_product_by_name()
        self.test_update_product()
        self.test_delete_product()

if __name__ == '__main__':
    products_dao = ProductDaoTesting()
    products_dao.run_tests()