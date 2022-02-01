from PyQt5.QtCore import QAbstractTableModel
from src.DataAccessObjects.InvoiceDao import InvoiceDao
from src.Logger import Logger


class InvoicesTableModel(QAbstractTableModel):
    def __init__(self):
        super(InvoicesTableModel, self).__init__()
        self.invoice_dao = InvoiceDao()
        self.invoices_dataframe = self.invoice_dao.get_invoices_dataframe()
        self.columns = self.invoices_dataframe.columns

