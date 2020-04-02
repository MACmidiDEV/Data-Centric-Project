import pymongo
import os

# MONGODB_URI = "mongodb+srv://root:r00tUser@mile3db-of5eb.mongodb.net/toodlerLearnDB?retryWrites=true&w=majority"
MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "toodlerLearnDB"
COLLECTION_NAME = "toodlerLearnDBcoll"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("ERROR! Connection FAILED: %s") % e    
conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]
documents = coll.find()
for doc in documents:
    print(doc)
