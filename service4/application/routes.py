from application import app
from flask import request, Response
from random import randint, random
import string
import requests
api1 = 'http://service2:5001'
api2 = 'http://service3:5002'

@app.route('/merge', methods=['GET','POST'])
def merge():
    response1 = requests.get(api1 +  '/number')
    response2 = requests.get(api2 + '/charecter')
    merged= (response1.text + response2.text)
    return Response(merged)
