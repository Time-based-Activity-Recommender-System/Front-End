#!/usr/bin/env python
from signupUI import Ui_MainWindow
import sys
from PyQt4 import QtGui,QtCore
import os

class SignUp(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)      
        self.initUI()
        self.credentials()
        self.ui.back_Button.clicked.connect(self.backFunc)
        self.ui.signup_button.clicked.connect(self.rateFunc)

    def initUI(self):
        self.setWindowTitle('SignUp')
        self.center()
        self.show()

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def credentials(self): 
        self.name = self.ui.name_lineEdit
        self.password = self.ui.password_lineEdit
        #TODO: name,password check in database   

    def backFunc(self):
        self.hide()
        os.system('python login_UI_run.py')  

    def rateFunc(self):
        self.hide()
        os.system('python rate_UI_run.py')
        

def main():
    app=QtGui.QApplication(sys.argv) 
    ui = SignUp() 
    #ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
