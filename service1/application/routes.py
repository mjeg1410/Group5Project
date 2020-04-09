from application import app
from flask import request, response
from random import randint, random
from string import string
api = 'http://localhost:5003'

tokenadd =  request.get(api + '/merge')
token = tokenadd.text
def fortune():
    fortunes= ["You will have a terrible day","You will have a mediocre day","You will have a great day"]
    fortuneshown= ("")
    if token.lower[0] == "1":
        fortuneshown = fortunes[0]
    elif token.lower[0] == "9":
        fortuneshown = fortunes[2]
    else:
        fortuneshown = fortunes[1]
#need a home route that renders the template