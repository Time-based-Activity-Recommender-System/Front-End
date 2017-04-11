#!/usr/bin/env python
from finalPage2UI import Ui_MainWindow
import sys
from PyQt4 import QtGui,QtCore
import os
import pandas as pd

class FinalPage2(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
        self.reco()
        self.ui.pushButton.clicked.connect(self.home)
        self.ui.pushButton_2.clicked.connect(self.logout)

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
        #recommend songs
        reco_scols = ['song_title']
	reco_bcols = ['book_title']
        reco_songs = pd.read_csv('song_reco.data', sep='\t', names=reco_scols, encoding='latin-1')
	reco_books = pd.read_csv('book_reco.data', sep='\t', names=reco_bcols, encoding='latin-1')
        print reco_songs['song_title'][0]
        #TODO: DONT DISPLAY ALL 15 ALWAYS. LOOK AT TIME
        
        k=0
        for j in range(0,5):
            for i in range(0,5):
                self.ui.tableWidget.setItem(i, j, QtGui.QTableWidgetItem(reco_songs['song_title'][k]))
		#self.ui.tableWidget.setItem(i, j, QtGui.QTableWidgetItem(reco_books['book_title'][k]))
                k = k + 1
                if(k == 15):
                    break
            if(k == 15):
                break

        #recommend books 
        #TODO

	cols = ['hour', 'minute']
        time = pd.read_csv('time.txt', sep='\t', names=cols, encoding='latin-1')
        minute = time['minute'][0]  
	hour = time['hour'][0]      
        print hour
        maxCol = 0
        if(hour<1):
            maxCol = 1;
        else:
            maxCol = 2;

	k=0
        for i in range(0,5):
            self.ui.tableWidget_2.setItem(i, 0, QtGui.QTableWidgetItem(reco_books['book_title'][k+1]))
            k = k + 1
            

	if(maxCol==2):
	    for i in range(0,5):
                self.ui.tableWidget_2.setItem(i, 1, QtGui.QTableWidgetItem(reco_books['book_title'][k+1]))
                k = k + 1
            

    def home(self):
        self.hide()
        os.system('python entertime_UI_run.py')
    
    def logout(self):
        self.hide()
        os.system('python reco_UI_run.py')

def main():
    app=QtGui.QApplication(sys.argv) 
    ui = FinalPage2() 
    #ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
