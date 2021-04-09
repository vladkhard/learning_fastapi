import os
import pymongo


DB_NAME = os.getenv("DB_NAME")


client = pymongo.MongoClient("mongodb://db:27017")
db = client[DB_NAME]
