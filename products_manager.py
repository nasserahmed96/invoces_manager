import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QStandardItem, QStandardItemModel, Qt
from PyQt5.QtSql import QSqlQuery, QSqlDatabase
from python_forms.productsManager_GUI import Ui_productsManagerWindow
from create_product import CreateProduct
from helpers import get_table_data, open_window
from models import Product

class ProductsManager(QMainWindow):
    def __init__(self):
        super(ProductsManager, self).__init__()
        self.ui = Ui_productsManagerWindow()
        self.ui.setupUi(self)
        self.initialize_db()
        self.initializeUI()
        self.setUpTable()
        self.get_products()
        self.search_critieria = []

    def setUpTable(self):
        self.model = QStandardItemModel()
        self.ui.products_table_view.setModel(self.model)
        self.ui.products_table_view.setSelectionMode(4)
        self.ui.products_table_view.setSelectionBehavior(1)
        self.ui.products_table_view.setSortingEnabled(True)


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
                "value": self.ui.product_name_line_edit.text(),
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
                "column": "products.barcode",
                "value": self.ui.bar_code_line_edit.text(),
                "operator": '=',
                'options': 'COLLATE NOCASE'
            }
        ) if self.ui.bar_code_line_edit.text() != "" else None
        return 'WHERE ' + 'AND '.join([self.get_condition_string(condition) for condition in conditions]) if any(conditions) else ""

    def get_condition_string(self, condition):
        """
        Get a condition string out of a condition object
        :param condition: A condition object contains the required parameters for the condition
        :return: A condition string to be used in SQL query
        """
        return f"{condition['column']} {condition['operator']} {condition['value']} {condition['options']}"


    def get_products(self):
        query_str = f"""
        SELECT 
        products.id,
        products.name, 
        products.description, 
        products.price, 
        products.quantity, 
        products.barcode,
        categories.name AS category_name,
        brands.name as brand_name
        FROM products 
        LEFT JOIN brands ON products.brand=brands.id 
        LEFT JOIN categories ON products.category=categories.id {self.build_conditions()}
        """
        query = self.execute_select_query(query_str)
        self.model.clear()
        while(query.next()):
            self.model.appendRow([QStandardItem(str(query.value(i))) for i in range(0, query.record().count())])
        #QStandard model needs to know the number of columns before writing headers
        self.model.setHorizontalHeaderLabels(["ID", "Name", "Description", "Price", "Quantity", "Bar code", "Category", "Brand"])


    def execute_select_query(self, query_str):
        query = QSqlQuery()
        query.exec_(query_str)
        return query

    def initialize_db(self):
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName("clear_vision.db")
        if not database.open():
            print("Unable to open database")
            sys.exit(1)

    def initializeUI(self):
        self.connect_signals_slots()
        self.initialize_combo_boxes()

    def connect_signals_slots(self):
        self.ui.create_btn.clicked.connect(lambda: open_window(self, CreateProduct))
        self.ui.search_btn.clicked.connect(self.get_products)
        self.ui.edit_btn.clicked.connect(self.edit_product)

    def edit_product(self):
        #Get only the first selected item
        selected_index = self.ui.products_table_view.selectedIndexes()[0]
        print("Row: ", self.model.item(selected_index.row(), 1).text())





    def initialize_combo_boxes(self):
        self.products_categories = get_table_data("categories")
        self.products_brands = get_table_data("brands")
        self.ui.product_category_cb.addItems(self.products_categories.keys())
        self.ui.product_brand_cb.addItems(self.products_brands.keys())
        self.ui.product_category_cb.addItem("All")
        self.ui.product_brand_cb.addItem("All")
        self.ui.product_category_cb.setCurrentText("All")
        self.ui.product_brand_cb.setCurrentText("All")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductsManager()
    window.show()
    sys.exit(app.exec_())