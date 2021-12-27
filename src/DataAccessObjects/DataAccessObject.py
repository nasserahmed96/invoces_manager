from PyQt5.QtSql import QSqlQuery
from src.DatabaseManager import DatabaseManager
from src.Logger import Logger


class DataAccessObject(object):
    def __init__(self, table_name):
        self.data_base = DatabaseManager()
        self.table_name = table_name
        self.logger = Logger()

    def debug_query(self, query:QSqlQuery):
        """
        This function takes QSqlQuery object and pass it to the logger class
        :param query:
        :return: True if no errors, False instead
        """
        self.logger.debug("Query errors: " + query.lastError().text())
        return True if not query.lastError().text() else False

    def build_insert_query(self, cols):
        """
        Takes a list of strings that represents the columns in the INSERT query, and place it in VALUES with
        :col_name, the substitution of the real value happens in bind_values function
        :param cols: List of strings represents the columns we want to insert
        :return: A string containing the INSERT statement without real values (only placeholders),
        placeholders are added in bind_values function
        """
        cols_values = "VALUES ("
        cols_names = ""
        query = f"INSERT INTO {self.table_name}("
        for col_name in cols:
            cols_names += col_name + ","
            cols_values += f":{col_name},"
        query += f"{cols_names[:-1]}) {cols_values[:-1]})"
        return query

    def bind_values(self, query:QSqlQuery, values:dict):
        """
        Bind the values in the values to its corresponding placeholder from the query
        :param query: QSqlQuery with placeholders
        :param values: A dictionary contains the values to placeholders in query object,
        the dictionary keys are the same as the placeholders names
        :return: None, as query is passed by reference
        """
        [query.bindValue(f':{value}', values[value]) for value in values.keys()]

    def insert(self, values:dict):
        """
        Insert the 'values', the values keys represents placeholders and column names
        :param values: Dictionary contains the columns names which act as placeholders and its values
        :return: QSqlQuery object after executing
        """
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

    def select(self, columns=None, placeholders=None, conditions=None):
        """
        Get the columns with conditions and values
        :param columns: The columns we want to retrieve from the table, if not presented use '*' instead
        :param placeholders: Values to the conditions to be retrieved
        :param conditions: Dictionary contains the required conditions on the query
        :return: QSqlQuery object after execution
        """
        query_str = f"""SELECT {" ".join(columns) if columns else '*'} FROM {self.table_name} {self.build_conditions(conditions) if conditions else ''}"""
        return self.execute_select_query(query_str, placeholders)

    def execute_select_query(self, query_str, placeholders=None):
        """
        Execute a QSqlQuery object that will fetch (Read only) data from the database
        :param query_str: The final query string with placeholders
        :param placeholders: A dictionary contains the values for the palceholders in the query string
        :return: query (with data) if it's successful None instead
        """
        query = self.execute_query(query_str, place_holders=placeholders)
        return query if self.debug_query(query) else None

    def execute_edit_query(self, query_str, place_holders=None):
        """
        Execute a QSqlQuery object that will modify (Write) data in the database
        :param query_str: The final query string with placeholders
        :param place_holders: A dictionary contains the values for the palceholders in the query string
        :return: True in case of success False instead
        """
        query = self.execute_query(query_str, place_holders=place_holders)
        return self.debug_query(query)

    def execute_query(self, query_str, place_holders):
        """
        Execute the query_str
        :param query_str: The final query string with placeholders
        :param place_holders: A dictionary contains the values for the palceholders in the query string
        :return: A QSqlQuery object after execution
        """
        query = QSqlQuery()
        query.prepare(query_str)
        if place_holders:
            self.bind_values(query, place_holders)
        query.exec_()
        return query

    def update(self, values, conditions):
        query_str = self.build_update_string(values.keys()) + self.build_conditions(conditions)
        place_holders = values
        for condition in conditions:
            place_holders[condition['column']] = values[condition['column']]
        self.execute_edit_query(query_str, place_holders)

    def build_update_string(self, columns):
        new_cols = ""
        query = f"UPDATE {self.table_name} SET "
        for col_name in columns:
            new_cols = f"{col_name}=:{col_name},"
        query += new_cols[:-1]
        return query

