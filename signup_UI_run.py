#!/usr/bin/env python
from signupUI import Ui_MainWindow
import sys
from PyQt4 import QtGui,QtCore


class SignUp(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.credentials()

    def credentials(self): 
        self.name = self.ui.name_lineEdit
        self.password = self.ui.password_lineEdit
        #TODO: name,password check in database     

def main():
    app=QtGui.QApplication(sys.argv) 
    ui = SignUp() 
    ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
