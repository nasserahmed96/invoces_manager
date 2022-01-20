from decimal import Decimal
import pandas as pd
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex, QVariant
from PyQt5.QtWidgets import QCompleter
from src.DataAccessObjects.EmployeeDao import EmployeeDao


class EmployeesSharesTableModel(QAbstractTableModel):
    def __init__(self):
        super(EmployeesSharesTableModel, self).__init__()
        self.employees_dao = EmployeeDao()
        self.columns = ['Id', 'Username', 'Percentage', 'Value']
        self.columns_dict = {self.columns[i]: i for i in range(len(self.columns))}
        self.employees_shares_dataframe = pd.DataFrame({column_name: [] for column_name in self.columns})
        self.employees_shares_dataframe = self.employees_shares_dataframe.set_index('Id')

    def rowCount(self, parent=QModelIndex()):
        return self.employees_shares_dataframe.shape[0]

    def columnCount(self, parent=QModelIndex()):
        return len(self.columns)

    def headerData(self, section, orientation=Qt.Horizontal, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.columns[section]

    def data(self, index=QModelIndex(), role=Qt.DisplayRole):
        if index.isValid() and (role == Qt.DisplayRole or role == Qt.EditRole):
            return str(self.get_employees_shares().iat[index.row(), index.column()-1]) if not index.column() == self.get_column_index('Id') else str(self.get_employees_shares().index[index.row()])
        return QVariant()

    def setData(self, index, value, role=Qt.EditRole):
        """
        As we only interested in changing the percentage value, so we will set the column to be Percentage,
        if we want to generalize it we will have to get the column name by index.column()
        :param index:
        :param value:
        :param role:
        :return:
        """
        if index.isValid() and role == Qt.EditRole:
            difference = value - self.get_employees_shares().loc[self.employees_shares_dataframe.index[index.row()], 'Percentage']
            if self.check_for_total_percentage(difference):
                self.employees_shares_dataframe.loc[self.employees_shares_dataframe.index[index.row()], 'Percentage'] = value
                self.refresh_shares_values()
                self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        if index.column() == self.get_column_index('Percentage'):
            return Qt.ItemIsEditable | Qt.ItemIsEnabled
        return QAbstractTableModel.flags(self, index) | Qt.ItemIsEnabled

    def check_for_total_percentage(self, provided_percentage):
        """
        Check if the provided percentage by the user alongside the current total(Sum of percentage column) doesn't exceed
        100
        :return: True if the total percentage <= 100 False instead
        """
        return True if self.get_employees_shares()['Percentage'].astype('int').sum() + provided_percentage <= 100 else False

    def get_column_index(self, column_name):
        return self.columns_dict[column_name]

    def append_employee_share(self, employee_share):
        if self.check_for_total_percentage(employee_share['Percentage']):
            new_row = self.employees_shares_dataframe.shape[0]
            self.beginInsertRows(QModelIndex(), new_row, new_row)
            temp_dataframe = pd.DataFrame([employee_share,])
            temp_dataframe = temp_dataframe.set_index('Id')
            self.employees_shares_dataframe = self.employees_shares_dataframe.append(temp_dataframe, verify_integrity=True)
            self.refresh_shares_values()
            self.dataChanged.emit(QModelIndex(), QModelIndex())
            self.endInsertRows()

    def refresh_shares_values(self):
        self.calculate_percentage_values(Decimal(self.employees_shares_dataframe['Value'].sum()).quantize(Decimal('.00')))

    def get_employees_shares(self):
        return self.employees_shares_dataframe

    def get_employees_data(self):
        """
        Get employees required data(employee_id, username)
        :return: A dictionary with username as Key and employee_id as value, to be used in shares TableView(or any other
        view that requires employee ID and username
        """
        employees_usernames = dict()
        employees_result = self.employees_dao.select(['id', 'username'])
        while employees_result.next():
            employees_usernames[employees_result.value('username')] = employees_result.value('id')
        return employees_usernames

    def calculate_percentage_values(self, new_invoice_total):
        """
        Recalculate the value corresponding to each employee share, the function needs to be optimized to not use
        apply method, and use something more efficient
        :param new_invoice_total:
        :return:
        """
        self.employees_shares_dataframe['Value'] = self.employees_shares_dataframe['Percentage'] * (float(new_invoice_total)/100)
        self.employees_shares_dataframe['Value'] = self.employees_shares_dataframe['Value'].apply(lambda x: Decimal(x).quantize(Decimal('.00')))
        self.dataChanged.emit(QModelIndex(), QModelIndex())

    def get_completer(self, col_name):
        completer = QCompleter(self.employees_dao.get_data_for_completer(col_name))
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        return completer

