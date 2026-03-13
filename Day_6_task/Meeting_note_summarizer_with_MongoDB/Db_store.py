from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["summary_store"]
collection = db["summary_details"]
