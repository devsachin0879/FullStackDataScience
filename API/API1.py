from flask import Flask, request, jsonify

## Flask helps to expose my func to outer world
##create object of flask class so, we can access all the methods inside FLask class
app = Flask(__name__)


##get:- posting a data in URL like google search
##post:- posting the data through a body like while logging to gmail
@app.route('/abc',methods=['GET', 'POST'])
def test1():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
        return jsonify(str(result))


@app.route('/abc1',methods=['GET', 'POST'])
def test2():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a * b
        return jsonify(str(result))

@app.route('/abc2',methods=['GET', 'POST'])
def test3():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a - b
        return jsonify(str(result))

@app.route('/abc3',methods=['GET', 'POST'])
def test4():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a / b
        return jsonify(str(result))

@app.route('/abc4',methods=['GET', 'POST'])
def test5():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a ** b
        return jsonify(str(result))

if __name__ == '__main__':
    app.run()

def test(a,b):
    return a+b

