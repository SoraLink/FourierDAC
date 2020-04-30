import csv
import os
from datetime import datetime

class logger:
    def __init__(self, columns):
        self._columns = columns
        self._data_storage = [0]*len(columns)
        self._nameOfFolder = str(datetime.now().strftime("%Y%m%d-%H%M%S"))
        self._path = os.getcwd()+'\\'+'data'+'\\'+self._nameOfFolder
        self._path.replace(' ','')
        if not os.path.exists(self._path):
            os.makedirs(self._path)
        self._file_directory = self._path+'\\log.csv'
        self._file = open(self._file_directory,'w', newline='')
        self.write_column_name()
        self._episode = 0

    def log(self, dataset):
        ### add data to logger. This function will sum your data to existed number,
        #  and wirte mean of it into csv file###
        for i, data in enumerate(dataset):
            self._data_storage[i]+=data
        self._episode+=1
    
    def dump(self):
        ### write data into csv file ###
        filewriter = csv.writer(self._file)
        row = []
        for i in range(len(self._data_storage)):
            row.append(self._data_storage[i]/self._episode)
        filewriter.writerow(row)
        self._data_storage=[0]*len(self._columns)
        self._episode=0

    def write_column_name(self):
        filewriter = csv.writer(self._file)
        filewriter.writerow(self._columns)


def logger_test():
    ### when you initialize it, you need to submit column name of this csv file.###
    log = logger(['a','b','c'])
    log.log([1,2,3])
    log.dump()
    log.log([1,2,3])
    log.log([1,2,3])
    log.dump()

if __name__ == '__main__':
    logger_test()