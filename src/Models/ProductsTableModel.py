from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex, QVariant, QAbstractItemModel
from PyQt5.QtWidgets import QCompleter
from src.DataAccessObjects.ProductDao import ProductDao


class ProductsTableModel(QAbstractTableModel):
    def __init__(self):
        super(ProductsTableModel, self).__init__()
        self.products_dao = ProductDao()
        self.products_dataframe = self.products_dao.get_products_dataframe()
        self.columns = self.products_dataframe.columns
        self.columns_dict = {self.columns[index]: index for index in range(len(self.columns))}

    def columnCount(self, parent=QModelIndex()):
        return len(self.columns)

    def rowCount(self, parent=QModelIndex()):
        return self.products_dataframe.shape[0]

    def headerData(self, section, orientation=Qt.Horizontal, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.columns[section]

    def data(self, index=QModelIndex(), role=Qt.DisplayRole):
        if not index.isValid():
            return QVariant()
        if role == Qt.DisplayRole:
            return str(self.get_products().iat[index.row(), index.column()])
        return QVariant()

    def get_products(self):
        return self.products_dataframe

    def select(self, conditions='', placeholders=''):
        self.products_dataframe = self.products_dao.get_products_dataframe(conditions=conditions, placeholders=placeholders)
        self.dataChanged.emit(QModelIndex(), QModelIndex())

    def get_completer(self, col_name):
        completer = QCompleter(self.products_dao.get_data_for_completer(col_name))
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        return completer

    def get_column_index(self, column_name):
        return self.columns_dict[column_name]



