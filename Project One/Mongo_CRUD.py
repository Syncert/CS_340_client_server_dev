from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self):
        # Connection Variables
        USER = 'aacuser'
        PASS = 'pickle123'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31580
        DB = 'aac'
        COL = 'animals'
        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        """Insert a document into the MongoDB database."""
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True  # Return True if insert is successful
            except Exception as e:
                print(f"An error occurred: {e}")
                return False  # Return False if insert fails
        else:
            raise ValueError("Nothing to save, because data parameter is empty")

    def read(self, criteria=None):
        """Query documents from the MongoDB database."""
        if criteria is None:
            criteria = {}  # If no criteria is given, set it to an empty dictionary

        try:
            documents = self.collection.find(criteria)
            return list(documents)  # Convert cursor to list and return
        except Exception as e:
            print(f"An error occurred: {e}")
            return []  # Return an empty list if query fails

# Example usage:

# Assuming 'animal_shelter' is an instance of the 'AnimalShelter' class
# To insert a document:
# result = animal_shelter.create({"name": "Max", "animal_type": "Dog"})
# print(result)

# To read documents:
# animals = animal_shelter.read({"animal_type": "Dog"})
# for animal in animals:
#     print(animal)
