# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/createCustomer_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_createCustomerWindow(object):
    def setupUi(self, createCustomerWindow):
        createCustomerWindow.setObjectName("createCustomerWindow")
        createCustomerWindow.resize(1049, 827)
        self.centralwidget = QtWidgets.QWidget(createCustomerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Labels_Layout = QtWidgets.QVBoxLayout()
        self.Labels_Layout.setSpacing(35)
        self.Labels_Layout.setObjectName("Labels_Layout")
        self.firstNameLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstNameLabel.sizePolicy().hasHeightForWidth())
        self.firstNameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.firstNameLabel.setFont(font)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.Labels_Layout.addWidget(self.firstNameLabel)
        self.middleNameLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middleNameLabel.sizePolicy().hasHeightForWidth())
        self.middleNameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.middleNameLabel.setFont(font)
        self.middleNameLabel.setObjectName("middleNameLabel")
        self.Labels_Layout.addWidget(self.middleNameLabel)
        self.lastNameLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastNameLabel.sizePolicy().hasHeightForWidth())
        self.lastNameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lastNameLabel.setFont(font)
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.Labels_Layout.addWidget(self.lastNameLabel)
        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emailLabel.sizePolicy().hasHeightForWidth())
        self.emailLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName("emailLabel")
        self.Labels_Layout.addWidget(self.emailLabel)
        self.addressLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addressLabel.sizePolicy().hasHeightForWidth())
        self.addressLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.addressLabel.setFont(font)
        self.addressLabel.setObjectName("addressLabel")
        self.Labels_Layout.addWidget(self.addressLabel)
        self.phoneNumberLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phoneNumberLabel.sizePolicy().hasHeightForWidth())
        self.phoneNumberLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.phoneNumberLabel.setFont(font)
        self.phoneNumberLabel.setObjectName("phoneNumberLabel")
        self.Labels_Layout.addWidget(self.phoneNumberLabel)
        self.genderLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.genderLabel.sizePolicy().hasHeightForWidth())
        self.genderLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.genderLabel.setFont(font)
        self.genderLabel.setObjectName("genderLabel")
        self.Labels_Layout.addWidget(self.genderLabel)
        self.horizontalLayout.addLayout(self.Labels_Layout)
        self.LineEdits_Layout = QtWidgets.QVBoxLayout()
        self.LineEdits_Layout.setSpacing(35)
        self.LineEdits_Layout.setObjectName("LineEdits_Layout")
        self.firstNameLineEdit = ValidatedLineEditor(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstNameLineEdit.sizePolicy().hasHeightForWidth())
        self.firstNameLineEdit.setSizePolicy(sizePolicy)
        self.firstNameLineEdit.setObjectName("firstNameLineEdit")
        self.LineEdits_Layout.addWidget(self.firstNameLineEdit)
        self.middleNameLineEdit = ValidatedLineEditor(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middleNameLineEdit.sizePolicy().hasHeightForWidth())
        self.middleNameLineEdit.setSizePolicy(sizePolicy)
        self.middleNameLineEdit.setObjectName("middleNameLineEdit")
        self.LineEdits_Layout.addWidget(self.middleNameLineEdit)
        self.lastNameLineEdit = ValidatedLineEditor(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastNameLineEdit.sizePolicy().hasHeightForWidth())
        self.lastNameLineEdit.setSizePolicy(sizePolicy)
        self.lastNameLineEdit.setObjectName("lastNameLineEdit")
        self.LineEdits_Layout.addWidget(self.lastNameLineEdit)
        self.emailLineEdit = ValidatedLineEditor(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emailLineEdit.sizePolicy().hasHeightForWidth())
        self.emailLineEdit.setSizePolicy(sizePolicy)
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.LineEdits_Layout.addWidget(self.emailLineEdit)
        self.addressLineEdit = ValidatedLineEditor(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addressLineEdit.sizePolicy().hasHeightForWidth())
        self.addressLineEdit.setSizePolicy(sizePolicy)
        self.addressLineEdit.setObjectName("addressLineEdit")
        self.LineEdits_Layout.addWidget(self.addressLineEdit)
        self.phoneNumberLineEdit = ValidatedLineEditor(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phoneNumberLineEdit.sizePolicy().hasHeightForWidth())
        self.phoneNumberLineEdit.setSizePolicy(sizePolicy)
        self.phoneNumberLineEdit.setObjectName("phoneNumberLineEdit")
        self.LineEdits_Layout.addWidget(self.phoneNumberLineEdit)
        self.genderComboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.genderComboBox.sizePolicy().hasHeightForWidth())
        self.genderComboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.genderComboBox.setFont(font)
        self.genderComboBox.setObjectName("genderComboBox")
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.LineEdits_Layout.addWidget(self.genderComboBox)
        self.horizontalLayout.addLayout(self.LineEdits_Layout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.save_btn.setFont(font)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_2.addWidget(self.save_btn)
        spacerItem = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_btn.sizePolicy().hasHeightForWidth())
        self.clear_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.clear_btn.setFont(font)
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout_2.addWidget(self.clear_btn)
        spacerItem1 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_btn.sizePolicy().hasHeightForWidth())
        self.cancel_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setAutoFillBackground(False)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_2.addWidget(self.cancel_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        createCustomerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(createCustomerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1049, 20))
        self.menubar.setObjectName("menubar")
        createCustomerWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(createCustomerWindow)
        self.statusbar.setObjectName("statusbar")
        createCustomerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(createCustomerWindow)
        self.clear_btn.clicked.connect(self.firstNameLineEdit.clear)
        self.clear_btn.clicked.connect(self.middleNameLineEdit.clear)
        self.clear_btn.clicked.connect(self.lastNameLineEdit.clear)
        self.clear_btn.clicked.connect(self.lastNameLineEdit.clear)
        self.clear_btn.clicked.connect(self.emailLineEdit.clear)
        self.clear_btn.clicked.connect(self.addressLineEdit.clear)
        self.clear_btn.clicked.connect(self.phoneNumberLineEdit.clear)
        self.cancel_btn.clicked.connect(createCustomerWindow.close)
        QtCore.QMetaObject.connectSlotsByName(createCustomerWindow)

    def retranslateUi(self, createCustomerWindow):
        _translate = QtCore.QCoreApplication.translate
        createCustomerWindow.setWindowTitle(_translate("createCustomerWindow", "Create customer"))
        self.firstNameLabel.setText(_translate("createCustomerWindow", "First name"))
        self.middleNameLabel.setText(_translate("createCustomerWindow", "Middle name"))
        self.lastNameLabel.setText(_translate("createCustomerWindow", "Last name"))
        self.emailLabel.setText(_translate("createCustomerWindow", "Email"))
        self.addressLabel.setText(_translate("createCustomerWindow", "Address"))
        self.phoneNumberLabel.setText(_translate("createCustomerWindow", "Phone number"))
        self.genderLabel.setText(_translate("createCustomerWindow", "Gender"))
        self.firstNameLineEdit.setPlaceholderText(_translate("createCustomerWindow", "First name"))
        self.middleNameLineEdit.setPlaceholderText(_translate("createCustomerWindow", "Middle name"))
        self.lastNameLineEdit.setPlaceholderText(_translate("createCustomerWindow", "Last name"))
        self.emailLineEdit.setPlaceholderText(_translate("createCustomerWindow", "Email"))
        self.addressLineEdit.setPlaceholderText(_translate("createCustomerWindow", "Address"))
        self.phoneNumberLineEdit.setPlaceholderText(_translate("createCustomerWindow", "Phone number"))
        self.genderComboBox.setItemText(0, _translate("createCustomerWindow", "Male"))
        self.genderComboBox.setItemText(1, _translate("createCustomerWindow", "Female"))
        self.save_btn.setText(_translate("createCustomerWindow", "Save"))
        self.clear_btn.setText(_translate("createCustomerWindow", "Clear"))
        self.cancel_btn.setText(_translate("createCustomerWindow", "Cancel"))
from src.validatedlineeditor import ValidatedLineEditor