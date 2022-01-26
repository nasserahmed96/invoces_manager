from src.Managers.base_manager import BaseManager
from python_forms.invoices_manager_GUI import Ui_invoicesManagerWindow
from src.Models.InvoiceProductsTableModel import InvoiceProductsTableModel


class InvoicesManager(BaseManager):
    def __init__(self, parent=None):
        super(InvoicesManager, self).__init__(ui=Ui_invoicesManagerWindow(), parent=parent,
                                              model=InvoiceProductsTableModel())