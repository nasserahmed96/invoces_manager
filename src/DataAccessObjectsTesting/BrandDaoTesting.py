from src.DataAccessObjects.BrandDao import BrandDao
from src.DataObjects.Brand import Brand
import config
import csv


class BrandDaoTesting(object):
    def __init__(self):
        self.FILE_PATH = config.PROJECT_ROOT_PATH + "Testing_Data/brands_data_testing"
        self.brand_dao = BrandDao()

    def print_brand(self, brand:Brand):
        print(f"Brand name: {brand.name}\nBrand description: {brand.description}")

    def test_create_brand(self):
        print('Creating brands')
        brands = []
        brands_dao = BrandDao()
        with open("../../Testing_Data/brands_data_testing.csv") as brands_file:
            reader = csv.DictReader(brands_file)
            [brands.append(Brand(name=row["name"], description=row["description"])) for row in reader]
        [brands_dao.create_brand(brand) for brand in brands]

    def test_get_all_brands(self):
        print('Getting all brands')
        [self.print_brand(brand) for brand in self.brand_dao.get_all_brands()]

    def test_get_brand_by_id(self):
        print('Getting brand by ID')
        brand = self.brand_dao.get_brand_by_id(1)
        self.print_brand(brand)

    def test_get_brand_by_name(self):
        print('Getting brand by Name')
        brand = self.brand_dao.get_brand_by_name('Julie Baird')
        self.print_brand(brand)

    def test_update_brand(self):
        print('Updating brand')
        values = {
            'name': 'Nasser ORM'
        }
        self.brand_dao.update_brand(1, values)
        self.print_brand(self.brand_dao.get_brand_by_id(1))

    def test_delete_brand(self):
        print('Deleting brand')
        self.brand_dao.delete_brand(brand_id=6)
        print('Deleted brand: ', 6) if not self.brand_dao.get_brand_by_id(6) else self.print_brand(self.brand_dao.get_brand_by_id(6))

    def run_tests(self):
        self.test_create_brand()
        self.test_get_all_brands()
        self.test_get_brand_by_id()
        self.test_get_brand_by_name()
        self.test_update_brand()
        self.test_delete_brand()


if __name__ == '__main__':
    brand_dao_testing = BrandDaoTesting()
    brand_dao_testing.run_tests()