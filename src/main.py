from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QLayout, QLineEdit
import sys
import os
import pdb
import gui.titleView2 as titleView
import gui.budgetView as budgetView
#import addLedgerWidget

class mainWindow(QtWidgets.QMainWindow, titleView.Ui_MainWindow):
    ledgerList = []
    item = ""
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        #init and show all ledgers list
        self.initLedgers()
       
        #self.widgetBtn.clicked.connect(self.addLedger)

    def initLedgers(self):
        newItem = QtWidgets.QListWidgetItem()

        widget = QtWidgets.QWidget()
        self.widgetText = QtWidgets.QLineEdit()
        self.widgetText.setObjectName("lineEdit")
        self.widgetText.setPlaceholderText("Test")
        #self.widgetText.setFixedWidth(400)
        self.widgetBtn = QtWidgets.QPushButton("Add New Ledger")
        self.widgetBtn.setObjectName("addBtn")
        widgetLayout = QtWidgets.QHBoxLayout()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        self.widgetText.setSizePolicy(sizePolicy)
        
        widgetLayout.addWidget(self.widgetText)
        widgetLayout.addWidget(self.widgetBtn)
        widgetLayout.addStretch()
        widgetLayout.setContentsMargins(0,0,0,0)
        widgetLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        widget.setLayout(widgetLayout)
        self.listWidget.addItem(newItem)
        self.listWidget.setItemWidget(newItem, widget)
        self.widgetBtn.clicked.connect(self.addLedger)
        self.listWidget.itemClicked.connect(self.itemClicked)
    
        
    def addLedger(self):
        name = self.widgetText.text()
        if name:
            print(name)
            self.listWidget.clear()
            mainWindow.ledgerList.insert(len(mainWindow.ledgerList), name)
            for item in mainWindow.ledgerList:
                self.listWidget.addItem(item)
            self.initLedgers()
        else:
            print("empty")

    def itemClicked(self,item):
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(budgetWidget())
        mainWindow.item = item.text()

class budgetWidget(QtWidgets.QWidget, budgetView.Ui_pyLedger):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setFixedSize(1280,720)
        self.setupUi(self)
        self.btnLedger.setText(mainWindow.item)
        


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = mainWindow()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
