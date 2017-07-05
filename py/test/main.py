from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os 
import design

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.btnBrowse.clicked.connect(self.browse_folder)

    def browse_folder(self):
        self.listWidget.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Pick a Folder")

        if directory :
            for file_name in os.listdir(directory):
                self.listWidget.addItem(file_name)

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
