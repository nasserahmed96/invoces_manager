import sys
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from python_forms.createNameDescObject_GUI import Ui_createNameDescObj


class CreateObjNameDesc(QMainWindow):
    def __init__(self, table_name, window_title):
        super(CreateObjNameDesc, self).__init__()
        self.ui = Ui_createNameDescObj()
        self.ui.setupUi(self)
        self.table_name = table_name
        self.window_title = window_title
        self.initializeUI()
        self.intialize_db()


    def intialize_db(self):
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName("clear_vision.db")
        if not database.open():
            print("Unable to open database")
            sys.exit(1)

    def initializeUI(self):
        self.setWindowTitle(f"Create new {self.window_title}")
        self.ui.save_btn.clicked.connect(self.save)

    def save(self):
        self.query = QSqlQuery()
        self.query.prepare(f"""INSERT INTO {self.table_name}(name, description) VALUES (?, ?)""")
        self.query.addBindValue(self.ui.nameLineEdit.text())
        self.query.addBindValue(self.ui.descriptionLineEdit.text())
        self.query.exec_()
        errors = self.query.lastError().text()
        if errors:
            print("Errors: ", errors)
        else:
            print("Saved")
            QMessageBox.information(self, "Object status", "Status created successfully")



