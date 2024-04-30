#!/usr/bin/env python3
""" 10-update_topics """

def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name"""
    # Update the document in the collection
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})

# Test the function
if __name__ == "__main__":
    from pymongo import MongoClient

    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Access the collection
    school_collection = client.my_db.school

    # Update topics for Holberton school
    update_topics(school_collection, "Holberton school", ["Sys admin", "AI", "Algorithm"])

    # Print updated documents
    print("After updating topics for Holberton school:")
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))

    # Update topics again for Holberton school
    update_topics(school_collection, "Holberton school", ["iOS"])

    # Print updated documents
    print("\nAfter updating topics for Holberton school again:")
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))
