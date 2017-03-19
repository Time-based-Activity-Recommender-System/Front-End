from bookRatingsUI import Ui_MainWindow
import sys
from PyQt4 import QtGui,QtCore
import os
import signal

class BookRatings(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
        self.ui.save_next_pushButton.clicked.connect(self.back)
        self.connections()
        
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

def main():
    app=QtGui.QApplication(sys.argv) 
    ui = BookRatings() 
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
