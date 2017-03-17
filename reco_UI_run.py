#!/usr/bin/env python
from recoUI import Ui_MainWindow
import sys
from PyQt4 import QtGui,QtCore
import os

class Panel(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.loginButton.clicked.connect(self.loginFunc)
        self.ui.signupButton.clicked.connect(self.signUpFunc)

    def loginFunc(self):
        os.system('python login_UI_run.py')

    def signUpFunc(self):
        os.system('python signup_UI_run.py')

def main():
    app=QtGui.QApplication(sys.argv) 
    ui = Panel() 
    ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
