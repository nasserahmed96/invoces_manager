from src.Logger import Logger
from PyQt5.QtSql import QSqlDatabase
import config


class DatabaseManager(object):
    class __DatabaseManager:
        def __init__(self):
            self.val = None
            self.DATABASE_FILENAME = f'{config.PROJECT_ROOT_PATH}/Assets/Database/{config.PROJECT_NAME}.db'
            self.logger = Logger()
            self.connectToDatabase()

        def __str__(self):
            return "{0!r} {1}".format(self, self.val)

        def connectToDatabase(self):
            database = QSqlDatabase.addDatabase("QSQLITE")
            self.val = database
            if not database.isValid():
                    self.logger.error("Can not add database")
            database.setDatabaseName(self.DATABASE_FILENAME)
            if not database.open():
                self.logger.error("Can not open database with file name: " + self.DATABASE_FILENAME)
                return
            self.logger.debug("Database opened")
    instance = None

    def __new__(cls):
        if not DatabaseManager.instance:
            DatabaseManager.instance = DatabaseManager.__DatabaseManager()
        return DatabaseManager.instance

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def __setattr(self, item):
        return setattr(self.instance, item)



