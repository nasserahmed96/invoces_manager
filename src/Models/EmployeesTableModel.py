from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant
from src.DataAccessObjects.EmployeeDao import EmployeeDao
from src.Logger import Logger


class EmployeesTableModel(QAbstractTableModel):
    def __init__(self):
        super(EmployeesTableModel, self).__init__()
        self.employee_dao = EmployeeDao()
        self.employees_dataframe = self.employee_dao.get_employees_dataframe()
        self.columns = self.employees_dataframe.columns
        self.logger = Logger()

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
        if not index.isValid():
            self.logger.error('Invalid index')
            return QVariant()
        if role == Qt.DisplayRole:
            return str(self.get_employees().iat[index.row(), index.column()])
        return QVariant()

    def save(self, employee):
        return self.employee_dao.create_employee(employee.pop('employee'), employee.pop('password'))


