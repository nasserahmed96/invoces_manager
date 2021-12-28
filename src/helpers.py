import json
from collections import OrderedDict
from cryptography.fernet import Fernet
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QToolTip


def get_style_sheets():
    style_sheets = dict()
    style_sheets['validated_line_edit_validation_error'] = """ValidatedLineEditor{
    border: 2px solid red
    }
    ToolTip{
    font-color: black;
    border-width: 2px;
    border-style: solid;
    border-color: red
    }
        """
    style_sheets['tool_tip_validation_error'] = """
    font-color: black;
    border-width: 2px;
    border-style: solid;
    border-color: red"""
    return style_sheets


def encrypt_text(text:str):
    """
    Encrypt text with Fernet with the saved key in .env and return an encrypted version of it
    :param text:
    :return: An ecrypted version of text
    """
    fernet = Fernet(get_key())
    text = fernet.encrypt(text.encode())
    return text.decode()


def decrypt_text(text:str):
    """
    Decrypt text with Fernet with the saved key in .env and return the real value
    :param text:
    :return: The real version of text
    """
    fernet = Fernet(get_key())
    text = fernet.decrypt(text.encode())
    return text.decode()

def get_key():
    with open(".env.json") as env_file:
        key = json.load(env_file)["key"]
        return key


def open_window(**args):
    parent_window = args.pop('parent_window')
    window = args.pop('window')
    parent_window.window = window(**args)
    parent_window.window.show()


def get_table_data(table_name:str):
    """
    Get data from table:table_name in database and return a dictionary contains the data from the database,
    the dictionary keys will act as the text for the chosen combo boc
    :param table_name: the table we wish to get the from
    :return: A dictionary containing the data we want
    """
    #Get the data from the database
    query = QSqlQuery()
    query.exec_("""SELECT id, name FROM {}""".format(table_name))
    data = OrderedDict()
    while(query.next()):
        data[str(query.value(1))] = str(query.value(0))
    return data


def initialize_combo_box(combo_box, items, default_value):
    combo_box.addItems(items)
    set_combo_box_default(combo_box, default_value)


def set_combo_box_default(combo_box, default):
    if combo_box.findText(default, Qt.MatchFixedString) < 0:
        combo_box.addItem('All')
    combo_box.setCurrentText('All')


def get_global_widget_position(widget):
        return widget.mapToGlobal(widget.rect().bottomLeft())


def show_validation_error(widget, error_msg=None):
    print('Widget type: ', type(widget))
    style_sheet = f"{type(widget).__name__} {{border: 2px solid red}}QToolTip {{border: 2px solid red;color:black}}"
    widget.setStyleSheet(style_sheet)
    error_msg = error_msg if error_msg else f'Validation error incorrect {widget.placeholderText()}'
    error_tool_tip = QToolTip
    error_tool_tip.showText(get_global_widget_position(widget), error_msg, widget, widget.rect(), 3000)
    print('Widget placeholder: ', widget.placeholderText())