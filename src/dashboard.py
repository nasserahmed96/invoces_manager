from PyQt5.QtWidgets import QWidget
from python_forms.dashboard_GUI import Ui_dashboard_widget


class Dashboard(QWidget):
    def __init__(self, parent=None):
        super(Dashboard, self).__init__(parent=parent)
        self.ui = Ui_dashboard_widget()
        self.ui.setupUi(self)