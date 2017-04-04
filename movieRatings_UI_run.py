from movieRatingsUI import Ui_MainWindow
import sys
from PyQt4 import QtGui,QtCore
import os
import signal
import numpy as np
import pandas as pd
from scipy import optimize

num_movies = 1682
num_users = 943 #updated by temp.data

class MovieRatings(QtGui.QMainWindow):
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
        self.ui.save_next_Button.clicked.connect(self.back)
        self.connections()
        self.movies()
        
    def initUI(self):
        self.setWindowTitle('Movie Ratings')
        self.center()
        self.show()

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
    
    def appendNewRatings(self):
        r_cols = ['1user_id', '2movie_id', '3rating', '4unix_timestamp']
        self.ratings_data = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols, encoding='latin-1')


        d = {'1user_id': [self.newuser_id],  '2movie_id': [1], '3rating': self.newuser_ratings[0] , '4unix_timestamp':[800000000]}
        df = pd.DataFrame(d)
        df.to_csv('ml-100k/u.data',mode='a' ,sep='\t',index=False, header=False) 

        d = {'1user_id': [self.newuser_id],  '2movie_id': [50], '3rating': self.newuser_ratings[49] , '4unix_timestamp':[800000001]}
        df = pd.DataFrame(d)
        df.to_csv('ml-100k/u.data',mode='a' ,sep='\t',index=False, header=False) 

        d = {'1user_id': [self.newuser_id],  '2movie_id': [71], '3rating': self.newuser_ratings[70] , '4unix_timestamp':[800000002]}
        df = pd.DataFrame(d)
        df.to_csv('ml-100k/u.data',mode='a' ,sep='\t',index=False, header=False) 

        d = {'1user_id': [self.newuser_id],  '2movie_id': [64], '3rating': self.newuser_ratings[63] , '4unix_timestamp':[800000003]}
        df = pd.DataFrame(d)
        df.to_csv('ml-100k/u.data',mode='a' ,sep='\t',index=False, header=False) 

        d = {'1user_id': [self.newuser_id],  '2movie_id': [69], '3rating': self.newuser_ratings[68] , '4unix_timestamp':[800000004]}
        df = pd.DataFrame(d)
        df.to_csv('ml-100k/u.data',mode='a' ,sep='\t',index=False, header=False) 

        d = {'1user_id': [self.newuser_id],  '2movie_id': [72], '3rating': self.newuser_ratings[71] , '4unix_timestamp':[800000005]}
        df = pd.DataFrame(d)
        df.to_csv('ml-100k/u.data',mode='a' ,sep='\t',index=False, header=False) 

        d = {'1user_id': [self.newuser_id],  '2movie_id': [82], '3rating': self.newuser_ratings[81] , '4unix_timestamp':[800000006]}
        df = pd.DataFrame(d)
        df.to_csv('ml-100k/u.data',mode='a' ,sep='\t',index=False, header=False) 

        d = {'1user_id': [self.newuser_id],  '2movie_id': [88], '3rating': self.newuser_ratings[87] , '4unix_timestamp':[800000007]}
        df = pd.DataFrame(d)
        df.to_csv('ml-100k/u.data',mode='a' ,sep='\t',index=False, header=False) 

        d = {'1user_id': [self.newuser_id],  '2movie_id': [94], '3rating': self.newuser_ratings[93] , '4unix_timestamp':[800000008]}
        df = pd.DataFrame(d)
        df.to_csv('ml-100k/u.data',mode='a' ,sep='\t',index=False, header=False) 

        d = {'1user_id': [self.newuser_id],  '2movie_id': [98], '3rating': self.newuser_ratings[97] , '4unix_timestamp':[800000009]}
        df = pd.DataFrame(d)

        df.to_csv('ml-100k/u.data',mode='a' ,sep='\t',index=False, header=False) 
        self.ratings_data = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols, encoding='latin-1')
    
    def back(self):    
        self.appendNewRatings()
        self.recommenderSystem()

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
        self.newRatings()

    def movies(self):
        i_cols = ['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
        'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
        'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
        items = pd.read_csv('ml-100k/u.item', sep='|', names=i_cols,encoding='latin-1')
        self.ui.lineEdit_1.setText(items['movie title'][0])
        self.ui.lineEdit_2.setText(items['movie title'][49])
        self.ui.lineEdit_3.setText(items['movie title'][70])
        self.ui.lineEdit_4.setText(items['movie title'][63])
        self.ui.lineEdit_5.setText(items['movie title'][68])
        self.ui.lineEdit_6.setText(items['movie title'][71])
        self.ui.lineEdit_7.setText(items['movie title'][81])
        self.ui.lineEdit_8.setText(items['movie title'][87])
        self.ui.lineEdit_9.setText(items['movie title'][93])
        self.ui.lineEdit_10.setText(items['movie title'][97])

    def newRatings(self):
        global num_movies
        self.newuser_ratings = np.zeros((num_movies, 1))
        self.newuser_ratings[0] = int(self.ui.horizontalSlider_1.value())
        self.newuser_ratings[49] = int(self.ui.horizontalSlider_2.value())
        self.newuser_ratings[70] = int(self.ui.horizontalSlider_3.value())   
        self.newuser_ratings[63] = int(self.ui.horizontalSlider_4.value())
        self.newuser_ratings[68] = int(self.ui.horizontalSlider_5.value())
        self.newuser_ratings[71] = int(self.ui.horizontalSlider_6.value())
        self.newuser_ratings[81] = int(self.ui.horizontalSlider_7.value())
        self.newuser_ratings[87] = int(self.ui.horizontalSlider_8.value())
        self.newuser_ratings[93] = int(self.ui.horizontalSlider_9.value())
        self.newuser_ratings[97] = int(self.ui.horizontalSlider_10.value())
        
    
    def recommenderSystem(self):
        global num_movies
        global num_users

        #update num_users
        cols = ['count']
        count_data = pd.read_csv('temp.data', sep='\t', names=cols, encoding='latin-1') 
        num_users = count_data['count'][0] - 1
        print "num_users=",num_users

        self.ratings = np.zeros((num_movies, num_users), dtype = np.uint8) #num_users updated 
        #Create 2D ratings matrix
        for i in range(len(self.ratings_data)):
	        col = (int)(self.ratings_data['1user_id'][i])-1
	        row = (int)(self.ratings_data['2movie_id'][i])-1
	        self.ratings[row][col]=(int)(self.ratings_data['3rating'][i])
        
        self.did_rate = (self.ratings != 0) * 1

        self.ratings, ratings_mean = self.normalize_ratings()
        num_users = self.ratings.shape[1] #num_users gets updated i.e. increases by 1
        num_features = 3

        movie_features = np.random.randn( num_movies, num_features )
        user_prefs = np.random.randn( num_users, num_features )
        initial_X_and_theta = np.r_[movie_features.T.flatten(), user_prefs.T.flatten()]

        reg_param = 30
        minimized_cost_and_optimal_params = optimize.fmin_cg(self.calculate_cost, fprime=self.calculate_gradient, x0=initial_X_and_theta, args=(self.ratings, self.did_rate, num_users, num_movies, num_features, reg_param), maxiter=100, disp=True, full_output=True ) 
        cost, optimal_movie_features_and_user_prefs = minimized_cost_and_optimal_params[1], minimized_cost_and_optimal_params[0]

        movie_features, user_prefs = self.unroll_params(optimal_movie_features_and_user_prefs, num_users, num_movies, num_features)
        # Make some predictions (movie recommendations). Dot product
        all_predictions = movie_features.dot( user_prefs.T )
        # add back the ratings_mean column vector to my (our) predictions
        predictions_for_newuser = all_predictions[:, 0:1] + ratings_mean
        
        i_cols = ['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
        'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
        'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
        items = pd.read_csv('ml-100k/u.item', sep='|', names=i_cols,encoding='latin-1')
        ind = np.argpartition(predictions_for_newuser, -1)[-5:]
        
        ind2 = self.ratings_data['2movie_id'][0]
        #print items['movie title'][ind2]
        d = { 'movie_title': [ items['movie title'][ind2] ] }
        df = pd.DataFrame(d)
        df.to_csv('movie_reco.data' ,sep='\t',index=False, header=False)      

        for i in range(1,len(ind)):
            ind2 = self.ratings_data['2movie_id'][i]
            #print items['movie title'][ind2]
            d = { 'movie_title': [ items['movie title'][ind2] ] }
            df = pd.DataFrame(d)
            df.to_csv('movie_reco.data',mode='a' ,sep='\t',index=False, header=False)
            
    def normalize_ratings(self):
        global num_movies
        num_movies = self.ratings.shape[0]
        
        ratings_mean = np.zeros(shape = (num_movies, 1))
        ratings_norm = np.zeros(shape = self.ratings.shape)
        
        for i in range(num_movies):
            # Get all the indexes where there is a 1
            idx = np.where(self.did_rate[i] == 1)[0]
            #  Calculate mean rating of ith movie only from user's that gave a rating
            ratings_mean[i] = np.mean(self.ratings[i, idx])
            ratings_norm[i, idx] = self.ratings[i, idx] - ratings_mean[i]
            
        return ratings_norm, ratings_mean

    def unroll_params(self, X_and_theta, num_users, num_movies, num_features):
	    # Retrieve the X and theta matrixes from X_and_theta, based on their dimensions (num_features, num_movies, num_movies)
	    # --------------------------------------------------------------------------------------------------------------
	    # Get the first 30 (10 * 3) rows in the 48 X 1 column vector
	    first_30 = X_and_theta[:num_movies * num_features]
	    # Reshape this column vector into a 10 X 3 matrix
	    X = first_30.reshape((num_features, num_movies)).transpose()
	    # Get the rest of the 18 the numbers, after the first 30
	    last_18 = X_and_theta[num_movies * num_features:]
	    # Reshape this column vector into a 6 X 3 matrix
	    theta = last_18.reshape(num_features, num_users ).transpose()
	    return X, theta

    def calculate_gradient(self, X_and_theta, ratings, did_rate, num_users, num_movies, num_features, reg_param):
	    X, theta = self.unroll_params(X_and_theta, num_users, num_movies, num_features)

	    # we multiply by did_rate because we only want to consider observations for which a rating was given
	    difference = X.dot( theta.T ) * did_rate - ratings
	    X_grad = difference.dot( theta ) + reg_param * X
	    theta_grad = difference.T.dot( X ) + reg_param * theta

	    # wrap the gradients back into a column vector 
	    return np.r_[X_grad.T.flatten(), theta_grad.T.flatten()]
    
    def calculate_cost(self, X_and_theta, ratings, did_rate, num_users, num_movies, num_features, reg_param):
	    X, theta = self.unroll_params(X_and_theta, num_users, num_movies, num_features)
	    # we multiply (element-wise) by did_rate because we only want to consider observations for which a rating was given
	    cost = np.sum( (X.dot( theta.T ) * did_rate - ratings) ** 2 ) / 2
	    # '**' means an element-wise power
	    regularization = (reg_param / 2) * (np.sum( theta**2 ) + np.sum(X**2))
	    return cost + regularization

    


def main():
    app=QtGui.QApplication(sys.argv) 
    ui = MovieRatings() 
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()