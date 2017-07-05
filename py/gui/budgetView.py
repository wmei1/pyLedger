# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'budgetView.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_pyLedger(object):
    def setupUi(self, pyLedger):
        pyLedger.setObjectName("pyLedger")
        pyLedger.resize(1280, 720)
        self.horizontalLayout = QtWidgets.QHBoxLayout(pyLedger)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnLedger = QtWidgets.QPushButton(pyLedger)
        self.btnLedger.setObjectName("btnLedger")
        self.verticalLayout.addWidget(self.btnLedger)
        self.listWidget = QtWidgets.QListWidget(pyLedger)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.columnView = QtWidgets.QColumnView(pyLedger)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.columnView.sizePolicy().hasHeightForWidth())
        self.columnView.setSizePolicy(sizePolicy)
        self.columnView.setObjectName("columnView")
        self.verticalLayout_2.addWidget(self.columnView)
        self.tableWidget = QtWidgets.QTableWidget(pyLedger)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(pyLedger)
        QtCore.QMetaObject.connectSlotsByName(pyLedger)

    def retranslateUi(self, pyLedger):
        _translate = QtCore.QCoreApplication.translate
        pyLedger.setWindowTitle(_translate("pyLedger", "Form"))
        self.btnLedger.setText(_translate("pyLedger", "ledger_name"))

