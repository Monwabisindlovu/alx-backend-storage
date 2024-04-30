#!/usr/bin/env python3
//8-all.py
from pymongo import MongoClient

def list_all(mongo_collection):
    """Function that lists all documents in a collection"""
    documents = mongo_collection.find()
    return [doc for doc in documents] if documents else []
