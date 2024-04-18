from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, user, password, host='nv-desktop-services.apporto.com', port = 30876, db='aac', col='animals'):

        """
        Initialize the AnimalShelter with connection details.
        
        :param user: Username for MongoDB authentication.
        :param password: Password for MongoDB authentication.
        :param host: MongoDB server host. Defaults to 'nv-desktop-services.apporto.com'.
        :param port: MongoDB server port. Defaults to 30876.
        :param db: Database name. Defaults to 'aac'.
        :param col: Collection name. Defaults to 'animals'.
        """
        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (user, password, host, port))
        self.database = self.client[db]
        self.collection = self.database[col]

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

    def update(self, query, update_values):
        """ Update document(s) in the MongoDB database. """
        if query is None or update_values is None:
            raise ValueError("Query and update values cannot be None")

        try:
            result = self.collection.update_many(query, {'$set': update_values})
            return result.modified_count  # Return the count of modified documents
        except Exception as e:
            print(f"An error occurred during update: {e}")
            return 0  # Return 0 if update fails

    def delete(self, query):
        """ Delete document(s) from the MongoDB database. """
        if query is None:
            raise ValueError("Query cannot be None")

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count  # Return the count of deleted documents
        except Exception as e:
            print(f"An error occurred during delete: {e}")
            return 0  # Return 0 if delete fails

# # Example usage:

# # Assuming 'animal_shelter' is an instance of the 'AnimalShelter' class

# # Create a new animal record
# new_animal = {
#     "name": "Sammy",
#     "animal_type": "Snake",
#     "age": 2
# }
# create_result = animal_shelter.create(new_animal)
# print(f"Creation result: {'Success' if create_result else 'Failure'}")

# # Update an existing animal record
# update_query = {"name": "Sammy", "animal_type": "Snake"}
# update_values = {"age": 3}
# update_result = animal_shelter.update(update_query, update_values)
# print(f"Number of documents updated: {update_result}")

# # Read the updated animal record
# read_result = animal_shelter.read(update_query)
# for doc in read_result:
#     print(doc)

# # Delete an animal record
# delete_query = {"name": "Sammy", "animal_type": "Snake"}
# delete_result = animal_shelter.delete(delete_query)
# print(f"Number of documents deleted: {delete_result}")