#!/usr/bin/env python
from loginUI import Ui_MainWindow
import sys
from PyQt4 import QtGui,QtCore
import os
import pandas as pd

class Login(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
        self.ui.signup_pushButton.clicked.connect(self.signUpFunc)
	self.ui.login_pushButton.clicked.connect(self.newfunc)

    def newfunc(self):
	self.username = ""
	self.password = ""
	self.username = self.ui.username_lineEdit.text()
	self.password = self.ui.password_lineEdit.text()

	self.u_cols = ['1username', '2password', '3user_id']
	self.check = pd.read_csv('passwords.data', sep='\t', names=self.u_cols, encoding='latin-1')
	
	flag = 0
	for i in range(len(self.check)):
	    if(self.check['1username'][i]==self.username and self.check['2password'][i]==self.password):
		flag = 1

		whatevercols1 = ['whatever1']
		newno = {'whatever1':[self.username]}
		newdf = pd.DataFrame(newno)
                newdf.to_csv('session.data' ,sep='\t',index=False, header=False)
                 
		self.hide()
		os.system('python entertime_UI_run.py')   
	
	if(flag==0):
		QtGui.QMessageBox.critical(self,'Error!','Wrong User ID and password!')

    def initUI(self):
        self.setWindowTitle('Login')
        self.center()
        self.show()

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def signUpFunc(self):
        self.hide()
        os.system('python signup_UI_run.py')    
   
    def loginFunc(self):
        self.hide()
        os.system('python entertime_UI_run.py')

    def tryAgain(self):
	self.hide()
        os.system('python tryAgain_UI_run.py')    

def main():
    app=QtGui.QApplication(sys.argv) 
    ui = Login() 
    #ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
