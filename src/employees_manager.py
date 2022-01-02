import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from python_forms.emplyees_manager_GUI import Ui_employee_management_window
from src.Models.EmployeesTableModel import EmployeesTableModel
from create_employee import CreateEmployee


class EmployeesManager(QMainWindow):
    def __init__(self):
        super(EmployeesManager, self).__init__()
        self.ui = Ui_employee_management_window()
        self.ui.setupUi(self)
        self.connect_signals_slots()
        self.initializeUI()

    def connect_signals_slots(self):
        self.ui.add_employee_btn.clicked.connect(self.open_create_employee)


    def open_create_employee(self):
        create_employee = CreateEmployee()
        create_employee.show()

    def initializeUI(self):
        self.setupTable()

    def setupTable(self):
        self.model = EmployeesTableModel()
        self.ui.employees_table_view.setModel(self.model)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmployeesManager()
    window.show()
    sys.exit(app.exec_())