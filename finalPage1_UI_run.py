#!/usr/bin/env python
from finalPage1UI import Ui_MainWindow
import sys
from PyQt4 import QtGui,QtCore
import os
import pandas as pd

class FinalPage1(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
        self.reco()
        self.ui.pushButton_2.clicked.connect(self.home)
        self.ui.pushButton.clicked.connect(self.logout)

    def initUI(self):
        self.setWindowTitle('Recommendations')
        self.center()
        self.show()

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def reco(self):
        reco_cols = ['song_title']
        reco_songs = pd.read_csv('song_reco.data', sep='\t', names=reco_cols, encoding='latin-1')
        #TODO: DONT DISPLAY ALL 15 ALWAYS. LOOK AT TIME

        cols = ['hour', 'minute']
        time = pd.read_csv('time.txt', sep='\t', names=cols, encoding='latin-1')
        minute = time['minute'][0]        
        
        maxCol = 0
        if(minute <= 5):
            maxCol = 1;
        elif(minute <= 10):
            maxCol = 2;
        else:
            maxCol = 3;
        
        k=0
        for j in range(0,maxCol):
            for i in range(0,5):
                self.ui.tableWidget.setItem(i, j, QtGui.QTableWidgetItem(reco_songs['song_title'][k]))
                k = k + 1
        
    def home(self):
        self.hide()
        os.system('python entertime_UI_run.py')

    def logout(self):
        self.hide()
        os.system('python reco_UI_run.py')

def main():
    app=QtGui.QApplication(sys.argv) 
    ui = FinalPage1() 
    #ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
