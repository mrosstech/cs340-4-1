from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password, port):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:%s' % (username, password, port))
        # where xxxx is your unique port number
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary            
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD. 
    def read(self, search):
        if search is not None:
            self.database.animals.find(search)  # data should be list of dictionaries            
        else:
            raise Exception("Nothing to read, because search parameter is empty")