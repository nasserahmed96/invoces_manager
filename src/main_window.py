import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from python_forms.main_window_GUI import Ui_MainWindow
from employees_manager import EmployeesManager
from system_properties import SystemProperties
from customers_manager import CustomersManager
from products_main_window import ProductsMainWindow
from dashboard import Dashboard


class AppMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AppMainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initializePages()
        self.connect_signals_slots()
        self.ui.window_content.setCurrentIndex(0)

    def connect_signals_slots(self):
        self.ui.employees_btn.clicked.connect(
            lambda: self.change_widget(self.widgets["employees_manager"]["index"]))
        self.ui.system_properties_btn.clicked.connect(
            lambda: self.change_widget(self.widgets["system_properties"]["index"]))
        self.ui.customers_btn.clicked.connect(
            lambda: self.change_widget(self.widgets["customers_manager"]["index"]))
        self.ui.products_btn.clicked.connect(
            lambda: self.change_widget(self.widgets["products_main_window"]["index"]))

    def initializePages(self):
        self.widgets = {
            "dashboard":
                {"index": 0, "widget": Dashboard()},
            "system_properties":
                {"index": 1, "widget": SystemProperties()},
            "employees_manager":
                {"index": 2, "widget": EmployeesManager()},
            "customers_manager":
                {"index": 3, "widget": CustomersManager()},
            "products_main_window":
                {"index": 4, "widget": ProductsMainWindow()}
        }
        [self.ui.window_content.insertWidget(self.widgets[widget]["index"], self.widgets[widget]["widget"]) for widget in self.widgets]


    def change_widget(self, index):
        """
        Change the stacked widget to the widget at index
        :param index:Integer represents the widget's index in the stacked widget
        :return: None
        """
        self.ui.window_content.setCurrentIndex(index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppMainWindow()
    window.show()
    sys.exit(app.exec_())