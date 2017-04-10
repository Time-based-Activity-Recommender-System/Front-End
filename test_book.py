from bookRatingsUI import Ui_MainWindow
import sys
from PyQt4 import QtGui,QtCore
import os
import signal
import numpy as np
import pandas as pd
from scipy import optimize

num_movies = 1682
num_users = 943 #updated by temp.data

class BookRatings(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

	#to get newuser_id
        c_cols = ['current_user']
        current_user_data = pd.read_csv('session.data', sep='\t', names=c_cols, encoding='latin-1') 
        name = current_user_data['current_user'][0]
        
        p_cols = ['1user_id', '2Password', '3user_id'] #first user_id is user name, 3rd column is system generated
        passwords_data = pd.read_csv('passwords.data', sep='\t', names=p_cols, encoding='latin-1')
        for i in range(len(passwords_data)):
            if( passwords_data['1user_id'][i] == name ):
                self.newuser_id = passwords_data['3user_id'][i]
                break

	print "newuser_id=",self.newuser_id 
	
        self.ui.save_next_pushButton.clicked.connect(self.back)
        self.connections()
	self.books()
	self.disp_reco()
        
    def initUI(self):
        self.setWindowTitle('Book Ratings')
        self.center()
        self.show()

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def back(self):
        self.hide()
        os.system('python rate_UI_run.py')
    
    def connections(self):
        self.connect(self.ui.horizontalSlider_1,QtCore.SIGNAL("valueChanged(int)"),self.sliderVal)
        self.connect(self.ui.horizontalSlider_2,QtCore.SIGNAL("valueChanged(int)"),self.sliderVal)
        self.connect(self.ui.horizontalSlider_3,QtCore.SIGNAL("valueChanged(int)"),self.sliderVal)
        self.connect(self.ui.horizontalSlider_4,QtCore.SIGNAL("valueChanged(int)"),self.sliderVal)
        self.connect(self.ui.horizontalSlider_5,QtCore.SIGNAL("valueChanged(int)"),self.sliderVal)
        self.connect(self.ui.horizontalSlider_6,QtCore.SIGNAL("valueChanged(int)"),self.sliderVal)
        self.connect(self.ui.horizontalSlider_7,QtCore.SIGNAL("valueChanged(int)"),self.sliderVal)
        self.connect(self.ui.horizontalSlider_8,QtCore.SIGNAL("valueChanged(int)"),self.sliderVal)
        self.connect(self.ui.horizontalSlider_9,QtCore.SIGNAL("valueChanged(int)"),self.sliderVal) 
        self.connect(self.ui.horizontalSlider_10,QtCore.SIGNAL("valueChanged(int)"),self.sliderVal) 

    def sliderVal(self):
        self.ui.lineEdit_11.setText(str(self.ui.horizontalSlider_1.value()))
        self.ui.lineEdit_12.setText(str(self.ui.horizontalSlider_2.value()))
        self.ui.lineEdit_13.setText(str(self.ui.horizontalSlider_3.value()))
        self.ui.lineEdit_14.setText(str(self.ui.horizontalSlider_4.value()))
        self.ui.lineEdit_15.setText(str(self.ui.horizontalSlider_5.value()))
        self.ui.lineEdit_16.setText(str(self.ui.horizontalSlider_6.value()))
        self.ui.lineEdit_17.setText(str(self.ui.horizontalSlider_7.value()))
        self.ui.lineEdit_18.setText(str(self.ui.horizontalSlider_8.value()))
        self.ui.lineEdit_19.setText(str(self.ui.horizontalSlider_9.value()))
        self.ui.lineEdit_20.setText(str(self.ui.horizontalSlider_10.value()))

    def books(self):
	print "asmita"
        i_cols = ['1ID','2Book']
        items = pd.read_csv('ratebook.data', sep=';', names=i_cols, encoding='latin-1')
		        
	self.ui.lineEdit_1.setText(items['2Book'][0]) #16
        self.ui.lineEdit_2.setText(items['2Book'][1]) #39
        self.ui.lineEdit_3.setText(items['2Book'][2]) #253
        self.ui.lineEdit_4.setText(items['2Book'][3])
        self.ui.lineEdit_5.setText(items['2Book'][4]) #283
        self.ui.lineEdit_6.setText(items['2Book'][5]) #750
        self.ui.lineEdit_7.setText(items['2Book'][6]) 
        self.ui.lineEdit_8.setText(items['2Book'][7])
        self.ui.lineEdit_9.setText(items['2Book'][8]) #105711
        self.ui.lineEdit_10.setText(items['2Book'][9]) #107290

    def disp_reco(self):
	
	pop_cols = ['book_id', 'book_title']
        items = pd.read_csv('book.data', sep=';', names=pop_cols, encoding='latin-1')
        l = len(items) 
        
        ind1 = np.random.randint(0, 2)
        ind2 = np.random.randint(2, 4)
        ind3 = np.random.randint(4, 7)
	ind4 = np.random.randint(7, 10)
        ind5 = np.random.randint(10, 12)
	ind6 = np.random.randint(12, 16)
        ind7 = np.random.randint(16, 18)
	ind8 = np.random.randint(18, 20)
	ind9 = np.random.randint(10, 23)
	ind10 = np.random.randint(23, 25)
        
        #print items['movie title'][ind2]
        d = { 'movie_title': [ items['book_title'][ind1] ] }
        df = pd.DataFrame(d)
        df.to_csv('movie_reco.data' ,sep='\t',index=False, header=False)      

        d= { 'movie_title': [ items['book_title'][ind1] ] }
        df = pd.DataFrame(d)
        df.to_csv('movie_reco.data',mode='a' ,sep='\t',index=False, header=False)
	
	d= { 'movie_title': [ items['book_title'][ind2] ] }
        df = pd.DataFrame(d)
        df.to_csv('movie_reco.data',mode='a' ,sep='\t',index=False, header=False)

	d= { 'movie_title': [ items['book_title'][ind3] ] }
        df = pd.DataFrame(d)
        df.to_csv('movie_reco.data',mode='a' ,sep='\t',index=False, header=False)

	d= { 'movie_title': [ items['book_title'][ind4] ] }
        df = pd.DataFrame(d)
        df.to_csv('movie_reco.data',mode='a' ,sep='\t',index=False, header=False)

	d= { 'movie_title': [ items['book_title'][ind5] ] }
        df = pd.DataFrame(d)
        df.to_csv('movie_reco.data',mode='a' ,sep='\t',index=False, header=False)

	d= { 'movie_title': [ items['book_title'][ind6] ] }
        df = pd.DataFrame(d)
        df.to_csv('movie_reco.data',mode='a' ,sep='\t',index=False, header=False)

	d= { 'movie_title': [ items['book_title'][ind7] ] }
        df = pd.DataFrame(d)
        df.to_csv('movie_reco.data',mode='a' ,sep='\t',index=False, header=False)

	d= { 'movie_title': [ items['book_title'][ind8] ] }
        df = pd.DataFrame(d)
        df.to_csv('movie_reco.data',mode='a' ,sep='\t',index=False, header=False)

	d= { 'movie_title': [ items['book_title'][ind9] ] }
        df = pd.DataFrame(d)
        df.to_csv('movie_reco.data',mode='a' ,sep='\t',index=False, header=False)

	d= { 'movie_title': [ items['book_title'][ind10] ] }
        df = pd.DataFrame(d)
        df.to_csv('movie_reco.data',mode='a' ,sep='\t',index=False, header=False)

def main():
    app=QtGui.QApplication(sys.argv) 
    ui = BookRatings() 
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
