from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["college_db"]
collection = db["students"]

# # insert data
# data = {
#     "name": "chandru",
#     "age": 27,
#     "city": "chennai"
# }
#
# collection.insert_one(data)

## read data
# for doc in collection.find():
#     print(doc)

## update data
# collection.update_one(
#     {"name": "chandru"},
#     {"$set": {"age": 12}}
# )
#
# for doc in collection.find():
#     print(doc)

print(collection.find_one({"name": "chandru"}))
## Delete data
# collection.delete_one({"name": "Arun"})
#
# for doc in collection.find():
#     print(doc)