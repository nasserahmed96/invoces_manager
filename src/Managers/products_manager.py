import re
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QHeaderView
from python_forms.products_manager_GUI import Ui_productsManagerWindow
from src.create_product import CreateProduct
from src.helpers import get_table_data, open_window, initialize_combo_box
from src.Managers.base_manager import BaseManager
from src.Models.ProductsTableModel import ProductsTableModel


class ProductsManager(BaseManager):
    def __init__(self, parent=None):
        self.initialize_required_data()
        super(ProductsManager, self).__init__(parent=parent,
                                              ui=Ui_productsManagerWindow(),
                                              model=ProductsTableModel())
        self.connect_signals_slots()
        self.search_critieria = []

    def initialize_required_data(self):
        self.products_categories = get_table_data('categories')
        self.products_brands = get_table_data('brands')
        self.status = get_table_data('status')

    def search(self):
        conditions = []
        conditions.append(
            self.build_condition(column="products.name", value=self.ui.product_name_line_edit.text(),
                                 operator='=', options="COLLATE NOCASE", logic='AND')
        ) if self.ui.product_name_line_edit.text() != "" else None

        conditions.append(
            self.build_condition(column="brand.id",
                                 value=int(self.products_brands[self.ui.product_brand_cb.currentText()]),
                                 operator='=', options="", logic='AND')
        ) if self.ui.product_brand_cb.currentText() != "All" else None

        conditions.append(
            self.build_condition(column="category.id",
                                 value=int(self.products_categories[self.ui.product_category_cb.currentText()]),
                                 operator='=', options="", logic='AND')
        ) if self.ui.product_category_cb.currentText() != "All" else None
        conditions.append(
            self.build_condition(column="products.barcode",
                                 value=self.ui.bar_code_line_edit.text(),
                                 operator='=', options="", logic='AND')
        ) if self.ui.bar_code_line_edit.text() != "" else None

        self.model.select(re.sub('(AND|OR)$', '', self.build_conditions(conditions)), self.extract_values_from_conditions(conditions))
        self.ui.products_table_view.update()

    def initialize_ui(self):
        super(ProductsManager, self).initialize_ui()
        self.initialize_combo_boxes()
        self.ui.bar_code_line_edit.setCompleter(self.model.get_completer('products.barcode'))
        self.ui.product_name_line_edit.setCompleter(self.model.get_completer('products.name'))

    def setup_table(self):
        self.ui.products_table_view.setModel(self.model)

    def connect_signals_slots(self):
        self.ui.create_btn.clicked.connect(lambda: open_window(self, CreateProduct))
        self.ui.search_btn.clicked.connect(self.search)
        #self.model.dataChanged.connect(self.item_changed)

    def item_changed(self):
        msg_box = QMessageBox()
        msg_box.setText(self.tr('The document has been changed'))
        msg_box.setInformativeText(self.tr('Are you sure do you want save the changes?'))
        msg_box.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        return_value = msg_box.exec_()
        if return_value == QMessageBox.Save:
            self.model.submitAll()
        else:
            """
            Disconnect and reconnect dataChanged to prevent calling this function again after revertAll()
            """
            self.model.dataChanged.disconnect(self.item_changed)
            self.model.revertAll()
            self.model.dataChanged.connect(self.item_changed)

    def delete(self):
        selected_rows_indices = self.ui.products_table_view.selectionModel().selectedRows()
        print(selected_rows_indices)
        for row in sorted(selected_rows_indices):
            self.model.removeRow(row.row())
        msg_box = QMessageBox()
        msg_box.setText(self.tr('Delete items'))
        msg_box.setInformativeText(self.tr('Are you sure do you want to delete the selected rows?'))
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Discard | QMessageBox.Cancel)
        return_value = msg_box.exec_()
        if return_value == QMessageBox.Ok:
            self.model.submitAll()
        else:
            self.revert_changes()

    def revert_changes(self):
        """
        Disconnect and reconnect dataChanged to prevent calling this function again after revertAll()
        """
        self.model.dataChanged.disconnect(self.item_changed)
        self.model.revertAll()
        self.model.dataChanged.connect(self.item_changed)

    def initialize_combo_boxes(self):
        initialize_combo_box(self.ui.product_category_cb, self.products_categories.keys(), 'All')
        initialize_combo_box(self.ui.product_brand_cb, self.products_brands.keys(), 'All')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductsManager()
    window.show()
    sys.exit(app.exec_())