from PyQt5.QtWidgets import QMainWindow
from python_forms.brandsManager_GUI import Ui_brands_manager
from create_brand import CreateBrand
from helpers import open_window

class BrandManager(QMainWindow):
    def __init__(self):
        super(BrandManager, self).__init__()
        self.ui = Ui_brands_manager()
        self.ui.setupUi(self)
        self.initializeUI()

    def initializeUI(self):
        self.ui.create_btn.clicked.connect(lambda: open_window(self, CreateBrand))
