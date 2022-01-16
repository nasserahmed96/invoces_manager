from PyQt5.QtWidgets import QWidget, QStyleOption, QStyle
from PyQt5.QtGui import QPainter
from python_forms.sidebar_GUI import Ui_SideBar
from helpers import open_window
from src.Managers.employees_manager import EmployeesManager
from system_properties import SystemProperties
from products_main_window import ProductsMainWindow


class SideBar(QWidget):
    def __init__(self, parent):
        super(SideBar, self).__init__(parent=parent)
        self.ui = Ui_SideBar()
        self.ui.setupUi(self)
        self.style_sheet = """
         QWidget#SideBar
        {
            background-color: white;
        }
        QPushButton
            { 
                background-color: #FFFFFF;
                color: rgb(190, 190, 190);
                border: none;
                color: white;
                text-align: left;
                text-decoration: none;
                color: black;
                padding: 1px;
            }
            QPushButton:hover{
                background-color: grey;
            }
            QPushButton:hover:pressed{
                background-color: #bebebe;
            }

        """
        self.connect_signals_slots()
        self.show()

    def connect_signals_slots(self):
        self.ui.employees_btn.clicked.connect(
            lambda: open_window(**{'parent_window': self, 'window': EmployeesManager}))
        self.ui.system_properties_btn.clicked.connect(
            lambda: open_window(**{'parent_window': self, 'window': SystemProperties}))
        self.ui.products_btn.clicked.connect(
            lambda: open_window(**{'parent_window': self, 'window': ProductsMainWindow}))

    def paintEvent(self, event):
        self.setStyleSheet(self.style_sheet)
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)




