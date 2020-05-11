import csv
import os
from datetime import datetime



_columns = None
_data_storage = None
_nameOfFolder = str(datetime.now().strftime("%Y%m%d-%H%M%S"))
_path = os.getcwd()+'\\'+'data'+'\\'+_nameOfFolder
_path.replace(' ','')
if not os.path.exists(_path):
    os.makedirs(_path)
_file_directory = _path+'\\log.csv'
_file = open(_file_directory,'w', newline='')
_write_column_name()

def initialize(columns):
    _columns = columns
    _data_storage = [0]*len(columns)

def log(key, data):
    ### add data to logger. This function will sum your data to existed number,
    #  and wirte mean of it into csv file###
    if key not in _columns:
        raise NameError()
    i = _columns.index(key) 
    _data_storage[i]+=data

def dump():
    ### write data into csv file ###
    filewriter = csv.writer(_file)
    row = []
    for i in range(len(_data_storage)):
        row.append(_data_storage[i])
    filewriter.writerow(row)
    self._data_storage=[0]*len(_columns)

def _write_column_name(self):
    filewriter = csv.writer(_file)
    filewriter.writerow(_columns)


def logger_test():
    ### when you initialize it, you need to submit column name of this csv file.###
    log = initialize(['a','b','c'])
    log([1,2,3])
    dump()
    log([1,2,3])
    log([1,2,3])
    dump()

if __name__ == '__main__':
    logger_test()