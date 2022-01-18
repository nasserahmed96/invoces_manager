import pandas as pd
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant


class InvoiceProductsTableModel(QAbstractTableModel):
    def __init__(self):
        super(InvoiceProductsTableModel, self).__init__()
        self.columns = ['Id', 'Name', 'Description', 'Price', 'Quantity', 'Total']
        self.invoice_products_dataframe = pd.DataFrame({column_name: [] for column_name in self.columns})
        self.columns_dict = {self.columns[index]: index for index in range(len(self.columns))}

    def rowCount(self, parent=QModelIndex()):
        return self.invoice_products_dataframe.shape[0]

    def columnCount(self, parent=QModelIndex()):
        return len(self.invoice_products_dataframe.columns)

    def headerData(self, section, orientation=Qt.Horizontal, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.columns[section]

    def data(self, index=QModelIndex(), role=Qt.DisplayRole):
        if index.isValid() and role == Qt.DisplayRole or role == Qt.EditRole:
            return str(self.get_invoice_products().iat[index.row(), index.column()])
        return QVariant()

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and role == Qt.EditRole:
            self.edit_product(index.row(), index.column(), value)
            self.update_total_price_for_product(index.row())
            self.dataChanged.emit(index, index)
            return True
        return False

    def edit_product(self, row, column, value):
        self.invoice_products_dataframe.iloc[row, column] = value

    def update_total_price_for_product(self, row):
        self.invoice_products_dataframe.iloc[row, self.get_column_index('Total')] = \
            float(self.invoice_products_dataframe.iloc[row, self.get_column_index('Price')]) * self.invoice_products_dataframe.iloc[row, self.get_column_index('Quantity')]

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        if index.column() == self.get_column_index('Quantity'):
            return Qt.ItemIsEditable | Qt.ItemIsEnabled
        return QAbstractTableModel.flags(self, index) | Qt.ItemIsEnabled

    def append_product(self, product_row):
        num_rows = self.invoice_products_dataframe.shape[0]
        self.beginInsertRows(QModelIndex(), num_rows, num_rows)
        self.invoice_products_dataframe = self.invoice_products_dataframe.append(product_row, ignore_index=True)
        self.dataChanged.emit(QModelIndex(), QModelIndex())
        self.endInsertRows()

    def get_invoice_products(self):
        return self.invoice_products_dataframe

    def get_column_index(self, column_name):
        return self.columns_dict[column_name]