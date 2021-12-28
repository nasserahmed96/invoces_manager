# This Python file uses the following encoding: utf-8
import bcrypt
from PyQt5.QtSql import QSqlQuery
from Logger import Logger
from DatabaseManager import DatabaseManager


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

    def set_password(self, id, password, username):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw((username+password).encode(), salt)
        query = QSqlQuery()
        query.prepare("INSERT INTO employees(user_id, password) VALUES (:user_id, :password)")
        query.bindValue(":user_id", id)
        query.bindValue(":password", hashed.decode())
        query.exec_()
        self.logger.debug(query.lastError())



