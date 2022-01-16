import csv
import config
from src.DataAccessObjects.CustomerDao import CustomerDao
from src.DataAccessObjects.UserDao import UserDao
from src.DataObjects.Customer import Customer
from src.DataObjects.User import User


class CustomerDaoTesting:
    def __init__(self):
        self.FILE_PATH = config.TEST_DATA_PATH + 'customers_data_testing.csv'
        self.customer_dao = CustomerDao()

    def print_customer(self, customer: Customer):
        print(f"Customer ID:  {customer.get_id()}\n"
              f"Customer name: {customer.get_user().get_first_name()} {customer.user.last_name}\n"
              f"Customer phone: {customer.user.phone_number}\n"
              f"Customer Email: {customer.user.email}\n"
              f"Customer address: {customer.user.address}\n"
              f"Customer gender: {customer.user.gender}")

    def read_file(self):
        data = []
        with open(self.FILE_PATH) as data_file:
            reader = csv.DictReader(data_file)
            for row in reader:
                data.append(row)
        return data

    def test_create_customer(self):
        print('Creating user')
        for customer in self.read_file():
            user = User(first_name=customer['first_name'],
                        middle_name=customer['middle_name'],
                        last_name=customer['last_name'],
                        phone_number=customer['phone_number'],
                        email=customer['email'],
                        address=customer['address'],
                        gender=customer['gender'])
            self.customer_dao.create_customer(customer=Customer(user=user))

    def test_update_customer(self):
        print('Updating customer')
        values = {
            'user':{
                'first_name': 'Nasser ORM'
            }
        }
        self.customer_dao.update_customer(1, values)

    def test_get_all_customers(self):
        print('Getting all customers')
        [self.print_customer(customer) for customer in self.customer_dao.get_all_customers()]

    def test_get_customer_by_id(self):
        print('Getting customer by ID')
        self.print_customer(self.customer_dao.get_customer_by_id(customer_id=1))

    def test_delete_customer(self):
        print('Deleting customer')
        self.customer_dao.delete_customer(customer_id=1)

    def test_get_dataframe(self):
        print(self.customer_dao.get_customers_dataframe())



    def run_tests(self):
        """self.test_create_customer()
        self.test_update_customer()
        self.test_get_all_customers()
        self.test_delete_customer()"""
        self.test_get_dataframe()


if __name__ == '__main__':
    customer_dao_testing = CustomerDaoTesting()
    customer_dao_testing.run_tests()