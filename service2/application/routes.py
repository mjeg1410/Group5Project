from application import app
from flask import request, Response
import random
from random import randint
@app.route('/number', methods=['GET', 'POST'])
def numsection():
    numsect=randint(0,1000)
    return  Response(str(numsect), mimetype="text/plain")
