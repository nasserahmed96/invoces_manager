import sys
from PyQt5.QtWidgets import QWidget, QApplication
from python_forms.system_properties_GUI import Ui_systemProperties
from create_objec_name_desc import CreateObjNameDesc
from helpers import open_window

class SystemProperties(QWidget):
    def __init__(self):
        super(SystemProperties, self).__init__()
        self.ui = Ui_systemProperties()
        self.ui.setupUi(self)
        self.initializeUI()

    def initializeUI(self):
        self.ui.job_titles_btn.clicked.connect(lambda: open_window(**{'parent_window': self, 'window': CreateObjNameDesc,
                                                                   'table_name': 'job_titles', 'window_title': 'job title'}))
        self.ui.groups_btn.clicked.connect(lambda: open_window(**{'parent_window': self, 'window': CreateObjNameDesc,
                                                                   'table_name': 'groups', 'window_title': 'group'}))
        self.ui.status_btn.clicked.connect(lambda: open_window(**{'parent_window': self, 'window': CreateObjNameDesc,
                                                                   'table_name': 'status', 'window_title': 'status'}))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SystemProperties()
    window.show()
    sys.exit(app.exec_())