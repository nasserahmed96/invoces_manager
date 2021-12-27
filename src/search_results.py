from PyQt5.QtWidgets import QWidget
from python_forms.searchResults_GUI import Ui_search_results


class SearchResults(QWidget):
    def __init__(self):
        super(SearchResults, self).__init__()
        self.ui = Ui_search_results()
        self.ui.setupUi(self)
