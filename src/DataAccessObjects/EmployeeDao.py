from src.DataAccessObjects.DataAccessObject import DataAccessObject
from src.DataAccessObjects.UserDao import UserDao
from src.Authenticate import Authentication
from src.DataObjects.Employee import Employee
import pandas as pd


class EmployeeDao(DataAccessObject):
    def __init__(self):
        super(EmployeeDao, self).__init__(table_name='employees')
        self.user_dao = UserDao()
        self._authenticate = Authentication()

    def create_employee(self, employee, password):
        user_id = self.user_dao.create_user(employee.get_user())
        values = {
            'user_id': user_id,
            'username': employee.get_username(),
            'password': self._authenticate.hash_password(username=employee.get_username(), password=password)
        }
        return self.insert(values)

    def get_all_employees(self, query_str=None):
        employees = []
        query_str = """SELECT users.*, employees.id AS employee_id, 
        employees.username FROM employees INNER JOIN users ON users.id=employee_id""" if not query_str else None
        query_result = self.execute_select_query(query_str=query_str)
        while(query_result.next()):
            user = self.user_dao.fill_user(query_result)
            employees.append(Employee(id=query_result.value('employee_id'),
                                      user=user,
                                      username=query_result.value('username')))
        return employees

    def get_employees_dataframe(self, conditions='', placeholders=None):
        employees = []
        query = """SELECT users.*, employees.id AS employee_id, 
                employees.username FROM employees INNER JOIN users ON users.id=employees.user_id""" + conditions
        query_result = self.execute_select_query(query_str=query, placeholders=placeholders)
        while(query_result.next()):
            user = self.user_dao.fill_user(query_result)
            employees.append(Employee(
                id=query_result.value('employee_id'),
                user=user,
                username=query_result.value('username')
            ).serialize_employee())
        employees_dataframe = pd.DataFrame(employees)
        new_columns = [column.replace('_', ' ').capitalize() for column in employees_dataframe.columns]
        employees_dataframe.rename({employees_dataframe.columns[i]:new_columns[i] for i in range(len(new_columns))},
                                   axis=1, inplace=True)
        return employees_dataframe




    def get_employees_data(self):
        query_str = """SELECT users.first_name AS first_name, users.middle_name AS middle_name
        users.last_name AS last_name, users.phone_number AS phone_number, users.address AS address,
        users.gender AS gender,
        employees.id AS employee_id, 
        employees.username FROM employees INNER JOIN users ON users.id=employee_id"""

    def get_employee_by_id(self, employee_id):
        query_str = """SELECT users.*, employees.id AS employee_id,employees.username FROM employees 
        INNER JOIN users ON users.id=employees.user_id"""
        conditions = [
            {
                'column': 'employee_id',
                'value': employee_id,
                'operator': '=',
                'options': ''
            }
        ]
        query_str += self.build_conditions(conditions)
        placeholders = self.extract_values_from_conditions(conditions)
        query_result = self.execute_select_query(query_str, placeholders)
        if query_result and query_result.first():
            return Employee(id=query_result.value('employee_id'),
                            username=query_result.value('username'),
                            user=self.user_dao.fill_user(query_result))
        return None

    def update_employee(self, employee_id, values):
        conditions = [{
            'column': 'id',
            'value': employee_id,
            'operator': '=',
            'options': ''
        }]
        if 'user' in values:
            user = values.pop('user')
            user_id = self.get_employee_user(employee_id)
            self.user_dao.update_user(user_id, user)
        return self.update(conditions=conditions, values=values)

    def get_employee_user(self, employee_id):
        user_id = self.select(columns=['user_id'], conditions=[{
            'column': 'id',
            'value': employee_id,
            'operator': '=',
            'options': '',
            'logic': ''
        }])
        if user_id and user_id.first():
            return user_id.value('user_id')
        return None

    def delete_employee(self, employee_id):
        user_id = self.get_employee_user(employee_id)
        return self.user_dao.delete(conditions=[{
            'column': 'id',
            'value': user_id,
            'operator': '=',
            'options': ''
        }])

    def get_objects_dataframe(self, objects):
        objects_data_frame = pd.DataFrame()

