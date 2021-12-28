from src.DataAccessObjectsTesting.BrandDaoTesting import BrandDaoTesting
from src.DataAccessObjectsTesting.CategoryDaoTesting import CategoryDaoTesting
from src.DataAccessObjectsTesting.ProductDaoTesting import ProductDaoTesting
from src.DataAccessObjectsTesting.UserDaoTesting import UserDaoTesting


def run_tests():
    brand_dao_testing = BrandDaoTesting()
    category_dao_testing = CategoryDaoTesting()
    product_dao_testing = ProductDaoTesting()
    user_dao_testing = UserDaoTesting()
    brand_dao_testing.run_tests()
    category_dao_testing.run_tests()
    product_dao_testing.run_tests()
    user_dao_testing.run_tests()



if __name__ == '__main__':
    run_tests()