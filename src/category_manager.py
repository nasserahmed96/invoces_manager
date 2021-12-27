from PyQt5.QtWidgets import QMainWindow
from python_forms.categoryManager_GUI import Ui_categories_manager
from src.create_category import CreateCategory
from src.helpers import open_window


class CategoryManager(QMainWindow):
    def __init__(self):
        super(CategoryManager, self).__init__()
        self.ui = Ui_categories_manager()
        self.ui.setupUi(self)
        self.initializeUI()

    def initializeUI(self):
        self.ui.create_btn.clicked.connect(lambda: open_window(self, CreateCategory))


