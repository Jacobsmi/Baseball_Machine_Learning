import os, csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

class AI:
    
    def __init__(self):
        super().__init__()
        self.get_data()
    
    def get_data(self):
        years = ['2010','2011','2012','2013','2014','2015','2016','2017','2010','2018']
        X = np.array([])
        Y = np.array([])
        for year in years:
            input_file = ('{cwd}\stats\Hitters_{input_year}.csv'.format(cwd=os.getcwd(), input_year = year))
            with open(input_file) as csvfile:
                csv_reader = csv.reader(csvfile, delimiter = ',')
                entry_count = 0
                for row in csv_reader:
                    try:
                        X = np.append(X, int(row[5]))
                        Y = np.append(Y, int(row[10]))
                    except:
                        print("Cannot append value {} or {}".format(row[5], row[10]))
                    
                    entry_count += 1
            print('THE NUMBER OF ENTRIES FOR {year} IS {count}'.format(year=year, count=entry_count))
        X1 = X.reshape(-1,1)
        linear_regressor = LinearRegression()
        linear_regressor.fit(X1,Y)
        Y_pred = linear_regressor.predict(X1)
        plt.scatter(X,Y)
        plt.plot(X, Y_pred, color = 'red')
        plt.show()