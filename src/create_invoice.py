import sys
from decimal import Decimal
from PyQt5.QtWidgets import QApplication, QMessageBox, QCompleter
from python_forms.create_invoice_GUI import Ui_createInvoiceWindow
from src.Managers.products_manager import ProductsManager
from src.SpinBoxDelegate import SpinBoxDelegate
from src.Models.InvoiceProductsTableModel import InvoiceProductsTableModel
from src.Models.EmployeesSharesTableModel import EmployeesSharesTableModel


class CreateInvoice(ProductsManager):
    def __init__(self):
        self.invoice_products_model = InvoiceProductsTableModel()
        self.employees_shares_model = EmployeesSharesTableModel()
        super(CreateInvoice, self).__init__(ui=Ui_createInvoiceWindow())
        self.employees_usernames = self.employees_shares_model.get_employees_data()
        self.ui.employees_usernames_cb.addItems(self.employees_usernames)

    def initialize_ui(self):
        super(CreateInvoice, self).initialize_ui()
        self.ui.employees_usernames_cb.setCompleter(self.employees_shares_model.get_completer('employees.username'))

    def setup_table(self):
        super(CreateInvoice, self).setup_table()
        self.ui.invoice_products_table_view.setModel(self.invoice_products_model)
        self.ui.invoice_products_table_view.setItemDelegateForColumn(self.invoice_products_model.get_column_index('Quantity'), SpinBoxDelegate())
        self.ui.employees_table_view.setModel(self.employees_shares_model)
        self.ui.employees_table_view.setItemDelegateForColumn(self.employees_shares_model.get_column_index('Percentage'), SpinBoxDelegate(maximum_value=100))

    def connect_signals_slots(self):
        super(CreateInvoice, self).connect_signals_slots()
        self.ui.products_table_view.doubleClicked.connect(self.add_product_to_invoice)
        self.invoice_products_model.dataChanged.connect(self.data_changed)
        self.ui.accessories_spin_box.valueChanged.connect(self.calculate_total_invoice)
        self.ui.above_installation_spin_box.valueChanged.connect(self.calculate_total_invoice)
        self.ui.invoice_products_table_view.doubleClicked.connect(self.remove_product_from_invoice)
        self.ui.append_employee_btn.clicked.connect(self.append_employee_share)
        self.ui.invoice_total_line_edit.textChanged.connect(self.calculate_percentage_values)

    def calculate_percentage_values(self, new_total):
        self.employees_shares_model.calculate_percentage_values(new_total)

    def append_employee_share(self):
        self.employees_shares_model.append_employee_share(self.get_employee_share())

    def get_employee_share(self):
        """
        Get a dictionary which holds a row to be appended in EmployeesSharesTableModel to be viewed in the view (whatever the
        view
        :return: A dictionary includes the required data for EmployeesSharesTableModel
        """
        return {'Id': self.employees_usernames[self.ui.employees_usernames_cb.currentText()],
                'Username': self.ui.employees_usernames_cb.currentText(),
                'Percentage': self.ui.employee_shares_sb.value(),
                'Value': self.get_employee_share_value(self.ui.employee_shares_sb.value())
                }

    def get_employee_share_value(self, percentage):
        """
        :param percentage: A float representing the employee percentage for the current invoice
        :return:
        """
        return (Decimal(Decimal(percentage) / 100).quantize(Decimal('.00')) * Decimal(
            self.ui.invoice_total_line_edit.text()).quantize(Decimal('.00'))).quantize(Decimal('.00'))

    def remove_product_from_invoice(self, index):
        if not index.column() == self.invoice_products_model.get_column_index('Quantity'):
            self.invoice_products_model.removeRow(index.row())

    def data_changed(self):
        self.calculate_total_invoice()

    def calculate_total_invoice(self):
        total = Decimal(self.invoice_products_model.get_invoice_products()['Total'].astype('float64').sum()).quantize(Decimal('.00'))
        total += Decimal(self.ui.accessories_spin_box.value()) + Decimal(self.ui.above_installation_spin_box.value())
        self.ui.invoice_total_line_edit.setText(str(total.quantize(Decimal('.00'))))

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