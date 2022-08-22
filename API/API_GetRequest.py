from flask import Flask, request, jsonify
import mysql.connector as connection

app = Flask(__name__)

@app.route("/testfun")
def test():
    get_name = request.args.get("get_name")
    mobile_number = request.args.get("mobile")
    mail_id = request.args.get("mail_id")
    return "This is my 1st function for  get {} {} {}".format(get_name, mobile_number, mail_id)

@app.route("/testfun1")
def get_database():
    db = request.args.get("db")
    table = request.args.get("table")

    conn = connection.connect(host='localhost',user='root',passwd='MSdhoni07',database = db)
    cur = conn.cursor()
    cur.execute(f"Select * FROM {table}")
    data = cur.fetchall()
    conn.commit()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(port = 5002)