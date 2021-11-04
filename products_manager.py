import sys
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from PyQt5.QtGui import QStandardItem, QStandardItemModel
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
        self.fillTable()
        self.search_critieria = []

    def setUpTable(self):
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Name", "Description", "Price", "Quantity", "Category", "Brand"])
        self.ui.products_table_view.setModel(self.model)

    def fillTable(self):
        items = []
        item = QStandardItemModel

    def build_conditions(self):
        condition_str = " WHERE "
        self.conditions = []
        if self.ui.product_name_line_edit.text() != "":
            self.conditions.append(
                {
                    "column": "products.name",
                    "value": self.ui.product_name_line_edit.text(),
                    "operator": "=",
                    "options": "COLLATE NOCASE"
                }
            )

        if self.ui.product_brand_cb.currentText() != "All":
            self.conditions.append(
                {
                    "column": "products.brand",
                    "value": self.products_brands[self.ui.product_brand_cb.currentText()],
                    "operator": "=",
                    "options": ""
                })

    def get_combobox_filter_object(self, combo_box, col_name:str, operator:str, options:str, default_value="All"):
        """
        :param combo_box: The combo box object that we need to filter against
        :param col_name: The column name in the database
        :param operator: The operator to be used in the query
        :param options: More additional options for the query
        :param default_value: The default value of the ComboBox, we check if it's changed or not,
        :return: if default value is changed we will
        return a dictionary containing the object to be inserted in the Query, if it's a default it will return an
        empty string
        """
        if combo_box.currentText() != default_value:
               return {
                   "column": col_name,
                   "value": combo_box.currentText(),
                   "operator": operator,
                   "options": options
               }
        return ""




    def search(self):
        self.build_conditions()


    def get_products(self):
        query_str = """
        SELECT products.name, products.description, products.price, products.quantity, categories.name, brands.name 
        FROM products 
        INNER JOIN brands ON products.brand=brands.id 
        INNER JOIN categories ON products.category=categories.id
        """
        condition_str = " WHERE "
        if self.ui.product_name_line_edit.text() != "":
            condition_str += f"""products.name """
        print("Query: ", query_str)
        products = []
        query = QSqlQuery()
        query.exec_(query_str)
        errors = query.lastError().text()
        print("Errors: ", errors)
        print("Query: ", query.record().count())

        while(query.next()):
            self.model.appendRow([QStandardItem(str(query.value(i))) for i in range(0, query.record().count())])

    def initialize_db(self):
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName("clear_vision.db")
        if not database.open():
            print("Unable to open database")
            sys.exit(1)

    def initializeUI(self):
        self.products_categories = get_table_data("categories")
        self.products_brands = get_table_data("brands")
        self.ui.search_btn.clicked.connect(self.search)
        self.ui.product_category_cb.addItems(self.products_categories.keys())
        self.ui.product_brand_cb.addItems(self.products_brands.keys())
        self.ui.product_category_cb.setCurrentText("All")
        self.ui.product_brand_cb.setCurrentText("All")
        self.ui.create_btn.clicked.connect(lambda: open_window(self, CreateProduct))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductsManager()
    window.show()
    sys.exit(app.exec_())