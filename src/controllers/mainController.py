from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QLayout, QLineEdit
import sys
import os
import pdb
import gui.titleView as titleView
import gui.budgetView as budgetView
#import addLedgerWidget

class mainWindow(QtWidgets.QWidget, titleView.Ui_Form):
    ledgerList = []
    item = ""
    def __init__(self,window):
        super(self.__class__, self).__init__()
        self.window = window
        self.setupUi(self)
        #init and show all ledgers list
        self.initLedgers()
       
        #self.widgetBtn.clicked.connect(self.addLedger)

    def initLedgers(self):
        self.listWidget.clear()
        for item in mainWindow.ledgerList:
            self.listWidget.addItem(item)
        
        newItem = QtWidgets.QListWidgetItem()
        newItem.setToolTip("addBar")
        widget = QtWidgets.QWidget()
        widget.setObjectName("addBar")
        self.widgetText = QtWidgets.QLineEdit()
        self.widgetText.setObjectName("lineEdit")
        self.widgetText.setPlaceholderText("Test")
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
        widgetLayout.setSpacing(0)
        widgetLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        widget.setLayout(widgetLayout)
        self.listWidget.addItem(newItem)
        self.listWidget.setItemWidget(newItem, widget)
        self.widgetBtn.clicked.connect(self.addLedger)
        self.listWidget.itemClicked.connect(self.itemClicked)
        #self.listWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #self.listWidget.customContextMenuRequested.connect(self.onRightClick)

        
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
    def contextMenuEvent(self, event):
        print("contextMenu: ", self.listWidget.itemAt(event.x()-11, event.y()-71).text())
        selectedItem = self.listWidget.itemAt(event.x()-11, event.y()-71).toolTip()
        if not selectedItem == "addBar":
            item = self.listWidget.itemAt(event.x()-11, event.y()-71)
            menu = QtWidgets.QMenu(self)
            deleteAction = menu.addAction("Delete")
            action = menu.exec_(self.mapToGlobal(event.pos()))
            if action == deleteAction:
                row = self.listWidget.row(item)
                self.listWidget.takeItem(row)
                del mainWindow.ledgerList[row]
        #self.listWidget.takeItem(self.listWidget.itemAt(event.pos()).row())

    def itemClicked(self,item):
        if QtWidgets.qApp.mouseButtons() & QtCore.Qt.RightButton:
            print("Right Clicked")
        self.window.central_widget = QtWidgets.QWidget()
        self.window.setCentralWidget(budgetWidget(self.window))
        mainWindow.item = item.text()
    

class budgetWidget(QtWidgets.QWidget, budgetView.Ui_pyLedger):
    def __init__(self,window):
        super(self.__class__, self).__init__()
        self.setFixedSize(1280,720)
        self.window = window
        self.setupUi(self)
        self.btnLedger.setText(mainWindow.item)
        self.btnLedger.clicked.connect(self.backToLedgers)

    def backToLedgers(self):
        #self.window = QtWidgets.QMainWindow()
        self.window.central_widget = QtWidgets.QWidget()
        self.window.setCentralWidget(mainWindow(self.window))
        self.window.adjustSize()

        
def initWindow():
    window = QtWidgets.QMainWindow()
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(window.sizePolicy().hasHeightForWidth())
    window.setSizePolicy(sizePolicy) 
    window.central_widget = QtWidgets.QWidget()
    window.centralwidget = QtWidgets.QWidget(window)
    window.verticalLayout = QtWidgets.QVBoxLayout(window.centralwidget)
    
    window.setCentralWidget(mainWindow(window))
    return window


def __init__():
    app = QtWidgets.QApplication(sys.argv)
    window = initWindow()
    window.show()
    app.exec_()


