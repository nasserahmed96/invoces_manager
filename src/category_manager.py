import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QCompleter
from src.base_manager import BaseManager
from python_forms.categoryManager_GUI import Ui_categories_manager
from src.Models.CategoriesTableModel import CategoriesTableModel
from src.create_category import CreateCategory


class CategoriesManager(BaseManager):
    def __init__(self, parent=None):
        super(CategoriesManager, self).__init__(parent=parent, model=CategoriesTableModel(), ui=Ui_categories_manager())

    def connect_signals_slots(self):
        super(CategoriesManager, self).connect_signals_slots()
        self.ui.search_btn.clicked.connect(self.search)
        self.ui.create_btn.clicked.connect(self.open_create_category)

    def open_create_category(self):
        create_category = CreateCategory(self)
        create_category.show()

    def initialize_ui(self):
        super(CategoriesManager, self).initialize_ui()
        completer = QCompleter(self.model.get_completer_data())
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.ui.name_line_edit.setCompleter(completer)

    def setup_table(self):
        self.ui.category_table_view.setModel(self.model)

    def search(self):
        conditions = []
        conditions.append(
            self.build_condition('categories.name', self.ui.name_line_edit.text(), '=', 'COLLATE NOCASE')) if self.ui.name_line_edit.text() != '' else None
        self.model.select(conditions=conditions)
        self.ui.category_table_view.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    category_manager = CategoriesManager()
    category_manager.show()
    sys.exit(app.exec_())




