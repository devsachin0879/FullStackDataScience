from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://SachinDev:MSdhoni07@cluster0.ubf77.mongodb.net/?retryWrites=true&w=majority")
database = client['taskdb']
collection = database['taskcollection']


@app.route("/insert/mongo", methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name: number})
        return jsonify(str("successfully inserted "))


if __name__ == '__main__':
    app.run(port=5001)