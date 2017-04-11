#!/usr/bin/env python
from entertimeUI import Ui_MainWindow
import sys
from PyQt4 import QtGui,QtCore
import os
import pandas as pd 
import numpy as np


class Entertime(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
        self.disp_pop()
        self.ui.enter_pushButton.clicked.connect(self.input_time)	

    def initUI(self):
        self.setWindowTitle('Enter Time')
        self.center()
        self.show()

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def disp_pop(self):
        #display popular movies
        pop_cols = ['movie_id', 'movie_title']
        pop_movies = pd.read_csv('popular_movies.data', sep='\t', names=pop_cols, encoding='latin-1')
        l = len(pop_movies) 
        #print "Length = ", l
        ind1 = np.random.randint(0, l)
        ind2 = np.random.randint(0, l)
        ind3 = np.random.randint(0, l)
        
        while(ind1 == ind2):
            ind2 = np.random.randint(0, l)
        while(ind1 == ind3 or ind2 == ind3):
            ind3 = np.random.randint(0, l)
        
        self.ui.tableWidget.setItem(0, 0, QtGui.QTableWidgetItem(pop_movies['movie_title'][ind1]))
        self.ui.tableWidget.setItem(1, 0, QtGui.QTableWidgetItem(pop_movies['movie_title'][ind2]))
        self.ui.tableWidget.setItem(2, 0, QtGui.QTableWidgetItem(pop_movies['movie_title'][ind3]))
        
        #display popular songs
        pop_cols = ['song_id', 'song_title']
        pop_songs = pd.read_csv('popular_songs.data', sep='\t', names=pop_cols, encoding='latin-1')
        l = len(pop_songs) 
        #print "Length = ", l
        ind1 = np.random.randint(0, l)
        ind2 = np.random.randint(0, l)
        ind3 = np.random.randint(0, l)

        while(ind1 == ind2):
            ind2 = np.random.randint(0, l)
        while(ind1 == ind3 or ind2 == ind3):
            ind3 = np.random.randint(0, l)

        self.ui.tableWidget.setItem(0, 2, QtGui.QTableWidgetItem(pop_songs['song_title'][ind1]))
        self.ui.tableWidget.setItem(1, 2, QtGui.QTableWidgetItem(pop_songs['song_title'][ind2]))
        self.ui.tableWidget.setItem(2, 2, QtGui.QTableWidgetItem(pop_songs['song_title'][ind3]))

        pop_cols = ['book_id', 'book_title']
        pop_books = pd.read_csv('popular_books.data', sep=';', names=pop_cols, encoding='latin-1')
        l = len(pop_books) 
        #print "Length = ", l
        ind1 = np.random.randint(0, l)
        ind2 = np.random.randint(0, l)
        ind3 = np.random.randint(0, l)

        while(ind1 == ind2):
            ind2 = np.random.randint(0, l)
        while(ind1 == ind3 or ind2 == ind3):
            ind3 = np.random.randint(0, l)

        self.ui.tableWidget.setItem(0, 1, QtGui.QTableWidgetItem(pop_books['book_title'][ind1]))
        self.ui.tableWidget.setItem(1, 1, QtGui.QTableWidgetItem(pop_books['book_title'][ind2]))
        self.ui.tableWidget.setItem(2, 1, QtGui.QTableWidgetItem(pop_books['book_title'][ind3]))

        
        #print pop_movies['movie_title'][ind1]
	    #print pop_movies['movie_title'][ind2]
	    #print pop_movies['movie_title'][ind3]

        # ratings = np.zeros((num_movies, num_users+1), dtype = np.float)
        # for i in range(len(ratings)):
        # 	row = ratings_data['2movie_id'][i]-1
        # 	col = ratings_data['1user_id'][i]-1
        # 	ratings[row][col]=ratings_data['3rating'][i]

        # avg_ratings = ratings.sum(0)/(ratings != 0).sum(0)

        # print avg_ratings
        # ind = np.argpartition(avg_ratings, -4)[-4:]
        # ind2 = ratings_data['2movie_id'][ind]
        # print items['movie title'][ind2]

    def input_time(self):
        self.hr = self.ui.hrs_spinBox.value()
        self.min = self.ui.mins_spinBox_2.value()

        d = {'hour':[self.hr],'minute':[self.min]}
        df = pd.DataFrame(d)
        df.to_csv('time.txt',sep='\t',index=False, header=False)

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
