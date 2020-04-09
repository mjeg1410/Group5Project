from application import app
from flask import request, response
from random import randint, random
from string import string
api1 = 'http://localhost:5001'
api2 = 'http://localhost:5002'

@app.route('/merge', methods=['GET','POST'])
def merge():
    response1 = requests.get(api1 +  '/number')
    response2 = requests.get(api2 + '/strsection')
    merged= (response1.text + response2.text)
def fortune():
    fortuneshown= #loop to determine fortune based on merged variable. Need a list/dictionary.
