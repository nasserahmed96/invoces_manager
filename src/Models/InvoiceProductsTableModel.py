from decimal import Decimal
import pandas as pd
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant


class InvoiceProductsTableModel(QAbstractTableModel):
    def __init__(self):
        super(InvoiceProductsTableModel, self).__init__()
        self.columns = ['Id', 'Name', 'Description', 'Price', 'Quantity', 'Total']
        self.invoice_products_dataframe = pd.DataFrame({column_name: [] for column_name in self.columns})
        self.invoice_products_dataframe.set_index('Id')
        self.columns_dict = {self.columns[index]: index for index in range(len(self.columns))}

    def rowCount(self, parent=QModelIndex()):
        return self.invoice_products_dataframe.shape[0]

    def columnCount(self, parent=QModelIndex()):
        return len(self.invoice_products_dataframe.columns)

    def headerData(self, section, orientation=Qt.Horizontal, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.columns[section]

    def data(self, index=QModelIndex(), role=Qt.DisplayRole):
        if index.isValid() and (role == Qt.DisplayRole or role == Qt.EditRole) :
            return str(self.get_invoice_products().iat[index.row(), index.column()]) if not \
                index.column() == self.get_column_index('Id') else str(self.get_invoice_products().index[index.row()])
        return QVariant()

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and role == Qt.EditRole:
            self.edit_product(index.row(), value)
            self.update_total_price_for_product(index.row())
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        if index.column() == self.get_column_index('Quantity'):
            return Qt.ItemIsEditable | Qt.ItemIsEnabled
        return QAbstractTableModel.flags(self, index) | Qt.ItemIsEnabled

    def removeRow(self, row, parent=QModelIndex()):
        self.beginRemoveRows(parent, row, row)
        self.invoice_products_dataframe = self.invoice_products_dataframe.drop(index=self.get_index_by_row(row))
        self.dataChanged.emit(parent, parent)
        self.endRemoveRows()

    def edit_product(self, row, value):
        self.invoice_products_dataframe.loc[self.invoice_products_dataframe.index[row], 'Quantity'] = value

    def update_total_price_for_product(self, row):
        self.invoice_products_dataframe.loc[self.get_index_by_row(row), 'Total'] = \
            (Decimal(self.invoice_products_dataframe.loc[self.get_index_by_row(row), 'Price']) *
             Decimal(self.invoice_products_dataframe.loc[self.get_index_by_row(row), 'Quantity'])).quantize(Decimal('.00'))

    def get_index_by_row(self, row):
        return self.invoice_products_dataframe.index[row]

    def append_product(self, product_row):
        num_row = self.invoice_products_dataframe.shape[0]
        self.beginInsertRows(QModelIndex(), num_row, num_row)
        temp_dataframe = pd.DataFrame([product_row])
        temp_dataframe = temp_dataframe.set_index('Id')
        self.invoice_products_dataframe = self.invoice_products_dataframe.append(temp_dataframe,
                                                                                 verify_integrity=True)
        self.dataChanged.emit(QModelIndex(), QModelIndex())
        self.endInsertRows()

    def get_invoice_products(self):
        return self.invoice_products_dataframe

    def get_column_index(self, column_name):
        return self.columns_dict[column_name]