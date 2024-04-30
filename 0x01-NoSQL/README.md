NoSQL Project
================
Description
This project demonstrates the use of MongoDB and Python for working with NoSQL databases. It includes various scripts for tasks such as creating databases, inserting documents, querying information, updating documents, and more.
Installation
MongoDB Installation
To install MongoDB on Ubuntu 18.04:
Add the MongoDB repository key: wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
Add the MongoDB repository: echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
Update the package list: sudo apt-get update
Install MongoDB: sudo apt-get install -y mongodb-org
Verify MongoDB installation: sudo service mongod status and mongo --version
Python Dependencies
Install necessary Python dependencies using pip: pip3 install pymongo
Usage
Clone the repository: git clone https://github.com/your_username/alx-backend-storage.git
Navigate to the project directory: cd alx-backend-storage/0x01-NoSQL
Execute scripts using provided commands.
Files
0-list_databases: List all MongoDB databases.
1-use_or_create_database: Create or use the my_db database.
2-insert: Insert a document into the school collection.
3-all: List all documents in the school collection.
4-match: List documents with name="Holberton school" in the school collection.
5-count: Display the number of documents in the school collection.
6-update: Add a new attribute to documents with name="Holberton school" in the school collection.
7-delete: Delete all documents with name="Holberton school" in the school collection.
8-all.py: Python function to list all documents in a collection.
9-insert_school.py: Python function to insert a new document in a collection.
10-update_topics.py: Python function to change topics of documents based on name.
11-schools_by_topic.py: Python function to return schools with a specific topic.
12-log_stats.py: Python script to provide statistics about Nginx logs stored in MongoDB.
100-find: List documents with name starting with "Holberton" in the school collection.
101-students.py: Python function to return all students sorted by average score.
102-log_stats.py: Enhanced version of 12-log_stats.py to include the top 10 most present IPs in the logs.
Credits
This project is part of the ALX Software Engineering program.
