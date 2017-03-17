#!/usr/bin/env python
from loginUI import Ui_MainWindow
import sys
from PyQt4 import QtGui,QtCore

class Panel(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def main():
    app=QtGui.QApplication(sys.argv) 
    ui = Panel() 
    ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
