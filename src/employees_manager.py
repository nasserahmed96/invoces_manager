import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QHeaderView, QWidget
from PyQt5.QtGui import QStandardItemModel
from python_forms.emplyees_manager_GUI import Ui_employee_management_window
from src.Models.EmployeesTableModel import EmployeesTableModel
from create_employee import CreateEmployee
from helpers import open_window


class EmployeesManager(QMainWindow):
    def __init__(self):
        super(EmployeesManager, self).__init__()
        self.ui = Ui_employee_management_window()
        self.ui.setupUi(self)
        self.initializeUI()

    def initializeUI(self):
        #self.ui.add_employee_btn.clicked.connect(lambda: open_window(self, CreateEmployee))
        self.setupTable()

    def setupTable(self):
        self.model = EmployeesTableModel()
        #self.model.setHorizontalHeaderLabels(["First name", "Middle name", "Last name", "Email", "Phone number"])
        self.ui.employees_table_view.setModel(self.model)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmployeesManager()
    window.show()
    sys.exit(app.exec_())