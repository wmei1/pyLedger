from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QLayout, QLineEdit
import sys
import os
import pdb
import titleView
import budgetView
#import addLedgerWidget

class mainWindow(QtWidgets.QMainWindow, titleView.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        #init and show all ledgers list
        
        newLedger = QtWidgets.QListWidgetItem()

        widget = QtWidgets.QWidget()
        widgetText = QtWidgets.QLineEdit()
        widgetText.setObjectName("lineEdit")
        widgetText.setPlaceholderText("Test")
        widgetText.setFixedWidth(400)
        widgetBtn = QtWidgets.QPushButton("Add New Ledger")
        widgetBtn.setObjectName("addBtn")
        widgetLayout = QtWidgets.QHBoxLayout()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        widgetText.setSizePolicy(sizePolicy)
        
        widgetLayout.addWidget(widgetText)
        widgetLayout.addWidget(widgetBtn)
        widgetLayout.addStretch()
        widgetLayout.setContentsMargins(0,0,0,0)
        widgetLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        widget.setLayout(widgetLayout)
        
        self.listWidget.addItem(newLedger)
        self.listWidget.setItemWidget(newLedger, widget)
        
        widgetBtn.clicked.connect(self.addLedger)

    def addLedger(self):
        print("do something here")
        #dialog = QDialog()
        #dialog.ui=Ui_addLedger()
        #self.listWidget.setItemWidget(newLedger, addLedger)

        #self.central_widget = QtWidgets.QWidget()
        #self.setCentralWidget(budgetWidget())

class budgetWidget(QtWidgets.QWidget, budgetView.Ui_pyLedger):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = mainWindow()
    form.show()
    app.exec_()
if __name__ == '__main__':
    main()
