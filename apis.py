from flask import Flask,make_response,abort
import json

from pymongo import MongoClient

app = flask.Flask(__name__)

@app.route("/",methods=['GET'])
def fun1():
    client = MongoClient()
    db = client.company
    e = db.Employees
    lst =[]
    for i in e.find():
        lst.append(i)
    return json.dumps(lst)
@app.route("/<int:get_id>",methods=[GET])
def get_emp(get_id):
    client=MongoClient()
    db=client.company
    e=db.Employees
    lst=[]
    req_emp=[]
    for i in e.find():
        lst.append(i)
    for emp in lst:
        if(emp["_id"]==get_id):
            req_emp.append(emp)
    if(len(req_emp==0)):
        abort(404)
    return json.dumps(req_emp)
@app.errorhandler(404)
def not_found(error):
    return make_response(json.dumps({"there is an error"}),404)
        

app.run(port=5050)
