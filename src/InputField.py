from PyQt5.QtWidgets import QWidget
from python_forms.input_field import Ui_input_field


class InputField(QWidget):
    def __init__(self, parent=None):
        super(InputField, self).__init__(parent)
        self.ui = Ui_input_field()
        self.ui.setupUi(self)
        self.connect_signals_slots()

    def connect_signals_slots(self):
        self.ui.input_line_edit
