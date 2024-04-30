#!/usr/bin/env python3
"""
Module defines a function that provides some stats about Nginx logs stored
in MongoDB.
"""
from pymongo import MongoClient


def data_logs():
    """
    Gather the logs collection from the database logs
    and return it.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_db = client.logs
    nginx_collection = logs_db.nginx

    return nginx_collection


def display():
    """Displays the number of documents in the collection nginx"""
    nginx_collection = data_logs()
    print("{} logs".format(nginx_collection.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print("\tmethod {}: {}".format(method,
                                       nginx_collection.count_documents
                                       ({"method": method})))
    print("{} status check".format(nginx_collection.count_documents({
        "method": "GET", "path": "/status"})))


if __name__ == "__main__":
    display()
