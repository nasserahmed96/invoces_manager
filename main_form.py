"""
A base class that inherits QMainWindow, is is used in each form through the system
"""

import re
from PyQt5.QtWidgets import (QMainWindow, QWidget)


class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.validation_widgets = []
        self.validation_error = False

    def clear_validation_errors(self):
        """
        Clear all validation colors and tool tips that appeared, mainly it clears the password fields, but if widgets
        are provided it clears it too.
        :return:
        """
        for widget in self.validation_widgets:
            widget["widget"].setStyleSheet("")

    def append_validation_widget(self, widgets: list, widget: QWidget, regex: str):
        """
        Append the widget I want to validate, along side with required regex
        :param widgets:
        :param widget:
        :param regex:
        :return: It doesn't return any thing, it just fills the widgets list
        """
        widget_dict = dict()
        widget_dict["widget"] = widget
        widget_dict["regex"] = regex
        print("Widget: ", widget_dict)
        widgets.append(widget_dict)

    def validate_form(self, widgets: list):
        try:
            """
            Validate with widgets in widgets list
            :param widgets: A list of dictionaries
            :return: If an error detected, it sets the validation_error flag to True, the user should check for this flag
            after calling the function
            """
            regex = dict()
            error_widgets = []
            regex["text"] = re.compile("^[a-zA-Z\u0621-\u064A\u0660-\u0669\s\,\:\;0-9]+$")
            regex["name"] = re.compile("^[a-zA-Z\u0621-\u064A]+[a-zA-Z\u0621-\u064A]$")
            regex["phone_number"] = re.compile("^(\+[0-9]{1,3}){0,1}[0-9]{1,13}")
            regex["email"] = re.compile("[a-zA-Z\.1-9\-\\\/\_]*@[A-Za-z]+(\.[a-zA-Z]+)*[a-zA-Z]$")
            for widget in widgets:
                if not regex[widget["regex"]].match(widget["widget"].text()):
                    widget["error"] = "Not a valid: " + widget["widget"].placeholderText()
                    widget["widget"].setStyleSheet("""background-color: red;""")
                    error_widgets.append(widget)
                else:
                    widget["widget"].setStyleSheet("")
            return error_widgets
        except KeyError as e:
            print("Unsupported regex: ", e)


