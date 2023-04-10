from pymongo import MongoClient, errors
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        try:
            self.client = MongoClient('mongodb://%s:%s@127.0.0.1:47725/?authSource=AAC' % (username, password))
            #self.client = MongoClient('127.0.0.1',
            #                username=username,
            #                password=password,
            #                authSource='AAC',
            #                authMechanism='SCRAM-SHA-256',
            #                port=port)
            #self.client.server_info()  # Immediately try to access the server to validate the conn settings
        except errors.ConnectionFailure as e:
            print(e)  # Print the error message for further context on connection failure
        print("Connected to server!")
        # where xxxx is your unique port number
        self.database = self.client['AAC']
        print("Connected to database!")

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            if type(data) is dict:
                if self.database.animals.insert(data):  # data should be dictionary
                    return True
                else:
                    return False 
            else:
                raise Exception("Data to be created must be in dictionary format!")          
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD. 
    def read(self, search):
        if search is not None:
            if type(search) is dict:
                return self.database.animals.find(search, {"_id":False})  # data should be a dictionary which represents the search terms  
            else:
                raise Exception("Search data type must be a dictionary!")          
        else:
            raise Exception("Nothing to read, because search parameter is empty")

# Create method to implement the R in CRUD but only for one entry 
    def readone(self, search):
        if search is not None:
            if type(search) is dict:
                return self.database.animals.find_one(search)  # data should be a dictionary which represents the search terms  
            else:
                raise Exception("Search data type must be a dictionary!")          
        else:
            raise Exception("Nothing to read, because search parameter is empty")
   
# Create method to implement the U in CRUD 
    def update(self, match, data):
        if match is not None and data is not None:
            if type(match) is dict and type(data) is dict:
                return self.database.animals.update(match,data)  # data should be a dictionary which represents the search terms  
            else:
                raise Exception("Search and update data must be of type dictionary!")          
        else:
            raise Exception("Match term and update term need to be supplied!")

# Create method to implement the D in CRUD 
    def delete(self, match):
        if match is not None:
            if type(match) is dict:
                return self.database.animals.remove(match)  # data should be a dictionary which represents the search terms  
            else:
                raise Exception("Search data type must be a dictionary!")          
        else:
            raise Exception("Nothing to delete, because search parameter is empty")