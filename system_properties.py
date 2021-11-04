import sys
from PyQt5.QtWidgets import QWidget
from python_forms.system_properties_GUI import Ui_systemProperties
from create_job_title import CreateJobTitle
from helpers import open_window

class SystemProperties(QWidget):
    def __init__(self):
        super(SystemProperties, self).__init__()
        self.ui = Ui_systemProperties()
        self.ui.setupUi(self)
        self.initializeUI()

    def initializeUI(self):
        self.ui.job_titles_btn.clicked.connect(lambda: open_window(self, CreateJobTitle))
        """
        self.ui.groups_btn.clicked.connect(lambda: open_window(self, Group))
        self.ui.status_btn.clicked.connect(lambda: open_window(self, Status))
        """