from flask import Flask, request, jsonify
import mysql.connector as conn

app = Flask(__name__)

mydb = conn.connect(host="localhost", user='root', passwd="MSdhoni07")
cursor = mydb.cursor()
cursor.execute("create database if not exists taskdb")
cursor.execute("create table if not exists taskdb.tasktable (name varchar(30) , number int)")


@app.route("/insert", methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into taskdb.tasktable  values(%s , %s)", (name, number))
        mydb.commit()
        return jsonify(str('succesfully inserted'))

@app.route("/update", methods=['POST'])
def update():
    if request.method == 'POST':
        get_name = request.json['get_name']
        cursor.execute("Update taskdb.tasktable set number = number+500 Where name = %s", (get_name,))
        mydb.commit()
        return jsonify(str('Updated successfully'))

@app.route("/delete", methods=['POST'])
def delete():
    if request.method == 'POST':
        name_del = request.json['name_del']
        cursor.execute("delete from taskdb.tasktable where name = %s", (name_del,))
        return jsonify(str('Deleted successfully'))

@app.route("/fetch", methods = ['POST'])
def fetch_data():
    cursor.execute("Select * FROM taskdb.tasktable")
    l = []
    for i in cursor.fetchall():
        l.append(i)
    return jsonify(str(l))

if __name__ == '__main__':
    app.run()