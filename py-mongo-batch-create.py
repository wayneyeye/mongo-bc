from pymongo import MongoClient
import pprint, time

host="192.168.1.188"
port="27017"
uri = "mongodb://yewenhe0904:k2cxtrb64vi@"+host+":"+port+"/test_db?authMechanism=SCRAM-SHA-1"
client = MongoClient(uri)

db=client.test_db
collection=db.test

# timer start
start=time.time()
for i in range(10000):
	collection.insert({"foo":"bar","baz":i,"z":10-i})
# timer end
total=time.time()-start
print("%d seconds" % total)


