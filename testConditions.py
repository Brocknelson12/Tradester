import sys
import MongoDBUtils


mongo = MongoDBUtils.MongoUtils()
mongo.connect()
mongo.connectToCollectino("dev","bitcoin")


values = mongo.getAll()
print(values)