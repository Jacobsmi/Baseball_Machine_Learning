import os, csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

class AI:
    
    def __init__(self):
        super().__init__()
        data = self.get_data(['2010','2011','2012','2013','2014','2015','2016','2017','2018'])
        model_data = self.create_model(data)
        self.predict(['2019'], model_data)
    
    def get_data(self, years):
        OPS_AB = np.array([])
        Y = np.array([])
        for year in years:
            path = os.path.join(os.getcwd(),'stats','Hitters_{input_year}.csv'.format(input_year = year))   
            with open(path) as csvfile:
                csv_reader = csv.reader(csvfile, delimiter = ',')
                entry_count = 0
                for row in csv_reader:
                    try:
                        value = float(row[5]) * float(row[22])
                        OPS_AB = np.append(OPS_AB, value)
                        Y = np.append(Y, int(row[10]))
                        entry_count += 1
                    except:
                        print("Cannot append value {} or {}".format(row[5], row[10]))
        # end for
        return([OPS_AB, Y])
    
    def create_model(self, data):
        OPS_AB = data[0]
        Y = data[1]
        linear_regressor = LinearRegression()
        OPS_AB1 = OPS_AB.reshape(-1,1)
        linear_regressor.fit(OPS_AB1,Y)
        print("The R-Squared score for At Bats multiplied by the OPS for is {}.".format(linear_regressor.score(OPS_AB1,Y)))
        print("Intercept: ",linear_regressor.intercept_)
        print("Slope: ", linear_regressor.coef_)
        Y_pred = linear_regressor.predict(OPS_AB1)
        plt.scatter(OPS_AB1,Y)
        plt.plot(OPS_AB1, Y_pred, color = 'red')
        plt.show()
        return([linear_regressor.intercept_, linear_regressor.coef_])

    def predict(self, years, model_data):
        intercept = model_data[0]
        coef = model_data[1]
        # variable that tracks the total error percentage so that the average can be calculated
        total_error = 0
        # Variable that tracks the total number of entries so that the average error can be calculated
        num_entries = 0
        for year in years:
            path = os.path.join(os.getcwd(),'stats','Hitters_{input_year}.csv'.format(input_year = year))   
            with open(path) as csvfile:
                csv_reader = csv.reader(csvfile, delimiter = ',')
                entry_count = 0
                for row in csv_reader:
                    try:
                        actual = float(row[10])
                        if(actual > 0):
                            value = float(row[5]) * float(row[22])
                            Y_PRED = coef * value + intercept 
                            # print("Predicted value for OPS_AB {} was {} and the actual value was {} ".format(value,Y_PRED,actual))
                            error = abs(Y_PRED - actual)
                            percent_error = (error / actual)
                            num_entries += 1
                            total_error += percent_error
                            print("There percentage of error for {} was {} and the actual value was {}".format(error, percent_error, actual))
                    except Exception as e: 
                        print(e)
        # end for
        # Calculating average error for predictions
        avg_err = total_error / num_entries
        print("The average amount of error was {}".format(avg_err))




            
