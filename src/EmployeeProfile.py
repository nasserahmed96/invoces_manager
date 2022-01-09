from PyQt5.QtWidgets import QWidget, QMainWindow
from src.DataObjects.Employee import Employee
from src.DataAccessObjects.EmployeeDao import EmployeeDao
from python_forms.employeeProfile_GUI import Ui_employeeProfileWindow


class EmployeeProfile(QMainWindow):
    def __init__(self, employee_id, parent=None):
        super(EmployeeProfile, self).__init__(parent)
        self.ui = Ui_employeeProfileWindow()
        self.ui.setupUi(self)
        self.employee_id = employee_id
        self.employee_dao = EmployeeDao()
        self.get_employee()
        self.initializeUI()
        self.show()

    def get_employee(self):
        self.employee = self.employee_dao.get_employee_by_id(employee_id=self.employee_id)
        print('Employee: ', self.employee)

    def initializeUI(self):
        self.ui.firstNameLineEdit.setText(self.employee.user.first_name)
        self.ui.middleNameLineEdit.setText(self.employee.user.middle_name)
        self.ui.lastNameLineEdit.setText(self.employee.user.last_name)
        self.ui.userNameLineEdit.setText(self.employee.username)
        self.ui.phoneNumberLineEdit.setText(self.employee.user.phone_number)
        self.ui.emailLineEdit.setText(self.employee.user.email)
        self.ui.addressLineEdit.setText(self.employee.user.address)