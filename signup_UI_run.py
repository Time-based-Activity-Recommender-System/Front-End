#!/usr/bin/env python
from signupUI import Ui_MainWindow
import sys
from PyQt4 import QtGui,QtCore
import os
from numpy import *
import pandas as pd

class SignUp(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)      
        self.initUI()
        #self.credentials()
        self.ui.back_Button.clicked.connect(self.backFunc)
        self.ui.signup_button.clicked.connect(self.rateFunc)

    def initUI(self):
        self.setWindowTitle('Sign Up')
        self.center()
        self.show()

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
   

    def backFunc(self):
        self.hide()
        os.system('python login_UI_run.py')  

    def rateFunc(self):
        if(self.ui.userID_lineEdit.text() == "" or self.ui.password_lineEdit.text() == ""):
            QtGui.QMessageBox.critical(self,'Error!','UserID and Password is mandatory')
        else:
            p_cols = ['1user_id', '2Password', '3user_id']
            passwords_data = pd.read_csv('passwords.data', sep='\t', names=p_cols, encoding='latin-1')
            print passwords_data.tail()
            self.userID=""
            self.userID=self.ui.userID_lineEdit.text() 
            self.password=""
            self.password = self.ui.password_lineEdit.text() 
            flag = 0
            print "length=",len(passwords_data) 
            for i in range(0,len(passwords_data)):
                print "length=",len(passwords_data)
                if(passwords_data['1user_id'][i] == self.userID):
                    flag = 1
                    QtGui.QMessageBox.critical(self,'Error!','UserID already exists')
            if(flag == 0):
		whatevercols = ['whatever']
		userid = pd.read_csv('temp.data', sep='\t', names=whatevercols, encoding='latin-1')
		self.temp_userid = userid['whatever'][0]
                d = {'1user_id': [self.userID], '2Password':[self.password], '3user_id':[self.temp_userid]}
		df = pd.DataFrame(d)
		df.to_csv('passwords.data',mode='a' ,sep='\t',index=False, header=False)

		self.temp_userid = self.temp_userid + 1
		new = {'whatever':[self.temp_userid]}
		newdf = pd.DataFrame(new)
		newdf.to_csv('temp.data',sep='\t',index=False, header=False)

		whatevercols1 = ['whatever1']
		newno = {'whatever1':[self.userID]}
		newdf = pd.DataFrame(newno)
                newdf.to_csv('session.data' ,sep='\t',index=False, header=False)
                 
                self.hide()
                os.system('python rate_UI_run.py')
        

def main():
    app=QtGui.QApplication(sys.argv) 
    ui = SignUp() 
    #ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
