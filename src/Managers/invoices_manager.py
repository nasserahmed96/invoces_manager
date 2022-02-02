import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from src.Managers.base_manager import BaseManager
from python_forms.invoices_manager_GUI import Ui_invoicesManagerWindow
from src.Models.InvoicesTableModel import InvoicesTableModel
from src.create_invoice import CreateInvoice


class InvoicesManager(BaseManager):
    def __init__(self, parent=None):
        super(InvoicesManager, self).__init__(ui=Ui_invoicesManagerWindow(), parent=parent,
                                              model=InvoicesTableModel())

    def setup_table(self):
        self.ui.invoices_table_view.setModel(self.model)

    def connect_signals_slots(self):
        self.ui.add_new_invoice_btn.clicked.connect(self.open_create_invoice)
        self.ui.search_btn.clicked.connect(self.search)
        self.ui.search_date_chbox.stateChanged.connect(self.enable_date)

    def enable_date(self, state):
        if state == Qt.Checked:
            self.ui.from_date_edit.setEnabled(True)
            self.ui.to_date_edit.setEnabled(True)
        else:
            self.ui.from_date_edit.setEnabled(False)
            self.ui.to_date_edit.setEnabled(False)

    def search(self):
        conditions = []
        if self.ui.search_date_chbox.checkState() == Qt.Checked:
            conditions.extend([self.get_search_condition(column='date', value=f"{self.ui.from_date_edit.text()}",
                                                         operator='>=', parameter='from_date'),
                               self.get_search_condition(column='date', value=f"{self.ui.to_date_edit.text()}",
                                                         operator='<=', logic='AND', parameter='to_date')])
        conditions.append(self.get_search_condition('serial_number', str(self.ui.invoice_serial_line_edit.text()), logic='AND')) if self.ui.invoice_serial_line_edit.text() != '' else None
        self.model.get_invoice_dataframe(conditions)
        self.ui.invoices_table_view.update()

    def get_search_condition(self, column, value, operator='=', options='', logic='', parameter=None):
        condition = {
            'column': column,
            'value': value,
            'operator': operator,
            'options': options,
            'logic': logic
        }
        if parameter:
            condition['parameter'] = parameter
        return condition

    def open_create_invoice(self):
        create_invoice = CreateInvoice(self)
        create_invoice.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    invoice_manager = InvoicesManager()
    invoice_manager.show()
    sys.exit(app.exec_())
