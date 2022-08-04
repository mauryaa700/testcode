import pymongo

client = pymongo.MongoClient("mongodb+srv://Maurya247:Amauryaa1998@cluster0.3jjdk3k.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['myinfo']
#collection1=database["dpkg"]
collection2=database["data"]
'''
record=collection.find()
for i in record:
    if i=='name':
        print(i)
        '''
#data1=collection.find({"name":"Agen"})
#query 1
data2=collection2.find({'id':{'$lt':10}})
#query2 want to select all data
q2=collection2.find()
#query3 filter
q3= collection2.find({'name':"Alais"})

# conditional filter query
'''
when ever we try to write any query in mongo we have to put in in curly braces or key:value pair
for multiple query we have to put query in side list
'''
q4=collection2.find({"name":{"$in":['Alais', 'Al Rais']}})
q5=collection2.find({"id":{"$lte":453}})
#q6=collection2.find({"name":{"$in":['Alais', 'Al Rais']}, "id":{"gt":500}})
#collection2.update_one({"name":"Achiras"}, {"$set":{"name":"Ashish"}})
#collection2.update_one({"id":398}, {"$set":{"name":"orgha"}})
collection2.update_one({"id":1}, {"$set":{"name":"Bhanu"}},{"id":2}, {"$set":{"name":"Prakash"}})
collection2.update_one({"id":[1,2]}, {"$set":[{"name":"Bhanu","name":"prakash"}]})



# delete record

#collection2.delete_one({'id':392})



for i in q2:
    print(i)