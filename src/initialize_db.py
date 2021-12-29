import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery


class DatabaseConnection(object):
    def __init__(self):
        self.initialize_db()

    def initialize_db(self):
        print("Database")
        self.database = QSqlDatabase.addDatabase("QSQLITE", "Base")
        self.database.setDatabaseName("")
        if not self.database:
            print("Unable to open database")
            sys.exit(1)
        return self.database