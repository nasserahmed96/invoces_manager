import json
from collections import OrderedDict
from cryptography.fernet import Fernet
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtCore import Qt

def get_key():
    with open(".env.json") as env_file:
        key = json.load(env_file)["key"]
        return key


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


def open_window(self, window):
    self.window = window()
    self.window.show()


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