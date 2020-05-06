from application import app
from flask import request, Response
from random import randint
@app.route('/number', methods=['GET', 'POST'])

def numsection():
    numsect=randint(0,100)
    return Response(str(numsect), mimetype="text/plain")
