# This Python file uses the following encoding: utf-8
import bcrypt
from PyQt5.QtSql import QSqlQuery
from src.Logger import Logger
from src.DatabaseManager import DatabaseManager


class Authentication:
    def __init__(self):
        self.database = DatabaseManager()
        self.logger = Logger()

    def authenticate_user(self, username, password):
        query = QSqlQuery()
        query.prepare("SELECT username, password FROM employees WHERE username=:username")
        query.bindValue(":username", username)
        query.exec_()
        query.first()
        self.logger.debug(query.lastError())
        hash_password = query.value("password")
        if hash_password and bcrypt.checkpw((username + password).encode(), hash_password.encode()):
            return True
        return False

    def hash_password(self, password, username):
        return bcrypt.hashpw((username+password).encode(), bcrypt.gensalt()).decode()

