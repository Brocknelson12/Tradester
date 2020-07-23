import pymongo
class MongoUtils():
    connectionString  = "mongodb://localhost:27017/"
    collection: any
    connection: any

    def connect(self):
        self.connection = pymongo.MongoClient(self.connectionString)

    def connectToCollectino(self, db,collection):
        self.collection = self.connection[db][collection]

    def getAll(self):
        return self.collection.find()

    # def findByIDAndUpdate(self,tempDict):
    #     print("findBYID")
    #     print(self.collection)
    #     try:
    #         self.collection.find_one_and_update(
    #             {"_id" : dict["_id"]},tempDict,upsert=True
    #         )
    #     except:
    #         try:
    #             print(tempDict)
    #             print(type(tempDict))
    #             self.collection.insert_one(tempDict) 
    #         except Exception as e:
    #             print(str(e))
                # print("ERRsOR")


# class TaLibMongo():
    
