import sys
from PyQt5.QtWidgets import QApplication
from python_forms.brandsManager_GUI import Ui_brands_manager
from src.base_manager import BaseManager
from src.Models.BrandsTableModel import BrandsTableModel
from src.create_brand import CreateBrand


class BrandsManager(BaseManager):
    def __init__(self, parent=None):
        super(BrandsManager, self).__init__(parent=parent, model=BrandsTableModel(), ui=Ui_brands_manager())

    def setup_table(self):
        self.ui.brand_table_view.setModel(self.model)

    def connect_signals_slots(self):
        self.ui.create_btn.clicked.connect(self.open_create_brand)

    def open_create_brand(self):
        create_brand = CreateBrand(self)
        create_brand.show()

    def search(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BrandsManager()
    window.show()
    sys.exit(app.exec_())
