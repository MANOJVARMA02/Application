from pymongo import MongoClient
import json
import random
client = MongoClient()
db=client.company
emp=db.Employees
i=1
while(i!=50):
    dic={}
    dic["_id"]=i
    dic["name"]=input()
    dic["age"]=random.randint(22,50)
    dic["role"]=input()
    dic["salary"]=random.randint(12000,50000)
    i+=1
    emp.insert_one(dic)

