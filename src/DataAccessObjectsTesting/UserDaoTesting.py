import csv
from src.DataAccessObjects.UserDao import UserDao
from src.DataObjects.User import User
import config
class UserDaoTesting(object):
    def __init__(self):
        self.FILE_PATH = config.TEST_DATA_PATH + 'users_data_testing.csv'
        self.user_dao = UserDao()

    def print_user(self, user: User):
        print(f"User name: {user.first_name} {user.last_name}\n"
              f"User phone: {user.phone_number}\n"
              f"User Email: {user.email}\n"
              f"User address: {user.address}\n"
              f"User gender: {user.gender}")

    def read_file(self):
        data = []
        with open(self.FILE_PATH) as data_file:
            reader = csv.DictReader(data_file)
            for row in reader:
                data.append(row)
        return data

    def test_create_user(self):
        print('Creating user')
        [self.user_dao.create_user(User(first_name=user['first_name'],
                                        middle_name=user['middle_name'],
                                        last_name=user['last_name'],
                                        phone_number=user['phone_number'],
                                        email=user['email'],
                                        address=user['address'],
                                        gender=user['gender']
                                        )) for user in self.read_file()]

    def test_get_all_users(self):
        print('Getting all users')
        [self.print_user(user) for user in self.user_dao.get_all_users()]

    def test_get_user_by_id(self):
        print('Getting user by ID')
        self.print_user(self.user_dao.get_user_by_id(2))

    def test_get_user_by_name(self):
        print('Getting user by name')
        self.print_user(self.user_dao.get_user_name('Brian'))

    def test_update_user(self):
        print('Updating user')
        values = {
            'first_name': 'Nasser ORM'
        }
        self.user_dao.update_user(1, values=values)
        self.print_user(self.user_dao.get_user_by_id(2))

    def test_delete_user(self):
        print('Deleting user')
        self.user_dao.delete_user(1)
        print('Deleted') if not self.user_dao.get_user_by_id(1) else self.print_user(self.user_dao.get_user_by_id(1))


    def run_tests(self):
        self.test_create_user()
        self.test_get_all_users()
        self.test_get_user_by_id()
        self.test_get_user_by_name()
        self.test_update_user()
        self.test_delete_user()


if __name__ == '__main__':
    user_dao_testing = UserDaoTesting()
    user_dao_testing.run_tests()
