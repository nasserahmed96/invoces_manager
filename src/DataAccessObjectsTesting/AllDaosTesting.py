from src.DataAccessObjectsTesting.BrandDaoTesting import BrandDaoTesting
from src.DataAccessObjectsTesting.CategoryDaoTesting import CategoryDaoTesting


def run_tests():
    brand_dao_testing = BrandDaoTesting()
    category_dao_testing = CategoryDaoTesting()
    brand_dao_testing.run_tests()
    category_dao_testing.run_tests()


if __name__ == '__main__':
    run_tests()