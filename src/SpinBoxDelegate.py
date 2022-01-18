from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyledItemDelegate, QSpinBox


class SpinBoxDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super(SpinBoxDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        print('Spinbox delegate')
        editor = QSpinBox(parent)
        editor.setFrame(False)
        editor.setMinimum(0)
        editor.setMaximum(99999)
        return editor

    def setEditorData(self, editor, index):
        value = index.model().data(index, Qt.EditRole)
        editor.setValue(int(float(value)))

    def setModelData(self, editor, model, index):
        editor.interpretText()
        value = editor.value()
        model.setData(index, value, Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        print('Spingbox delegate')
        editor.setGeometry(option.rect)