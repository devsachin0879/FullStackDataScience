import pymongo
client = pymongo.MongoClient("mongodb+srv://SachinDev:MSdhoni07@cluster0.ubf77.mongodb.net/?retryWrites=true&w=majority")
db = client.test
# print(db)

## Create Database
database = client["MyTest2"]

### check existing database name
# for i in client.list_database_names():
#     print(i)

## create collection
collection_name = "Faculties"
faculties = database[collection_name]

###########################################################################

### insert records with user defined ids
list_of_records_user_defined_ids = [
    {
        "_id":"1",
        "comapnyName":"iNeuron",
        "Faculty": "Sachin Dev"
    },
    {
        "_id":"2",
        "comapnyName":"iNeuron",
        "Faculty": "Manna Dev"
    }
]
faculties_record = faculties.insert_many(list_of_records_user_defined_ids)
for i in faculties_record.inserted_ids:
    print(i)

###########################################################################

### FInd Method in MongoDB
find_first_record = faculties.find_one()
print(f"The First record of the collection: \n{collection_name} = \n{find_first_record}")


## find all records
all_records = faculties.find()
for  idx,record in enumerate(all_records):
    print(f"{idx}.  {record}")

###########################################################################

### Query or filter out data

query1 = {"_id": "1"}
results = faculties.find(query1)
for data in results:
    print(data)

query2 = {"comapnyName":"iNeuron"}
results = faculties.find(query2)
for i in results:
    print(i)

for i in faculties.find({'_id':{'$gt':'1'}}):##id should be greater than(gt) 1
    print(i)

for i in faculties.find({'_id':{'$lt':'2'}}):##id should be gesser than(lt) 2
    print(i)

for i in faculties.find({'_id':{'$eq':'2'}}):##id should be equals to(eq) 2
    print(i)

###########################################################################

#### Delete one or many documents in MongoDB
random_data = [
    {'_id':'3','comapnyName': 'iNeuron', 'Faculty': 'XYZ'},
    {'_id':'4','comapnyName': 'iNeuron', 'Faculty': 'ABC'},
    {'_id':'5','comapnyName': 'iNeuron', 'Faculty': 'POR'},
]
faculties.insert_many(random_data)

for i in faculties.find():
    print(i)

# delete one document
query_to_delete = {"Faculty": "XYZ"}
faculties.delete_one(query_to_delete)

# delete multiple documents
multi_query_to_delete = {"_id": {"$gte": "4"}} ### id >= 4
faculties.delete_many(multi_query_to_delete)

### in order to delete all the documents present in the collection we can just pass an empty dictionary like:
# faculties.delete_many({})

###########################################################################

