from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["brain_tumor_db"]

collection = db["predictions"]