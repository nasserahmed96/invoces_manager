import sys
from PyQt5.QtWidgets import QApplication, QCompleter, QMessageBox
from PyQt5.QtCore import Qt
from python_forms.productsManager_GUI import Ui_productsManagerWindow
from src.create_product import CreateProduct
from src.helpers import get_table_data, open_window, initialize_combo_box

from src.Managers.base_manager import BaseManager


class ProductsManager(BaseManager):
    def __init__(self, parent=None):
        super(ProductsManager, self).__init__(parent=parent)
        self.ui = Ui_productsManagerWindow()
        self.ui.setupUi(self)
        self.initialize_db()
        self.initialize_required_data()
        self.initializeUI()
        self.setUpModel()
        self.setUpTableView()
        self.connect_signals_slots()
        self.search_critieria = []

    def initialize_required_data(self):
        self.products_categories = get_table_data('categories')
        self.products_brands = get_table_data('brands')
        self.status = get_table_data('status')


    def build_conditions(self):
        """
        This function builds conditions for the SELECT query, based on whether the required widget has something in it
        or not
        :return:
        """
        conditions = []
        conditions.append(
            {
                "column": "products.name",
                "value": f"'{self.ui.product_name_line_edit.text()}'",
                "operator": "=",
                "options": "COLLATE NOCASE"
            }
        ) if self.ui.product_name_line_edit.text() != "" else None

        conditions.append(
            {
                "column": "brands.id",
                "value": self.products_brands[self.ui.product_brand_cb.currentText()],
                "operator": "=",
                "options": ""
            }) if self.ui.product_brand_cb.currentText() != "All" else None

        conditions.append(
            {
                "column": "categories.id",
                "value": self.products_categories[self.ui.product_category_cb.currentText()],
                "operator": "=",
                "options": ""
            }
        ) if self.ui.product_category_cb.currentText() != "All" else None
        conditions.append(
            {
                "column": "status.id",
                "value": self.status[self.ui.product_status_cb.currentText()],
                "operator": "=",
                "options": ""
            }
        ) if self.ui.product_status_cb.currentText() != "All" else None
        conditions.append(
            {
                "column": "products.barcode",
                "value": f"'{self.ui.bar_code_line_edit.text()}'",
                "operator": '=',
                'options': 'COLLATE NOCASE'
            }
        ) if self.ui.bar_code_line_edit.text() != "" else None
        return ' WHERE ' + ' AND '.join([self.get_condition_string(condition) for condition in conditions]) if any(conditions) else ""

    def get_condition_string(self, condition):
        """
        Get a condition string out of a condition object
        :param condition: A condition object contains the required parameters for the condition
        :return: A condition string to be used in SQL query
        """
        return f"{condition['column']} {condition['operator']} {condition['value']} {condition['options']}"


    def initializeUI(self):
        self.initialize_combo_boxes()
        products_name_completer = QCompleter(get_table_data('products'))
        products_name_completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.product_name_line_edit.setCompleter(products_name_completer)

    def connect_signals_slots(self):
        self.ui.create_btn.clicked.connect(lambda: open_window(self, CreateProduct))
        self.ui.delete_btn.clicked.connect(self.delete)
        self.ui.search_btn.clicked.connect(self.search)
        self.model.dataChanged.connect(self.item_changed)

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

    def search(self):
        print("Conditions: ", self.build_conditions())
        query_str = f"""
        SELECT products."id",
        products."name",
        products."description",
        categories.name AS categories_name_4,
        products."barcode",
        products."price",
        status.name AS status_name_3,
        products."quantity",
        products."notes",
        brands.name AS brands_name_2 
        FROM products 
        LEFT JOIN categories ON products."category"=categories.id 
        LEFT JOIN status ON products."status"=status.id 
        LEFT JOIN brands ON products."brand"=brands.id 
        {self.build_conditions()} ORDER BY products."id" DESC
        """
        query = QSqlQuery(query_str)
        self.model.setQuery(query)
        print("Query: ", self.model.query().lastQuery())
        print("Query error: ", self.model.query().lastError().text())


    def initialize_combo_boxes(self):
        initialize_combo_box(self.ui.product_category_cb, self.products_categories.keys(), 'All')
        initialize_combo_box(self.ui.product_brand_cb, self.products_brands.keys(), 'All')
        initialize_combo_box(self.ui.product_status_cb, self.status.keys(), 'All')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductsManager()
    window.show()
    sys.exit(app.exec_())