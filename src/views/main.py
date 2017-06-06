from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import titleView
import budgetView
class mainWindow(QtWidgets.QMainWindow, titleView.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        #init list, show any existing ledgers
        #create button widget
        newLedger = QtWidgets.QListWidgetItem()
        widget = QtWidgets.QWidget()
        self.listWidget.addItem("Test1")
        self.listWidget.addItem("Test2")
        self.listWidget.addItem("Test3")
        widgetText = QtWidgets.QTextEdit("New Ledger Here")
        #widgetText.set
        widgetButton = QtWidgets.QPushButton("Add New Ledger")
        widgetLayout = QtWidgets.QHBoxLayout()
        #widgetLayout.setAlignment(QtCore.Qt.AlignRight)
        widgetLayout.addWidget(widgetText)
        widgetLayout.addWidget(widgetButton)
        widgetLayout.addStretch()

        #widgetLayout.setSizeConstraint(QtWidgets.QLayout.setFixedSize)
        widget.setLayout(widgetLayout)
        newLedger.setSizeHint(widget.sizeHint())
        self.listWidget.addItem(newLedger)
        self.listWidget.setItemWidget(newLedger, widget)
        
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(budgetWidget())
        #app = QtWidgets.QApplication(sys.argv)
        #form = budgetView()
        #form.show()
        #app.exec_()

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
