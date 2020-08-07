from pymongo import MongoClient
from pprint import pprint
from random import randint
import asyncio
import aiohttp

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
def InsertRecord(data, collection):    
    if type(data) == list:
        res = db[collection].insert_many(data, show_record_id=True).inserted_ids
    else: 
        if type(data) == dict:
            res = db[collection].insert_one(data).inserted_id

    return res

client = MongoClient(host="127.0.0.1", port=27017)
db=client.business

smt = {
    "name": "Salty Big Inc",
    "rating": 2,
    "cuisine": "halal"
}

print(InsertRecord(smt,'reviews'))
print(db["reviews"].find_one({"cuisine":"halal"}))