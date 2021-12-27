import sys
from PyQt5.QtWidgets import QApplication

from create_objec_name_desc import CreateObjNameDesc


class CreateStatus(CreateObjNameDesc):
    def __init__(self):
        super().__init__(table_name='status', window_title='status')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateStatus()
    window.show()
    sys.exit(app.exec_())


