import csv
import json
from configparser import ConfigParser

#import os
#from glob import glob
#PATH = "E:/Test_Portal_Automation/KHS"
#EXT = "*.csv"
#all_csv_files = [file
#                 for path, subdir, files in os.walk(PATH)
#                 for file in glob(os.path.join(path, EXT))]
##print(all_csv_files)
#print(len(all_csv_files))
#
#
##Readcsv
#configur = ConfigParser() 
#print (configur.read('config.ini')) 
#print ("khs_portal: ", configur.get('portals_path','khs_path')) 

#with open('E:/Test_Portal_Automation/KHS/Run/10062020/Data/10062020_Dailylogs.csv', 'r') as f:
#    reader = csv.reader(f, delimiter=';')
#    data_list = list()
#    for row in reader:
#        data_list.append(row)
#data = [dict(zip(data_list[0],row)) for row in data_list]
#data.pop(0)
#s = json.dumps(data, indent=2)
#print (s)

with open ("E:/Test_Portal_Automation/KHS/Run/10062020/Data/10062020_Dailylogs.csv") as csvFile:
    csvReader = csv.DictReader(csvFile)
    arr= {'list': []}
    print(csvReader)
    for csvRow in csvReader:
        arr["list"].append(csvRow)
#print(arr)

    s= json.dumps(arr, indent = 4)
    print(type(s))
    print(s)
