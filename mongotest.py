import pymongo
client = pymongo.MongoClient("mongodb+srv://Maurya24:Amauryaa1998@cluster0.uks8ruj.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name" : "Ashish",
    "email" : "mr.mauryaa@gmail.com",
    "surname" : "maurya"

}

db1=client['mongotest']
coll = db1['test']
coll.insert_one(d)