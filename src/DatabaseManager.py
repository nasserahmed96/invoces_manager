from src.Logger import Logger
from PyQt5.QtSql import QSqlDatabase
import config


class DatabaseManager(object):
    class __DatabaseManager:
        def __init__(self, is_testing):
            self.val = None
            self.DATABASE_FILENAME = f'{config.PROJECT_ROOT_PATH}/Assets/Database/{config.PROJECT_NAME}.db'
            self.TESTING_DATABASE_FILENAME = f'{config.PROJECT_ROOT_PATH}/Assets/Database/{config.PROJECT_NAME}_Testing.db'
            self.is_testing = is_testing
            self.current_database = self.DATABASE_FILENAME if not self.is_testing else self.TESTING_DATABASE_FILENAME
            self.logger = Logger()
            self.connectToDatabase()

        def __str__(self):
            return "{0!r} {1}".format(self, self.val)

        def connectToDatabase(self):
            database = QSqlDatabase.addDatabase("QSQLITE")
            self.val = database
            if not database.isValid():
                    self.logger.error("Can not add database")
            database.setDatabaseName(self.current_database)
            if not database.open():
                self.logger.error("Can not open database with file name: " + self.self.current_database)
                return
            self.logger.debug("Database opened")
    instance = None

    def __new__(cls, is_testing=False):
        if not DatabaseManager.instance:
            DatabaseManager.instance = DatabaseManager.__DatabaseManager(is_testing=is_testing)
        return DatabaseManager.instance

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def __setattr(self, item):
        return setattr(self.instance, item)



