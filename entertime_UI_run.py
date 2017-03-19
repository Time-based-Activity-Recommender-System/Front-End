#!/usr/bin/env python
from entertimeUI import Ui_MainWindow
import sys
from PyQt4 import QtGui,QtCore
import os

class Entertime(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
        self.ui.enter_pushButton.clicked.connect(self.timeAlgo)

    def initUI(self):
        self.setWindowTitle('Rate')
        self.center()
        self.show()

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def timeAlgo(self):
        self.hr = self.ui.hrs_spinBox.value()
        self.min = self.mins_spinBox_2.value()
        if(self.hr == 0 and self.min < 15): #song(1 or 2)
            self.hide()
            os.system('python finalPage1_UI_run.py')  
        elif(self.hr == 0 and self.min >= 15): #3 songs and 1 book
            self.hide()
            os.system('python finalPage2_UI_run.py')
        elif(self.hr == 1):
            self.hide()
            os.system('python finalPage2_UI_run.py')
        elif(self.hr >= 2):
            self.hide()
            os.system('python finalPage3_UI_run.py')     

def main():
    app=QtGui.QApplication(sys.argv) 
    ui = Entertime() 
    #ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
