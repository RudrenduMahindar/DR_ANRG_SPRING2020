from pymongo import MongoClient 

import datetime
ts = datetime.datetime.now().timestamp()
#converting timestamp to proper format
import time
readable = time.ctime(ts)

def insert_data(collection,collection_data): #insert the data in collection
   rec_id1 = collection.insert_one(collection_data) 
   print("Data inserted with record ids",rec_id1)
   #rec_id2 = collection.insert_one(temperature2) 
   #print("Data inserted with record ids",rec_id1," ",rec_id2) 

def show_data(collection): #show the data in collection
   cursor = collection.find() 
   for record in cursor: 
      print(record) 

def get_collection_in_database(database_name,collection_name): #Get a particular collection from database       
    try: 
        conn = MongoClient()  #connect to localhost
        print("Connected successfully!!!") 
    except:   
        print("Could not connect to MongoDB") 
    # database 
    #db = conn.database
    db = conn[database_name] 
    # Created or Switched to collection names: my_temperature_collection 
    collection = db[collection_name]
    return collection

temperature1 = { 
        "timestamp":readable, 
        "value":24
        } 
temperature2 = { 
        "timestamp":readable, 
        "value":28
        } 
        
database_name="database" #write your database name
collection_name="my_temperature_collection" #collection name
collection=get_collection_in_database(database_name,collection_name) #get your collection for next operations
insert_data(collection,temperature1)
insert_data(collection,temperature2)
show_data(collection)

