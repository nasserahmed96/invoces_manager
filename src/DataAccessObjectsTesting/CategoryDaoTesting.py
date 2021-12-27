import csv
import config
from src.DataAccessObjects.CategoryDao import CategoryDao
from src.DataObjects.Category import Category


class CategoryDaoTesting(object):
    def __init__(self):
        self.FILE_PATH = f"{config.PROJECT_ROOT_PATH}/Testing_Data/categories_data_testing.csv"
        self.category_dao = CategoryDao()

    def print_category(self, category: Category):
        print(f"Category name: {category.name}\nCategory description: {category.description}")

    def read_file(self):
        data = []
        with open(self.FILE_PATH) as data_file:
            reader = csv.DictReader(data_file)
            for row in reader:
                data.append(row)
        return data

    def test_create_category(self):
        print('Create category')
        categories = [Category(name=category['name'], description=category['description']) for category in self.read_file()]
        [self.category_dao.create_category(category) for category in categories]

    def test_get_all_categories(self):
        print('Getting all categories')
        [self.print_category(category) for category in self.category_dao.get_all_categories()]

    def test_get_category_by_id(self):
        print('Getting category by ID')
        self.print_category(self.category_dao.get_category_by_id(1))

    def test_get_category_by_name(self):
        print('Getting category by name')
        self.print_category(self.category_dao.get_category_by_name('Cyrus Simpson'))

    def test_update_category(self):
        print('Updating category')
        values = {
            'name': 'Nasser ORM'
        }
        self.category_dao.update_category(category_id=1, values=values)

    def run_tests(self):
        self.test_create_category()
        self.test_get_all_categories()
        self.test_get_category_by_id()
        self.test_get_category_by_name()
        self.test_update_category()


if __name__ == '__main__':
    categories_testing = CategoryDaoTesting()
    categories_testing.run_tests()

