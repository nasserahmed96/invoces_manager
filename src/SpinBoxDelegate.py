from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyledItemDelegate, QSpinBox


class SpinBoxDelegate(QStyledItemDelegate):
    def __init__(self, parent=None, maximum_value=999999, minimum_value=0):
        super(SpinBoxDelegate, self).__init__(parent)
        self.maximum_value = maximum_value
        self.minimum_value = minimum_value

    def createEditor(self, parent, option, index):
        editor = QSpinBox(parent)
        editor.setFrame(False)
        editor.setMinimum(self.minimum_value)
        editor.setMaximum(self.maximum_value)
        return editor

    def setEditorData(self, editor, index):
        value = index.model().data(index, Qt.EditRole)
        editor.setValue(float(value))

    def setModelData(self, editor, model, index):
        editor.interpretText()
        value = editor.value()
        model.setData(index, value, Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        print('Spingbox delegate')
        editor.setGeometry(option.rect)