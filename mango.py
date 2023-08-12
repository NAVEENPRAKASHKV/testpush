import pymongo
client=pymongo.MongoClient("mongodb+srv://naveenprakash1912:Naveen123@cluster0.nth4nhy.mongodb.net/?retryWrites=true&w=majority")
db=client.test
print(db)

d={
    "a":1,
    "b":2,
    "c":3
}

db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)