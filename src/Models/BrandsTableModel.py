from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant
from src.Logger import Logger
from src.DataAccessObjects.BrandDao import BrandDao


class BrandsTableModel(QAbstractTableModel):
    def __init__(self):
        super(BrandsTableModel, self).__init__()
        self.logger = Logger()
        self.brands_dao = BrandDao()
        self.brands_dataframe = self.brands_dao.get_brands_dataframe()
        self.columns = self.brands_dataframe.columns

    def rowCount(self, parent=QModelIndex):
        return self.brands_dataframe.shape[0]

    def columnCount(self, parent=QModelIndex):
        return len(self.columns)

    def headerData(self, section, orientation=Qt.Horizontal, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.columns[section]

    def data(self, index=QModelIndex, role=Qt.DisplayRole):
        if not index.isValid():
            self.logger.error('Invalid index')
            return QVariant()
        if role == Qt.DisplayRole:
            return str(self.get_brands().iat[index.row(), index.column()])
        return QVariant()

    def get_brands(self):
        return self.brands_dataframe

    def select(self, conditions=None):
        self.brands_dataframe = self.brands_dao.get_brands_dataframe(conditions=conditions)
        self.dataChanged.emit(QModelIndex(), QModelIndex())

    def save(self, brand):
        return self.brands_dao.create_brand(brand)