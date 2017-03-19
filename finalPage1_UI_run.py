#!/usr/bin/env python
from finalPage1UI import Ui_MainWindow
import sys
from PyQt4 import QtGui,QtCore
import os

class FinalPage1(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
        self.ui.pushButton_2.clicked.connect(self.home)

    def initUI(self):
        self.setWindowTitle('Recommendations')
        self.center()
        self.show()

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def home(self):
        self.hide()
        os.system('python entertime_UI_run.py')

def main():
    app=QtGui.QApplication(sys.argv) 
    ui = FinalPage1() 
    #ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
