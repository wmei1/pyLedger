from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QLayout, QLineEdit
import sys  
import os
import pickle
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
        self.widgetText.setPlaceholderText("My Ledger")
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


    def addLedger(self):
        name = self.widgetText.text()
        if name:
            print(name)
            self.listWidget.clear()
            mainWindow.ledgerList.insert(len(mainWindow.ledgerList), name)
            #for item in mainWindow.ledgerList:
            #    self.listWidget.addItem(item)
            self.initLedgers()
        else:
            print("empty")
            self.widgetText.setPlaceholderText("invalid name")

    def contextMenuEvent(self, event):
        selectedItem = self.listWidget.itemAt(event.x()-11, event.y()-71)
        if not selectedItem.toolTip() == "addBar":
            menu = QtWidgets.QMenu(self)
            deleteAction = menu.addAction("Delete")
            action = menu.exec_(self.mapToGlobal(event.pos()))
            if action == deleteAction:
                row = self.listWidget.row(selectedItem)
                self.listWidget.takeItem(row)
                del mainWindow.ledgerList[row]
                #print(len(mainWindow.ledgerList))

    def itemClicked(self,item):
        self.window.central_widget = QtWidgets.QWidget()
        mainWindow.item = item.text()
        self.window.setCentralWidget(budgetWidget(self.window))
        
        print('click:'+mainWindow.item)
    

class budgetWidget(QtWidgets.QWidget, budgetView.Ui_pyLedger):
    def __init__(self,window):
        super(self.__class__, self).__init__()
        self.setFixedSize(1280,720)
        self.window = window
        self.setupUi(self)
        self.btnLedger.setText(mainWindow.item)
        print(mainWindow.item)
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
    if( os.path.isfile('./ledgerList.p') ):
        mainWindow.ledgerList=pickle.load(open("./ledgerList.p","rb"))
        print('loading')
        print(mainWindow.ledgerList)
        
    app = QtWidgets.QApplication(sys.argv)
    window = initWindow()
    window.show()
    app.exec_()
    pickle.dump(mainWindow.ledgerList,open("ledgerList.p","wb"))
    print(mainWindow.ledgerList)


