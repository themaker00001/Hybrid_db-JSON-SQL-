import json
import os 

df_file="sample.json"

class Storage:
    def __init__(self):
        '''the constrcutor is just creating the object and also making the directory and the file which store the data our case it is
        data/sample.json'''
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(df_file):
            with open (df_file,"w")as f: # I just need to create a empty file if my db file is not thhere 
                # json.dumps({}) # donot use the dumps i have used it earlier but it convert the json into string 
                json.dump({},f)
    def _load(self):   # this is a private method which i have used for loading the data 
        '''this is going to read the JSON file and returns its content into python dictionary 
        that is our evivalet to the python obj.'''
        with open(df_file,"r")as f:
            return json.load(f)
    def _save(self,data):
        '''this is going to save the data dictonary/obj to the json - which is going to act life in memory db '''
        with open(df_file,'w')as f:
            return json.dump(data,f)
    def insert(self,table,row):
        '''in this code we are first loading the data from our private methods then checking the table is there or not in the dictonary
        and then adding the new table with its data like this 
        {
            "users": [
                {"id": 1, "name": "Alice"},
                {"id": 2, "name": "Bob"}
            ],
            "products": [
                {"id": 101, "name": "Laptop"}
            ]
        }'''
        data=self._load()   
        if table not in data:
            data[table]=[]
        data[table].append(row)
        self._save(data)
    def scan(self,table):
        '''we are taking of the table deatils which kind of data is inside the table for this i am just giving the 
        dictonary key which is table_name and fetching all the data inside the array which is everything'''
        data=self._load()
        return data.get(table,[])
        
