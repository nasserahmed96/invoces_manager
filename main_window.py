import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QMainWindow
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from python_forms.main_window_GUI import Ui_MainWindow
from employees_manager import EmployeesManager
from system_properties import SystemProperties
from products_main_window import ProductsMainWindow
from helpers import open_window

class AppMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AppMainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initializeUI()

    def initializeUI(self):
        self.ui.employees_btn.clicked.connect(lambda: open_window(self, EmployeesManager))
        self.ui.system_properties_btn.clicked.connect(lambda: open_window(self, SystemProperties))
        self.ui.products_btn.clicked.connect(lambda: open_window(self, ProductsMainWindow))
