import csv
import config
from src.DataAccessObjects.EmployeeDao import EmployeeDao
from src.DataObjects.User import User
from src.DataObjects.Employee import Employee
import pandas as pd


class EmployeeDaoTesting:
    def __init__(self):
        self.FILE_PATH = config.TEST_DATA_PATH + 'employees_data_testing.csv'
        self.employee_dao = EmployeeDao()

    def print_employee(self, employee: Employee):
        print(f"Employee ID:  {employee.get_id()}\n"
              f"Employee name: {employee.get_user().get_first_name()} {employee.get_user().get_last_name()}\n"
              f"Employee phone: {employee.get_user().get_phone_number()}\n"
              f"Employee Email: {employee.get_user().get_email()}\n"
              f"Employee address: {employee.get_user().get_address()}\n"
              f"Employee gender: {employee.get_user().get_gender()}")

    def read_file(self):
        data = []
        with open(self.FILE_PATH) as data_file:
            reader = csv.DictReader(data_file)
            for row in reader:
                data.append(row)
        return data

    def test_create_employee(self):
        print('Creating Employee')
        i = 0
        for row in self.read_file():
            print('I: ', i)
            user = User(first_name=row.pop('first_name'),
                        middle_name=row.pop('middle_name'),
                        last_name=row.pop('last_name'),
                        phone_number=row.pop('phone_number'),
                        address=row.pop('address'),
                        email=row.pop('email'),
                        gender=row.pop('gender')
                        )
            self.employee_dao.create_employee(Employee(user=user,
                                                       username=row['username']),
                                              password=row['password'])

    def test_get_all_employees(self):
        print('Getting all employees')
        print(pd.DataFrame([employee.serialize_employee() for employee in self.employee_dao.get_all_employees()]))

    def test_get_dataframe(self):
        print(self.employee_dao.get_employees_dataframe())

    def test_get_employee_by_id(self):
        print('Getting employee by ID')
        print('Employee dictionary: ', self.employee_dao.get_employee_by_id(4).serialize_employee())
        self.print_employee(self.employee_dao.get_employee_by_id(1))

    def test_updtate_employee(self):
        print('Updating employee')
        values = {
            'user': {
                'first_name': 'Nasser ORM'
            }
        }
        self.employee_dao.update_employee(1, values)

    def test_delete_employee(self):
        print('Deleting employee')
        self.employee_dao.delete_employee(1)
        #self.employee_dao.get_employee_by_id(1)


    def run_tests(self):
        #self.test_create_employee()
        #self.test_get_all_employees()
        #self.test_delete_employee()
        #self.test_get_employee_by_id()
        self.test_get_dataframe()


if __name__ == '__main__':
    employee_dao_test = EmployeeDaoTesting()
    employee_dao_test.run_tests()