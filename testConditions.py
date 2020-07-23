import sys
import MongoDBUtils
import json


mongo = MongoDBUtils.MongoUtils()
mongo.connect()
mongo.connectToCollectino("dev","bitcoin")


values = mongo.getAll()
print(list(values)[0])