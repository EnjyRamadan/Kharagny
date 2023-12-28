from calendar import c
from http import client
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId


class Database:
    _instance = None
    dbName = "Kharagny"
    client = MongoClient()

    def _new_(cls, *args, **kwargs):
        if cls._instance is None:
            cls.instance = super().new_(cls)
            # Use the connection string for a local MongoDB instance
            uri = "mongodb://localhost:27017/"
            cls._instance.client = MongoClient(uri)
        return cls._instance

    @staticmethod
    def getInstance():
        return Database()._instance

    def getCollection(self, collection):
        return self.client[Database.dbName][collection]

    @staticmethod
    def Insert(collectionName, document):
        collection = Database().getCollection(collectionName)
        insertID = collection.insert_one(document).inserted_id
        return insertID

    @staticmethod
    def InsertMany(collectionName, documents):
        collection = Database().getCollection(collectionName)
        collection.insert_many(documents)

    @staticmethod
    def SelectCollection(collectionName, param):
        collection = Database().getCollection(collectionName)
        if param:
            result = collection.find(param)
        else:
            result = collection.find()
        data = list(result)
        return data

    @staticmethod
    def SelectRecordCollection(collectionName, param, col):
        collection = Database().getCollection(collectionName)
        if col:
            col = {key: 1 for key in col}
        else:
            col = None
        if param:
            result = collection.find(param, col)
        else:
            result = collection.find({}, col)
        data = list(result)
        return data

    @staticmethod
    def SelectByID(collectionName, ID):
        collection = Database().getCollection(collectionName)
        data = collection.find_one({"_id": ObjectId(ID)})
        return data

    @staticmethod
    def Count(collectionName):
        collection = Database().getCollection(collectionName)
        return collection.count_documents(filter={})

    @staticmethod
    def DeleteID(collectionName, ID):
        collection = Database().getCollection(collectionName)
        collection.delete_one({"_id": ObjectId(ID)})

    @staticmethod
    def UpdateOne(collectionName, ID, query):
        collection = Database().getCollection(collectionName)
        collection.update_one({"_id": ObjectId(ID)}, query)

    @staticmethod
    def ReplaceOne(collectionName, ID, newData):
        collection = Database().getCollection(collectionName)
        collection.replace_one({"_id": ObjectId(ID)}, newData)

    @staticmethod
    def AddToRecord(collectionName, ID, data):
        collection = Database().getCollection(collectionName)
        collection.update_one({"_id": ObjectId(ID)}, {"$push": data})

    @staticmethod
    def RemoveFromRecord(collectionName, ID, data):
        collection = Database().getCollection(collectionName)
        collection.update_one({"_id": ObjectId(ID)}, {"$pull": data})
