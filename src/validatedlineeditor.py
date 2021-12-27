
from PyQt5.QtWidgets import QLineEdit
from helpers import show_validation_error, get_global_widget_position
from PyQt5.QtWidgets import QToolTip


class ValidatedLineEditor(QLineEdit):
    def __init__(self, parent):
        super().__init__(parent=parent)

    def focusInEvent(self, event):
        super(ValidatedLineEditor, self).focusInEvent(event)
        self.setStyleSheet("")
        error_tool_tip = QToolTip
        error_tool_tip.showText(get_global_widget_position(self), 'In widget', self, self.rect(), 3000)

    def focusOutEvent(self, event):
        if self.validator():
            state = self.validator().validate(self.text(), 0)
            if state[0] == self.validator().Acceptable:
                pass
                #self.setStyleSheet("")
            else:
                print('Widget type: ', type(self))
                style_sheet = f"{type(self).__name__} {{border: 2px solid red}}QToolTip {{border: 2px solid red;color:black}}"
                self.setStyleSheet(style_sheet)
                error_msg =f'Validation error incorrect {self.placeholderText()}'
                error_tool_tip = QToolTip
                error_tool_tip.showText(get_global_widget_position(self), error_msg, self, self.rect(), 3000)
                print('Widget placeholder: ', self.placeholderText())
        super(ValidatedLineEditor, self).focusOutEvent(event)





    def get_validation_confirm(self):
        return self.validation_confirmed if self.validation_confirmed else False
