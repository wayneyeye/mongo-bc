from pymongo import MongoClient
import pprint

host="192.168.1.188"
port="27017"
uri = "mongodb://yewenhe0904:k2cxtrb64vi@"+host+":"+port+"/test_db?authMechanism=SCRAM-SHA-1"
client = MongoClient(uri)


# db=client.test_db
# collection=db.test

# pprint.pprint(collection.find_one())