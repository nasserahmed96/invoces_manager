from src.Managers.base_manager import BaseManager
from python_forms.invoices_manager_GUI import Ui_invoicesManagerWindow
from src.Models.InvoiceProductsTableModel import InvoiceProductsTableModel
from src.create_invoice import CreateInvoice


class InvoicesManager(BaseManager):
    def __init__(self, parent=None):
        super(InvoicesManager, self).__init__(ui=Ui_invoicesManagerWindow(), parent=parent,
                                              model=InvoiceProductsTableModel())

    def connect_signals_slots(self):
        self.ui.add_new_invoice_btn.clicked.connect(self.open_create_invoice)

    def open_create_invoice(self):
        create_invoice = CreateInvoice(self)
        create_invoice.show()
