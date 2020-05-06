from application import app
from flask import request, Response
from random import randint, random, choice
import string

@app.route('/strsection', methods=['GET', 'POST'])
def strgen():
    strsection= ''.join([choice(string.ascii_letters) for n in range(3)])
    return Response(strsection, mimetype="text/plain")
