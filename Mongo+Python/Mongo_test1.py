import pymongo
client = pymongo.MongoClient("mongodb+srv://SachinDev:MSdhoni07@cluster0.ubf77.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

### create a database
database = client["MyTest"]

### check existing database name
print(client.list_database_names())

## create collection....... collection is equaivalent to tables in sql but format is different
collection = database["test"]
print(collection)

## insert record to collection
record = {
    'companyName':'iNeuron',
    'product':'Affordable AI',
    'courseOffered':'Deep Learning for Computer Vision',
    'name': ["Sachin","Dev",1345],
    "record_dict": {"name": "Sachin","mail_id": "devsachin0879#gmail.com", "ph_num": 1234561}
}
collection.insert_one(record)


## insert multiple records
list_of_records = [
    {
        'companyName':'iNeuron',
        'product':'Affordable AI',
        'courseOffered':'Deep Learning for Computer Vision'
    },

    {
        'companyName':'iNeuron',
        'product':'Affordable AI',
        'courseOffered':'Machine Learning With Deployment'
    },

    {
        'companyName':'iNeuron',
        'product':'Affordable AI',
        'courseOffered':'Data Science Masters'
    },
]
rec = collection.insert_many(list_of_records)


### Print unique IDs of the records
inserted_IDs = rec.inserted_ids

for idx,unique_ids in enumerate(inserted_IDs):
    print(f"{idx}.  {unique_ids}")










