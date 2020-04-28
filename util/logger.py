import csv
import os
from datetime import datetime

class logger:
    def __init__(self, columns):
        self.columns = columns
        self.data_storage = [0]*len(columns)
        self.nameOfFolder = datetime.now()
        self.path = os.getcwd()+'\\'+self.nameOfFolder
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        self.file_directory = self.path+'\\log.csv'
        self.file = open(self.file_directory,'wb')
        self.episode = 0

    def log(self, dataset):
        for i, data in enumerate(dataset):
            self.data_storage[i]+=data
        self.episode+=1
    
    def dump(self):
        filewriter = csv.writer(self.file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in len(self.data_storage):
            self.data_storage[i]/=self.episode
        filewriter.writerow(self.data_storage)
        self.data_storage=[0]*len(self.columns)
        self.episode=0

    def write_column_name(self):
        filewriter = csv.writer(self.file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(self.columns)


if __name__ == '__main__':
    l = [0]*10
    for i in l:
        i+=10
    print(l)