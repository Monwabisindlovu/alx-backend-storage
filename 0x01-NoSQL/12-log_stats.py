#!/usr/bin/env python3
"""12-log_stats"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # Total number of logs
    num_logs = collection.count_documents({})
    print("{} logs".format(num_logs))

    # Methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        num_method = collection.count_documents({"method": method})
        print("    method {}: {}".format(method, num_method))

    # Status check
    num_status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(num_status_check))
