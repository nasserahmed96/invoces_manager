from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex, QVariant
from src.DataAccessObjects.ProductDao import ProductDao


class ProductsTableModel(QAbstractTableModel):
    def __init__(self):
        super(ProductsTableModel, self).__init__()
        self.products_dao = ProductDao()
        self.products_dataframe = self.products_dao.get_products_dataframe()
        self.columns = self.products_dataframe.columns

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
        return QVariant

    def get_products(self):
        return self.products_dataframe



