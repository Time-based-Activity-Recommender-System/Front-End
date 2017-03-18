from movieRatings import Ui_MainWindow
import sys
from PyQt4 import QtGui,QtCore
import os

class MovieRatings(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Login')
        self.center()
        self.show()

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

def main():
    app=QtGui.QApplication(sys.argv) 
    ui = MovieRatings() 
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()