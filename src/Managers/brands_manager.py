import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QCompleter
from python_forms.brandsManager_GUI import Ui_brands_manager
from src.Managers.base_manager import BaseManager
from src.Models.BrandsTableModel import BrandsTableModel
from src.create_brand import CreateBrand


class BrandsManager(BaseManager):
    def __init__(self, parent=None):
        super(BrandsManager, self).__init__(parent=parent, model=BrandsTableModel(), ui=Ui_brands_manager())

    def setup_table(self):
        self.ui.brand_table_view.setModel(self.model)

    def initialize_ui(self):
        super(BrandsManager, self).initialize_ui()
        completer = QCompleter(self.model.get_completer_data())
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.ui.name_line_edit.setCompleter(completer)

    def connect_signals_slots(self):
        self.ui.create_btn.clicked.connect(self.open_create_brand)
        self.ui.search_btn.clicked.connect(self.search)

    def open_create_brand(self):
        create_brand = CreateBrand(self)
        create_brand.show()

    def search(self):
        conditions = []
        conditions.append(
            self.build_condition('brands.name', self.ui.name_line_edit.text(), '=', 'COLLATE NOCASE')) if self.ui.name_line_edit.text() != '' else None
        self.model.select(conditions)
        self.ui.brand_table_view.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BrandsManager()
    window.show()
    sys.exit(app.exec_())
