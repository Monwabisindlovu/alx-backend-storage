#!/usr/bin/env python3
""" 8-all """

def list_all(mongo_collection):
    """List all documents in a collection"""
    documents = []
    for doc in mongo_collection.find():
        documents.append(doc)
    return documents

# Test the function
if __name__ == "__main__":
    from pymongo import MongoClient
    
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Access the collection
    school_collection = client.my_db.school
    
    # List all documents in the collection
    schools = list_all(school_collection)
    
    # Print the documents
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
