# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/create_invoice_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_createInvoiceWindow(object):
    def setupUi(self, createInvoiceWindow):
        createInvoiceWindow.setObjectName("createInvoiceWindow")
        createInvoiceWindow.resize(1174, 889)
        self.centralwidget = QtWidgets.QWidget(createInvoiceWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.invoice_basic_information_frame = QtWidgets.QFrame(self.centralwidget)
        self.invoice_basic_information_frame.setMinimumSize(QtCore.QSize(0, 169))
        self.invoice_basic_information_frame.setMaximumSize(QtCore.QSize(16777215, 169))
        self.invoice_basic_information_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.invoice_basic_information_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.invoice_basic_information_frame.setObjectName("invoice_basic_information_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.invoice_basic_information_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.employee_username_label = QtWidgets.QLabel(self.invoice_basic_information_frame)
        self.employee_username_label.setMinimumSize(QtCore.QSize(120, 25))
        self.employee_username_label.setMaximumSize(QtCore.QSize(70, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.employee_username_label.setFont(font)
        self.employee_username_label.setObjectName("employee_username_label")
        self.horizontalLayout_2.addWidget(self.employee_username_label)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.employee_percentage_label = QtWidgets.QLabel(self.invoice_basic_information_frame)
        self.employee_percentage_label.setMinimumSize(QtCore.QSize(130, 25))
        self.employee_percentage_label.setMaximumSize(QtCore.QSize(130, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.employee_percentage_label.setFont(font)
        self.employee_percentage_label.setObjectName("employee_percentage_label")
        self.horizontalLayout_2.addWidget(self.employee_percentage_label)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.employees_usernames_cb = QtWidgets.QComboBox(self.invoice_basic_information_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.employees_usernames_cb.sizePolicy().hasHeightForWidth())
        self.employees_usernames_cb.setSizePolicy(sizePolicy)
        self.employees_usernames_cb.setMinimumSize(QtCore.QSize(150, 30))
        self.employees_usernames_cb.setMaximumSize(QtCore.QSize(200, 30))
        self.employees_usernames_cb.setObjectName("employees_usernames_cb")
        self.horizontalLayout_13.addWidget(self.employees_usernames_cb)
        self.employee_shares_sb = QtWidgets.QDoubleSpinBox(self.invoice_basic_information_frame)
        self.employee_shares_sb.setMinimumSize(QtCore.QSize(0, 30))
        self.employee_shares_sb.setMaximumSize(QtCore.QSize(95, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.employee_shares_sb.setFont(font)
        self.employee_shares_sb.setObjectName("employee_shares_sb")
        self.horizontalLayout_13.addWidget(self.employee_shares_sb)
        self.add_employee_btn = QtWidgets.QPushButton(self.invoice_basic_information_frame)
        self.add_employee_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.add_employee_btn.setMaximumSize(QtCore.QSize(110, 30))
        self.add_employee_btn.setObjectName("add_employee_btn")
        self.horizontalLayout_13.addWidget(self.add_employee_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.client_name_label = QtWidgets.QLabel(self.invoice_basic_information_frame)
        self.client_name_label.setMinimumSize(QtCore.QSize(190, 25))
        self.client_name_label.setMaximumSize(QtCore.QSize(190, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.client_name_label.setFont(font)
        self.client_name_label.setObjectName("client_name_label")
        self.verticalLayout.addWidget(self.client_name_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clients_names_cb = QtWidgets.QComboBox(self.invoice_basic_information_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clients_names_cb.sizePolicy().hasHeightForWidth())
        self.clients_names_cb.setSizePolicy(sizePolicy)
        self.clients_names_cb.setMinimumSize(QtCore.QSize(300, 30))
        self.clients_names_cb.setMaximumSize(QtCore.QSize(295, 40))
        self.clients_names_cb.setObjectName("clients_names_cb")
        self.horizontalLayout.addWidget(self.clients_names_cb)
        self.add_client_btn = QtWidgets.QPushButton(self.invoice_basic_information_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_client_btn.sizePolicy().hasHeightForWidth())
        self.add_client_btn.setSizePolicy(sizePolicy)
        self.add_client_btn.setMinimumSize(QtCore.QSize(100, 30))
        self.add_client_btn.setMaximumSize(QtCore.QSize(110, 30))
        self.add_client_btn.setObjectName("add_client_btn")
        self.horizontalLayout.addWidget(self.add_client_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_14.addWidget(self.invoice_basic_information_frame)
        self.employees_shares_frame = QtWidgets.QFrame(self.centralwidget)
        self.employees_shares_frame.setMinimumSize(QtCore.QSize(0, 169))
        self.employees_shares_frame.setMaximumSize(QtCore.QSize(16777215, 169))
        self.employees_shares_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.employees_shares_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.employees_shares_frame.setObjectName("employees_shares_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.employees_shares_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.other_employees_label = QtWidgets.QLabel(self.employees_shares_frame)
        self.other_employees_label.setMinimumSize(QtCore.QSize(278, 25))
        self.other_employees_label.setMaximumSize(QtCore.QSize(278, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.other_employees_label.setFont(font)
        self.other_employees_label.setObjectName("other_employees_label")
        self.verticalLayout_3.addWidget(self.other_employees_label)
        self.employees_table_view = QtWidgets.QTableView(self.employees_shares_frame)
        self.employees_table_view.setObjectName("employees_table_view")
        self.verticalLayout_3.addWidget(self.employees_table_view)
        self.horizontalLayout_14.addWidget(self.employees_shares_frame)
        self.invoice_details_frame = QtWidgets.QFrame(self.centralwidget)
        self.invoice_details_frame.setMinimumSize(QtCore.QSize(270, 169))
        self.invoice_details_frame.setMaximumSize(QtCore.QSize(270, 169))
        self.invoice_details_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.invoice_details_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.invoice_details_frame.setObjectName("invoice_details_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.invoice_details_frame)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.invoice_date_frame = QtWidgets.QLabel(self.invoice_details_frame)
        self.invoice_date_frame.setMinimumSize(QtCore.QSize(190, 20))
        self.invoice_date_frame.setMaximumSize(QtCore.QSize(190, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.invoice_date_frame.setFont(font)
        self.invoice_date_frame.setObjectName("invoice_date_frame")
        self.verticalLayout_2.addWidget(self.invoice_date_frame)
        self.invoice_date_edit = QtWidgets.QDateEdit(self.invoice_details_frame)
        self.invoice_date_edit.setMinimumSize(QtCore.QSize(200, 30))
        self.invoice_date_edit.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.invoice_date_edit.setFont(font)
        self.invoice_date_edit.setCalendarPopup(True)
        self.invoice_date_edit.setObjectName("invoice_date_edit")
        self.verticalLayout_2.addWidget(self.invoice_date_edit)
        self.invoice_serial_number_label = QtWidgets.QLabel(self.invoice_details_frame)
        self.invoice_serial_number_label.setMinimumSize(QtCore.QSize(250, 25))
        self.invoice_serial_number_label.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.invoice_serial_number_label.setFont(font)
        self.invoice_serial_number_label.setObjectName("invoice_serial_number_label")
        self.verticalLayout_2.addWidget(self.invoice_serial_number_label)
        self.invoice_serial_number_line_edit = QtWidgets.QLineEdit(self.invoice_details_frame)
        self.invoice_serial_number_line_edit.setMinimumSize(QtCore.QSize(200, 30))
        self.invoice_serial_number_line_edit.setMaximumSize(QtCore.QSize(250, 30))
        self.invoice_serial_number_line_edit.setObjectName("invoice_serial_number_line_edit")
        self.verticalLayout_2.addWidget(self.invoice_serial_number_line_edit)
        self.horizontalLayout_14.addWidget(self.invoice_details_frame)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.search_products_label = QtWidgets.QLabel(self.centralwidget)
        self.search_products_label.setMinimumSize(QtCore.QSize(231, 25))
        self.search_products_label.setMaximumSize(QtCore.QSize(231, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.search_products_label.setFont(font)
        self.search_products_label.setObjectName("search_products_label")
        self.verticalLayout_4.addWidget(self.search_products_label)
        self.search_products_layout = QtWidgets.QHBoxLayout()
        self.search_products_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.search_products_layout.setObjectName("search_products_layout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.product_name_label = QtWidgets.QLabel(self.centralwidget)
        self.product_name_label.setMinimumSize(QtCore.QSize(100, 50))
        self.product_name_label.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setBold(True)
        self.product_name_label.setFont(font)
        self.product_name_label.setObjectName("product_name_label")
        self.horizontalLayout_3.addWidget(self.product_name_label)
        self.product_name_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.product_name_line_edit.sizePolicy().hasHeightForWidth())
        self.product_name_line_edit.setSizePolicy(sizePolicy)
        self.product_name_line_edit.setMinimumSize(QtCore.QSize(125, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.product_name_line_edit.setFont(font)
        self.product_name_line_edit.setObjectName("product_name_line_edit")
        self.horizontalLayout_3.addWidget(self.product_name_line_edit)
        self.search_products_layout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bar_code_label = QtWidgets.QLabel(self.centralwidget)
        self.bar_code_label.setMinimumSize(QtCore.QSize(60, 50))
        self.bar_code_label.setMaximumSize(QtCore.QSize(56, 50))
        font = QtGui.QFont()
        font.setBold(True)
        self.bar_code_label.setFont(font)
        self.bar_code_label.setObjectName("bar_code_label")
        self.horizontalLayout_4.addWidget(self.bar_code_label)
        self.bar_code_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bar_code_line_edit.sizePolicy().hasHeightForWidth())
        self.bar_code_line_edit.setSizePolicy(sizePolicy)
        self.bar_code_line_edit.setMinimumSize(QtCore.QSize(125, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bar_code_line_edit.setFont(font)
        self.bar_code_line_edit.setObjectName("bar_code_line_edit")
        self.horizontalLayout_4.addWidget(self.bar_code_line_edit)
        self.search_products_layout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.category_label = QtWidgets.QLabel(self.centralwidget)
        self.category_label.setMinimumSize(QtCore.QSize(120, 50))
        self.category_label.setMaximumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setBold(True)
        self.category_label.setFont(font)
        self.category_label.setObjectName("category_label")
        self.horizontalLayout_5.addWidget(self.category_label)
        self.product_category_cb = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.product_category_cb.sizePolicy().hasHeightForWidth())
        self.product_category_cb.setSizePolicy(sizePolicy)
        self.product_category_cb.setMinimumSize(QtCore.QSize(125, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.product_category_cb.setFont(font)
        self.product_category_cb.setObjectName("product_category_cb")
        self.horizontalLayout_5.addWidget(self.product_category_cb)
        self.search_products_layout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.brand_label = QtWidgets.QLabel(self.centralwidget)
        self.brand_label.setMinimumSize(QtCore.QSize(100, 50))
        self.brand_label.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setBold(True)
        self.brand_label.setFont(font)
        self.brand_label.setObjectName("brand_label")
        self.horizontalLayout_7.addWidget(self.brand_label)
        self.product_brand_cb = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.product_brand_cb.sizePolicy().hasHeightForWidth())
        self.product_brand_cb.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.product_brand_cb.setFont(font)
        self.product_brand_cb.setObjectName("product_brand_cb")
        self.horizontalLayout_7.addWidget(self.product_brand_cb)
        self.search_products_layout.addLayout(self.horizontalLayout_7)
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_btn.sizePolicy().hasHeightForWidth())
        self.search_btn.setSizePolicy(sizePolicy)
        self.search_btn.setMinimumSize(QtCore.QSize(115, 50))
        self.search_btn.setMaximumSize(QtCore.QSize(115, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.search_btn.setFont(font)
        self.search_btn.setObjectName("search_btn")
        self.search_products_layout.addWidget(self.search_btn)
        self.create_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_btn.sizePolicy().hasHeightForWidth())
        self.create_btn.setSizePolicy(sizePolicy)
        self.create_btn.setMinimumSize(QtCore.QSize(115, 50))
        self.create_btn.setMaximumSize(QtCore.QSize(115, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.create_btn.setFont(font)
        self.create_btn.setObjectName("create_btn")
        self.search_products_layout.addWidget(self.create_btn)
        self.verticalLayout_4.addLayout(self.search_products_layout)
        self.products_table_view = QtWidgets.QTableView(self.centralwidget)
        self.products_table_view.setObjectName("products_table_view")
        self.products_table_view.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_4.addWidget(self.products_table_view)
        self.products_invoice_table_view = QtWidgets.QLabel(self.centralwidget)
        self.products_invoice_table_view.setMinimumSize(QtCore.QSize(231, 25))
        self.products_invoice_table_view.setMaximumSize(QtCore.QSize(231, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.products_invoice_table_view.setFont(font)
        self.products_invoice_table_view.setObjectName("products_invoice_table_view")
        self.verticalLayout_4.addWidget(self.products_invoice_table_view)
        self.invoice_products_table_view = QtWidgets.QTableView(self.centralwidget)
        self.invoice_products_table_view.setObjectName("invoice_products_table_view")
        self.invoice_products_table_view.horizontalHeader().setCascadingSectionResizes(True)
        self.invoice_products_table_view.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_4.addWidget(self.invoice_products_table_view)
        createInvoiceWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(createInvoiceWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1174, 19))
        self.menubar.setObjectName("menubar")
        createInvoiceWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(createInvoiceWindow)
        self.statusbar.setObjectName("statusbar")
        createInvoiceWindow.setStatusBar(self.statusbar)

        self.retranslateUi(createInvoiceWindow)
        QtCore.QMetaObject.connectSlotsByName(createInvoiceWindow)

    def retranslateUi(self, createInvoiceWindow):
        _translate = QtCore.QCoreApplication.translate
        createInvoiceWindow.setWindowTitle(_translate("createInvoiceWindow", "MainWindow"))
        self.employee_username_label.setText(_translate("createInvoiceWindow", "User name"))
        self.employee_percentage_label.setText(_translate("createInvoiceWindow", "Percentage"))
        self.add_employee_btn.setText(_translate("createInvoiceWindow", "Add employee"))
        self.client_name_label.setText(_translate("createInvoiceWindow", "To (Client name)"))
        self.add_client_btn.setText(_translate("createInvoiceWindow", "Add client"))
        self.other_employees_label.setText(_translate("createInvoiceWindow", "Other employees shares"))
        self.invoice_date_frame.setText(_translate("createInvoiceWindow", "Invoice date"))
        self.invoice_date_edit.setDisplayFormat(_translate("createInvoiceWindow", "d/M/yyyy"))
        self.invoice_serial_number_label.setText(_translate("createInvoiceWindow", "Invoice serial number"))
        self.search_products_label.setText(_translate("createInvoiceWindow", "Search for products"))
        self.product_name_label.setText(_translate("createInvoiceWindow", "Product name"))
        self.bar_code_label.setText(_translate("createInvoiceWindow", "Barcode"))
        self.category_label.setText(_translate("createInvoiceWindow", "Product category"))
        self.brand_label.setText(_translate("createInvoiceWindow", "Product brand"))
        self.search_btn.setText(_translate("createInvoiceWindow", "Search"))
        self.create_btn.setText(_translate("createInvoiceWindow", "Create"))
        self.products_invoice_table_view.setText(_translate("createInvoiceWindow", "Products in invoice"))