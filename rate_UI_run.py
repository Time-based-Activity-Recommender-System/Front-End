#!/usr/bin/env python
from rateUI import Ui_MainWindow
import sys
from PyQt4 import QtGui,QtCore
import os

class Rate(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
	self.initUI()
	self.ui.next_pushButton_4.clicked.connect(self.time_enterpage)
	self.ui.movie_pushButton.clicked.connect(self.movierate)
        self.ui.book_pushButton_2.clicked.connect(self.bookrate)
	self.ui.music_pushButton_3.clicked.connect(self.musicrate)
	
    def initUI(self):
        self.setWindowTitle('Rate')
        self.center()
        self.show()

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def movierate(self):
        self.hide()
        os.system('python movieRatings_UI_run.py')

    def bookrate(self):
        self.hide()
        os.system('python bookRatings_UI_run.py')
    
    def musicrate(self):
        self.hide()
        os.system('python musicRatings_UI_run.py')

    def time_enterpage(self):
        self.hide()
        os.system('python entertime_UI_run.py')

    
def main():
    app=QtGui.QApplication(sys.argv) 
    ui = Rate() 
    #ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
