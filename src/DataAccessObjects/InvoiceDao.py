from src.DataAccessObjects.DataAccessObject import DataAccessObject


class InvoiceDao(DataAccessObject):
    def __init__(self):
        super(InvoiceDao, self).__init__(table_name='invoices')

