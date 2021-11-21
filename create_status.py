import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from python_forms.createNameDescObject_GUI import Ui_createNameDescObj


class CreateStatus(QMainWindow):
    def __init__(self):
        super(CreateStatus, self).__init__()
        self.ui = Ui_createNameDescObj()
        self.ui.setupUi(self)
        self.initializeUI()
        self.intialize_db()

    def intialize_db(self):
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName("clear_vision.db")
        if not database.open():
            print("Unable to open database")
            sys.exit(1)

    def initializeUI(self):
        self.setWindowTitle("Create new job title")
        self.ui.save_btn.clicked.connect(self.save)

    def save(self):
        self.query = QSqlQuery()
        self.query.prepare("""INSERT INTO status(name, description) VALUES (?, ?)""")
        self.query.addBindValue(self.ui.nameLineEdit.text())
        self.query.addBindValue(self.ui.descriptionLineEdit.text())
        self.query.exec_()
        errors = self.query.lastError().text()
        if errors:
            print("Errors: ", errors)
        else:
            print("Saved")
            QMessageBox.information(self, "Object status", "Status created successfully")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateStatus()
    window.show()
    sys.exit(app.exec_())


