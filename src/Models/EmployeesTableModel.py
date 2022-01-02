from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant
from PyQt5.QtGui import QColor
from src.DataAccessObjects.EmployeeDao import EmployeeDao
import numpy as np


class EmployeesTableModel(QAbstractTableModel):
    def __init__(self):
        super(EmployeesTableModel, self).__init__()
        self.employee_dao = EmployeeDao()
        self.employees_dataframe = self.employee_dao.get_employees_dataframe()
        self.columns = self.employees_dataframe.columns

    def get_employees(self):
        return self.employees_dataframe

    def rowCount(self, parent=QModelIndex()):
        return self.get_employees().shape[0]

    def columnCount(self, parent=QModelIndex()):
        return len(self.columns)

    def headerData(self, section: int, orientation=Qt.Horizontal, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.columns[section]

    def data(self, index=QModelIndex(), role=Qt.DisplayRole):
        print('Index: ', index)
        print(f'Index row:  {index.row()} Role: {role}')
        if not index.isValid():
            print('Invalid')
            return QVariant()
        if role == Qt.DisplayRole:
            return self.get_employees().iat[index.row(), index.column()]
        return QVariant()

    def roleNames(self):
        roles = {
            'First name': Qt.UserRole + 1,
            'Middle name': Qt.UserRole + 2
        }
        return roles


