# project/__init__.py

import os  # new
from flask import Flask
from flask_restx import Resource, Api
import csv
import json
from configparser import ConfigParser
from glob import glob

#c1 : /readcsv : this method should read csv file and return its contents(json format)
#c2: path of the csv file should be configured into setting
#c2 : read csv func can read multiple csv files at once, so input of this method/operation should be an arary



#/writecsv:
#c1: 

# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')  # new
app.config.from_object(app_settings)      # new

class Readcsv(Resource):
    
    def csvtojsonconvert(file): 
        f= open(file,'r')
        csvReader = csv.DictReader(f)
        rootitem = str(file)
        arr= {rootitem: []}
        #arr= []
        for csvRow in csvReader:
           arr[rootitem].append(csvRow)
           #arr.append(csvRow)
        s= json.dumps(arr)
        #print (s)
        #print (type(s))
#        print (f)
#        reader = csv.reader(f, delimiter=';')
#        data_list = list()
#        for row in reader:
#            data_list.append(row)
#            data = [dict(zip(data_list[0],row)) for row in data_list]
#            data.pop(0)
#        s = json.dumps(data)

        #print (s)
        return s;
    
    def get(self, portal):
        print(portal)
        all_csv_files = Readcsv.getallcsvfiles(portal)
       # print(all_csv_files)
        outp ={}
        for file in range(len(all_csv_files)):
#            print (all_csv_files[file])
            output = Readcsv.csvtojsonconvert(all_csv_files[file])
            print(output)
            print(json.loads(output))
            #outp += output
            outp[len(outp)] = json.loads(output)
        #print(outp)
        #print(output)
        #print(type(output))
        #print(outp)
        #out =json.loads(outp)
        #out =json.loads(outp)
        #print(type(outp))
        return outp
    
    def getallcsvfiles(portal):
        configur = ConfigParser() 
        print (configur.read('.//project//config.ini'))
        print ("khs_portal: ", configur.get('portals_path','khs_path'))
        print ("krones_portal: ", configur.get('portals_path','krones_path'))
        if portal=="khs":
            PATH = configur.get('portals_path','khs_path')
        elif portal=="krones":
            PATH = configur.get('portals_path','krones_path')
        EXT = "*.csv"
        all_csv_files = [file
                 for path, subdir, files in os.walk(PATH)
                 for file in glob(os.path.join(path, EXT))]
        return all_csv_files;
    
    

api.add_resource(Readcsv, '/readcsv/<portal>')