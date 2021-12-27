from PyQt5.QtSql import QSqlQuery
from src.DatabaseManager import DatabaseManager
from src.Logger import Logger


class DataAccessObject(object):
    def __init__(self, table_name):
        self.data_base = DatabaseManager()
        self.table_name = table_name
        self.logger = Logger()

    def debug_query(self, query:QSqlQuery):
        self.logger.debug("Query errors: " + query.lastError().text())
        return True if not query.lastError().text() else False

    def build_insert_query(self, cols):
        cols_values = "VALUES ("
        cols_names = ""
        query = f"INSERT INTO {self.table_name}("
        for col_name in cols:
            cols_names += col_name + ","
            cols_values += f":{col_name},"
        query += f"{cols_names[:-1]}) {cols_values[:-1]})"
        return query

    def bind_values(self, query, values):
        [query.bindValue(f':{value}', values[value]) for value in values.keys()]

    def insert(self, values):
        query_str = self.build_insert_query(values.keys())
        return self.execute_edit_query(query_str=query_str, place_holders=values)

    def build_conditions(self, conditions):
        """
        This function builds conditions for the SELECT query, based on whether the required widget has something in it
        or not
        :return:
        """
        return ' WHERE ' + ' AND '.join([self.get_condition_string(condition) for condition in conditions]) if any(
            conditions) else ""

    def get_condition_string(self, condition):
        """
        Get a condition string out of a condition object
        :param condition: A condition object contains the required parameters for the condition
        :return: A condition string to be used in SQL query
        """
        return f"{condition['column']} {condition['operator']} :{condition['column']} {condition['options']}"

    def select(self, columns=None, values=None, conditions=None):
        query_str = f"""SELECT {" ".join(columns) if columns else '*'} FROM {self.table_name} {self.build_conditions(conditions) if conditions else ''}"""
        return self.execute_select_query(query_str, values)

    def execute_select_query(self, query_str, values=None):
        query = self.execute_query(query_str, place_holders=values)
        return query if self.debug_query(query) else None

    def execute_edit_query(self, query_str, place_holders=None):
        query = self.execute_query(query_str, place_holders=place_holders)
        return self.debug_query(query)

    def execute_query(self, query_str, place_holders):
        query = QSqlQuery()
        print('Query string: ', query_str)
        query.prepare(query_str)
        if place_holders:
            self.bind_values(query, place_holders)
        query.exec_()
        return query

