from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant
from src.DataAccessObjects.CustomerDao import CustomerDao
from src.Logger import Logger


class CustomerTableModel(QAbstractTableModel):
    def __init__(self):
        super(CustomerTableModel, self).__init__()
        self.customer_dao = CustomerDao()
        self.customers_dataframe = self.customer_dao.get_customers_dataframe()
        self.columns = self.customers_dataframe.columns
        self.logger = Logger()

    def select(self, conditions=None, placeholders=None):
        print('Conditions: ', conditions)
        print('Place holders: ', placeholders)
        self.customers_dataframe = self.customer_dao.get_customers_dataframe(conditions=conditions, placeholders=placeholders)
        print('Search result: ', self.customers_dataframe)
        self.dataChanged.emit(QModelIndex(), QModelIndex())

    def get_customers(self):
        return self.customers_dataframe

    def rowCount(self, parent=QModelIndex()):
        return self.get_customers().shape[0]

    def columnCount(self, parent=QModelIndex()):
        return len(self.columns)

    def headerData(self, section: int, orientation=Qt.Horizontal, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.columns[section]

    def data(self, index=QModelIndex(), role=Qt.DisplayRole):
        if not index.isValid():
            self.logger.error('Invalid index')
            return QVariant()
        if role == Qt.DisplayRole:
            return str(self.get_customers().iat[index.row(), index.column()])
        return QVariant()

    def save(self, customer):
        return self.customer_dao.create_customer(customer)


