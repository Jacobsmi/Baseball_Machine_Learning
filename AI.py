import os, csv

class AI:
    
    def __init__(self):
        super().__init__()
        self.get_data()
    
    def get_data(self):
        years = ['2010','2011','2012','2013','2014','2015','2016','2017','2010','2018','2019']
        for year in years:
            input_file = ('{cwd}\stats\Hitters_{input_year}.csv'.format(cwd=os.getcwd(), input_year = year))
            with open(input_file) as csvfile:
                csv_reader = csv.reader(csvfile, delimiter = ',')
                entry_count = 0
                for row in csv_reader:
                    entry_count += 1
                print('THE NUMBER OF ENTRIES FOR {year} IS {count}'.format(year=year, count=entry_count))
                    
