#!/usr/bin/env python3
""" 102-log_stats """

def log_stats(mongo_collection):
    """ Log stats """

    # Total number of logs
    total_logs = mongo_collection.count_documents({})

    # Methods stats
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_stats = {method: mongo_collection.count_documents({"method": method}) for method in methods}

    # Status check stats
    status_check = mongo_collection.count_documents({"method": "GET", "path": "/status"})

    # IP stats
    ips = mongo_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    # Print stats
    print("{} logs".format(total_logs))
    print("Methods:")
    for method, count in method_stats.items():
        print("\tmethod {}: {}".format(method, count))
    print("{} status check".format(status_check))
    print("IPs:")
    for ip in ips:
        print("\t{}: {}".format(ip["_id"], ip["count"]))

# Test the function
if __name__ == "__main__":
    from pymongo import MongoClient

    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Access the collection
    logs_collection = client.logs.nginx

    # Call the function
    log_stats(logs_collection)
