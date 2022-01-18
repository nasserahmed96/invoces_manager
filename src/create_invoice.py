import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView
from python_forms.create_invoice_GUI import Ui_createInvoiceWindow
from src.Managers.products_manager import ProductsManager
from src.SpinBoxDelegate import SpinBoxDelegate
from src.Models.InvoiceProductsTableModel import InvoiceProductsTableModel

class CreateInvoice(ProductsManager):
    def __init__(self):
        self.invoice_products_model = InvoiceProductsTableModel()
        super(CreateInvoice, self).__init__(ui=Ui_createInvoiceWindow())


    def setup_table(self):
        super(CreateInvoice, self).setup_table()
        self.ui.invoice_products_table_view.setModel(self.invoice_products_model)
        self.ui.invoice_products_table_view.setItemDelegateForColumn(self.invoice_products_model.get_column_index('Quantity'), SpinBoxDelegate())

    def connect_signals_slots(self):
        super(CreateInvoice, self).connect_signals_slots()
        self.ui.products_table_view.doubleClicked.connect(self.add_product_to_invoice)
        self.invoice_products_model.dataChanged.connect(self.data_changed)

    def data_changed(self):
        print('Datachanged')
        self.ui.invoice_products_table_view.update()
        print(self.invoice_products_model.get_invoice_products())

    def add_product_to_invoice(self, selected_index):
        product_row = dict()
        product_row['Id'] = self.model.index(selected_index.row(), self.model.get_column_index('Id')).data()
        product_row['Name'] = self.model.index(selected_index.row(), self.model.get_column_index('Name')).data()
        product_row['Description'] = self.model.index(selected_index.row(), self.model.get_column_index('Description')).data()
        product_row['Price'] = self.model.index(selected_index.row(), self.model.get_column_index('Price')).data()
        product_row['Quantity'] = int(1)
        product_row['Total'] = product_row['Price'] * product_row['Quantity']
        self.invoice_products_model.append_product(product_row)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateInvoice()
    window.show()
    sys.exit(app.exec_())