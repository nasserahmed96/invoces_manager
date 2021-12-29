from src.DataAccessObjects.DataAccessObject import DataAccessObject
from src.DataAccessObjects.UserDao import UserDao
from src.Authenticate import Authentication
from src.DataObjects.Employee import Employee


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

    def get_all_employees(self):
        employees = []
        query_str = """SELECT users.*, employees.id AS employee_id, 
        employees.username FROM employees INNER JOIN users ON users.id=employee_id"""
        query_result = self.execute_select_query(query_str=query_str)
        while(query_result.next()):
            user = self.user_dao.fill_user(query_result)
            employees.append(Employee(id=query_result.value('employee_id'),
                                      user=user,
                                      username=query_result.value('username')))
        return employees