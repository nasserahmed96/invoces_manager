from PyQt5.QtWidgets import QLineEdit


class ValidatedLineEditor(QLineEdit):

    def keyPressEvent(self, e):
        state = self.validator().validate(e.text(), 0)
        keyboard_actions = ('\x08', '\r', '\x01', '\x03', '\x18', '\x16', '\x19', '\x15')
        if state[0] == self.validator().Acceptable or state[1] in keyboard_actions:
            super().keyPressEvent(e)

    def get_validation_confirm(self):
        return self.validation_confirmed if self.validation_confirmed else False
