from PyQt5 import QtWidgets, QtGui, QtCore
import sys
class MyApp(object):    
    def __init__(self):
        super(MyApp, self).__init__()                
        self.mainWidget = QtWidgets.QWidget()
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainWidget.setLayout(self.mainLayout)

        self.hLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.insertLayout(0, self.hLayout)


        self.listA=QtWidgets.QTreeWidget()
        self.listA.setColumnCount(3)
        self.listA.setHeaderLabels(['Checkbox','Name','Data'])
        for i in range(3):
            item=QtWidgets.QTreeWidgetItem()
            item.setCheckState(0,QtCore.Qt.Checked)
            item.setText(1, 'Item '+str(i))
            item.setData(2, QtCore.Qt.UserRole, id(item) )
            item.setText(2, str(id(item) ) )
            self.listA.addTopLevelItem(item)

        self.hLayout.addWidget(self.listA)

        self.buttonGroupbox = QtWidgets.QGroupBox()
        self.buttonlayout = QtWidgets.QVBoxLayout()
        self.buttonGroupbox.setLayout(self.buttonlayout)

        okButton = QtWidgets.QPushButton('Remove Selected')
        okButton.clicked.connect(self.removeSel)
        self.buttonlayout.addWidget(okButton)

        getDataButton = QtWidgets.QPushButton('Get Items Data')
        getDataButton.clicked.connect(self.getItemsData)
        self.buttonlayout.addWidget(getDataButton)

        self.mainLayout.addWidget(self.buttonGroupbox)
        self.mainWidget.show()
        sys.exit(app.exec_())

    def removeSel(self):
        listItems=self.listA.selectedItems()
        if not listItems: return   
        for item in listItems:
            itemIndex=self.listA.indexOfTopLevelItem(item)
            self.listA.takeTopLevelItem(itemIndex)
        print( '\n\t Number of items remaining', self.listA.topLevelItemCount())

    def getItemsData(self):
        for i in range(self.listA.topLevelItemCount()):
            item=self.listA.topLevelItem(i)
            itmData=item.data(2, QtCore.Qt.UserRole)
            itemId=itmData.toPyObject()
            print ('\n\t Item Id Stored as Item Data:', itemId, 'Item Checkbox State:', item.checkState(0))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MyApp()
