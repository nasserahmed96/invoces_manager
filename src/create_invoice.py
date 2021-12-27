import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from python_forms.createInvoice_GUI import Ui_create_invoice_window
from search_results import SearchResults
from helpers import open_window


class createInvoice(QMainWindow):
    def __init__(self):
        super(createInvoice, self).__init__()
        self.ui = Ui_create_invoice_window()
        self.ui.setupUi(self)
        self.initializeUI()

    def initializeUI(self):
        self.ui.search_btn.clicked.connect(lambda: open_window(self, SearchResults))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = createInvoice()
    window.show()
    sys.exit(app.exec_())