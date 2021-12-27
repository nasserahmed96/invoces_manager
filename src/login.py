import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QSplashScreen
from PyQt5.QtGui import QPixmap
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

from initialize_db import DatabaseConnection
from python_forms.login_GUI import Ui_login_form
from main_window import AppMainWindow
from helpers import decrypt_text, encrypt_text


class Login(QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_login_form()
        self.ui.setupUi(self)
        database = DatabaseConnection()
        self.initializeUI()

    def initializeUI(self):
        self.ui.login_btn.clicked.connect(self.login)

    def login(self):
        """
        :return:
        """
        user = {"username": "nasser", "password": encrypt_text("secret")}
        username = self.ui.usernameLineEdit.text()
        if username == user["username"] and self.ui.passwordLineEdit.text() == decrypt_text(user["password"]):
            self.main_window = AppMainWindow()
            self.main_window.show()
            self.close()
        else:
            QMessageBox.information(self, "Login status", "Login failed, please check username and the password",
                                    QMessageBox.Ok, QMessageBox.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash = QSplashScreen(QPixmap('images/clear_vision_logo.jpg'))
    splash.show()
    app.processEvents()
    window = Login()
    splash.finish(window)
    window.show()
    sys.exit(app.exec_())