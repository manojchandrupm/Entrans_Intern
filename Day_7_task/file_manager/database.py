from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["file_manager_db"]

collection = db["files"]

