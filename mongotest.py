import pymongo

client = pymongo.MongoClient("mongodb+srv://Maurya247:Amauryaa1998@cluster0.3jjdk3k.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data={
    "name": "ashish",
    "mail":"mauryaa@gmail.com",
    "subject":"FSDS"
}

database = client['myinfo']
collection=database["ashu"]
collection.insert_one(data)