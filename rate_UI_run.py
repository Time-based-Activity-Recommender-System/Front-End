#!/usr/bin/env python
from rateUI import Ui_MainWindow
import sys
from PyQt4 import QtGui,QtCore

class Rate(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
	self.initUI()

    def initUI(self):
        self.setWindowTitle('Rate')
        self.center()
        self.show()

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

def main():
    app=QtGui.QApplication(sys.argv) 
    ui = Rate() 
    #ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
