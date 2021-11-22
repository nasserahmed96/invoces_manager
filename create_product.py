import sys
from PyQt5.QtWidgets import (QApplication, QMessageBox, QMainWindow)
from CreateForm import CreateForm
from python_forms.createProduct_GUI import Ui_createProductWindow
from helpers import get_table_data


class CreateProduct(CreateForm):
    """
    To do
    If there is any other forms, please generalize this and put it in MainForm
    """
    def __init__(self):
        super(CreateProduct, self).__init__('products')
        self.ui = Ui_createProductWindow()
        self.ui.setupUi(self)
        self.initialize_db()
        self.initializeUI()
        self.show()

    def fill_combo_boxes(self):
        """
        Fill the combo box from get_table_data items which returns a dictionary
        that its keys act like text for combo box
        """
        self.categories = get_table_data("categories")
        self.brands = get_table_data("brands")
        self.ui.categoryComboBox.addItems(self.categories.keys())
        self.ui.brandComboBox.addItems(self.brands)


    def initializeUI(self):
        self.mandatory_widgets = [self.ui.nameLineEdit, self.ui.descriptionLineEdit, self.ui.barcodeLineEdit]
        self.fill_combo_boxes()
        self.ui.categoryComboBox.setCurrentIndex(1)
        self.ui.brandComboBox.setCurrentIndex(1)
        self.initialize_validators()
        self.assign_validators()
        self.connect_signals_slots()

    def assign_validators(self):
        """
        Assign validators for each widget
        :return:
        """
        self.ui.nameLineEdit.setValidator(self.arabic_text_validator)
        self.ui.descriptionLineEdit.setValidator(self.arabic_text_validator)
        self.ui.barcodeLineEdit.setValidator(self.text_validator)

    def connect_signals_slots(self):
        cols_values = {"name": self.ui.nameLineEdit.text(),
                       "description": self.ui.descriptionLineEdit.text(),
                       "barcode": self.ui.barcodeLineEdit.text(),
                       "price": self.ui.priceDoubleSpinBox.text(),
                       "quantity": self.ui.quantitySpinBox.text(),
                       "notes": self.ui.notesLineEdit.text(),
                       "category": self.categories[self.ui.categoryComboBox.currentText()],
                       "brand": self.brands[self.ui.brandComboBox.currentText()]}

        self.ui.save_btn.clicked.connect(lambda: self.save(cols_values))


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                           "Are you sure you want to exit the program?", QMessageBox.Yes, QMessageBox.No)

        event.accept() if reply == QMessageBox.Yes else event.ignore()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateProduct()
    sys.exit(app.exec_())
