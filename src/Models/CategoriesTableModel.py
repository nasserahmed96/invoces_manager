from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant
from src.DataAccessObjects.CategoryDao import CategoryDao


class CategoriesTableModel(QAbstractTableModel):
    def __init__(self):
        super(CategoriesTableModel, self).__init__()
        self.categories_dao = CategoryDao()
        self.categories_dataframe = self.categories_dao.get_categories_dataframe()
        self.columns = self.categories_dataframe.columns

    def rowCount(self, parent=QModelIndex()):
        return self.categories_dataframe.shape[0]

    def columnCount(self, parent=QModelIndex()):
        return len(self.columns)

    def headerData(self, section, orientation=Qt.Horizontal, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role ==  Qt.DisplayRole:
            return self.columns[section]

    def data(self, index=QModelIndex, role=Qt.DisplayRole):
        if not index.isValid():
            self.logger.error('Invalid index')
            return QVariant()
        if role == Qt.DisplayRole:
            print(str(self.get_categories().iat[index.row(), index.column()]))
            return str(self.get_categories().iat[index.row(), index.column()])
        return QVariant()

    def select(self, conditions=''):
        self.categories_dataframe = self.categories_dao.get_categories_dataframe(conditions=conditions)
        self.dataChanged.emit(QModelIndex(), QModelIndex())

    def get_categories(self):
        return self.categories_dataframe

    def get_completer_data(self):
        return self.categories_dao.get_data_for_completer('name')

    def save(self, category):
        return self.categories_dao.create_category(category)

