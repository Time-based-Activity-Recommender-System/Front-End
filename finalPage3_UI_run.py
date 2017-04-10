#!/usr/bin/env python
from finalPage3UI import Ui_MainWindow
import sys
from PyQt4 import QtGui,QtCore
import os
import pandas as pd

class FinalPage3(QtGui.QMainWindow):
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
        reco_cols = ['song_title']
        reco_songs = pd.read_csv('song_reco.data', sep='\t', names=reco_cols, encoding='latin-1')
        print reco_songs['song_title'][0]
        #TODO: DONT DISPLAY ALL 15 ALWAYS. LOOK AT TIME
        
        k=0
        for j in range(0,5):
            for i in range(0,5):
                self.ui.tableWidget.setItem(i, j, QtGui.QTableWidgetItem(reco_songs['song_title'][k]))
                k = k + 1
                if(k == 15):
                    break
            if(k == 15):
                break

        #recommend books 
        #!/usr/bin/env python
from finalPage3UI import Ui_MainWindow
import sys
from PyQt4 import QtGui,QtCore
import os
import pandas as pd

class FinalPage3(QtGui.QMainWindow):
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
        reco_cols = ['song_title']
        reco_songs = pd.read_csv('song_reco.data', sep='\t', names=reco_cols, encoding='latin-1')
        print reco_songs['song_title'][0]
        #TODO: DONT DISPLAY ALL 15 ALWAYS. LOOK AT TIME
        
        k=0
        for j in range(0,5):
            for i in range(0,5):
                self.ui.tableWidget.setItem(i, j, QtGui.QTableWidgetItem(reco_songs['song_title'][k]))
                k = k + 1
                if(k == 15):
                    break
            if(k == 15):
                break

        #recommend books 
        #!/usr/bin/env python
from finalPage3UI import Ui_MainWindow
import sys
from PyQt4 import QtGui,QtCore
import os
import pandas as pd

class FinalPage3(QtGui.QMainWindow):
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
        reco_cols = ['song_title']
        reco_songs = pd.read_csv('song_reco.data', sep='\t', names=reco_cols, encoding='latin-1')
        print reco_songs['song_title'][0]
        #TODO: DONT DISPLAY ALL 15 ALWAYS. LOOK AT TIME
        
        k=0
        for j in range(0,5):
            for i in range(0,5):
                self.ui.tableWidget.setItem(i, j, QtGui.QTableWidgetItem(reco_songs['song_title'][k]))
                k = k + 1
                if(k == 15):
                    break
            if(k == 15):
                break

        #recommend books 
        
	reco_bcols = ['book_title']
        
	reco_books = pd.read_csv('book_reco.data', sep='\t', names=reco_bcols, encoding='latin-1')
        k=0
        for i in range(0,5):
            self.ui.tableWidget_2.setItem(i, 0, QtGui.QTableWidgetItem(reco_books['book_title'][k+1]))
            k = k + 1
            

	for i in range(0,5):
            self.ui.tableWidget_2.setItem(i, 1, QtGui.QTableWidgetItem(reco_books['book_title'][k+1]))
            k = k + 1

        #recommend movies
        reco_cols = ['movie_title']
        reco_movies = pd.read_csv('movie_reco.data', sep='\t', names=reco_cols, encoding='latin-1')
        print reco_movies['movie_title'][0]
        
        k=0
        for i in range(0,5):
            self.ui.tableWidget_3.setItem(i, 0, QtGui.QTableWidgetItem(reco_movies['movie_title'][k+1]))
            k = k + 1
                
    def home(self):
        self.hide()
        os.system('python entertime_UI_run.py')

    def logout(self):
        self.hide()
        os.system('python reco_UI_run.py')

def main():
    app=QtGui.QApplication(sys.argv) 
    ui = FinalPage3() 
    #ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

