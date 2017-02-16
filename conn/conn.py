from pymongo import MongoClient

class conn:
    def insertintodb(self, types, names):
        client = MongoClient()
        db = client.listofnames
        db.names.insert_one({
            types : names
        })

