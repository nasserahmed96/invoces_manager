import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QSplashScreen
from PyQt5.QtGui import QPixmap
from python_forms.login_GUI import Ui_login_form
from src.main_window import AppMainWindow
from src.Authenticate import Authentication
from src.cache import Cache
from src.DataAccessObjects.EmployeeDao import EmployeeDao


class Login(QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_login_form()
        self.ui.setupUi(self)
        self.initializeUI()
        self.authenticaion = Authentication()
        self.cache = Cache()
        self.employee_dao = EmployeeDao()

    def initializeUI(self):
        self.ui.login_btn.clicked.connect(self.login)

    def login(self):
        """
        :return:
        """
        user_id = self.authenticaion.authenticate_user(username=self.ui.usernameLineEdit.text(), password=self.ui.passwordLineEdit.text())
        if user_id:
            self.set_employee_session(user_id)
            self.main_window = AppMainWindow()
            self.main_window.show()
            self.close()
        else:
            QMessageBox.information(self, "Login status", "Login failed, please check username and the password",
                                    QMessageBox.Ok, QMessageBox.Ok)

    def set_employee_session(self, employee_id):
        self.cache.append_to_cache('employee', {'id': employee_id, 'employee_object': self.employee_dao.get_employee_by_id(employee_id)})



if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash = QSplashScreen(QPixmap(''))
    splash.show()
    app.processEvents()
    window = Login()
    splash.finish(window)
    window.show()
    sys.exit(app.exec_())