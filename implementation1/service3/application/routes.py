from application import app
from flask import request, response
from random import randint, random
from string import string 
@app.route('/strsection', methods=['GET', 'POST'])
def strgen():
    strsection= ''.join([random.choice(string.ascii_letters ) for n in range(3)])
    return response(strsection)
