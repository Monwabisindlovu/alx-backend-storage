#!/usr/bin/env python3
""" 9-insert_school """

def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs"""
    # Insert the document into the collection
    result = mongo_collection.insert_one(kwargs)
    # Return the new _id
    return result.inserted_id

# Test the function
if __name__ == "__main__":
    from pymongo import MongoClient

    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Access the collection
    school_collection = client.my_db.school

    # Insert a new school document
    new_school_id = insert_school(school_collection, name="UCSF", address="505 Parnassus Ave")
    print("New school created: {}".format(new_school_id))
