import os, csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

class AI:
    
    def __init__(self):
        super().__init__()
        self.get_data()
    
    def get_data(self):
        years = ['2010','2011','2012','2013','2014','2015','2016','2017','2018']
        for year in years:
            OPS_AB = np.array([])
            Y = np.array([])
            input_file = ('{cwd}\stats\Hitters_{input_year}.csv'.format(cwd=os.getcwd(), input_year = year))
            with open(input_file) as csvfile:
                csv_reader = csv.reader(csvfile, delimiter = ',')
                entry_count = 0
                for row in csv_reader:
                    try:
                        value = float(row[5]) * float(row[22])
                        OPS_AB = np.append(OPS_AB, value)
                        Y = np.append(Y, int(row[10]))
                    except:
                        print("Cannot append value {} or {}".format(row[5], row[10]))
                    
                    entry_count += 1
            linear_regressor = LinearRegression()
            OPS_AB1 = OPS_AB.reshape(-1,1)
            linear_regressor.fit(OPS_AB1,Y)
            print("The R-Squared score for At Bats multiplied by the OPS for {} is {}.".format(year,linear_regressor.score(OPS_AB1,Y)))
            Y_pred = linear_regressor.predict(OPS_AB1)
            plt.scatter(OPS_AB1,Y)
            plt.plot(OPS_AB1, Y_pred, color = 'red')
            plt.show()