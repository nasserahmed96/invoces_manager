from PyQt5.QtWidgets import QMainWindow
from python_forms.productsMainWindow_GUI import Ui_products_main_window
from brands_manager import BrandsManager
from category_manager import CategoriesManager
from products_manager import ProductsManager
from src.helpers import open_window


class ProductsMainWindow(QMainWindow):
    def __init__(self):
        super(ProductsMainWindow, self).__init__()
        self.ui = Ui_products_main_window()
        self.ui.setupUi(self)
        self.initializeUI()

    def initializeUI(self):
        self.ui.brands_btn.clicked.connect(lambda: open_window(self, BrandsManager))
        self.ui.categories_btn.clicked.connect(lambda: open_window(self, CategoriesManager))
        self.ui.products_btn.clicked.connect(lambda: open_window(self, ProductsManager))
