from pymongo import MongoClient, errors
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password, port):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        try:
            self.client = MongoClient('mongodb://%s:%s@localhost:%s' % (username, password, port))
            self.client.server_info()  # Immediately try to access the server to validate the conn settings
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
                return self.database.animals.insert(data)  # data should be dictionary  
            else:
                raise Exception("Data to be created must be in dictionary format!")          
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD. 
    def read(self, search):
        if search is not None:
            if type(search) is dict:
                return self.database.animals.find(search)  # data should be a dictionary which represents the search terms  
            else:
                raise Exception("Search data type must be a dictionary!")          
        else:
            raise Exception("Nothing to read, because search parameter is empty")