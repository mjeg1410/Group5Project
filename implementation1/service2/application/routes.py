from application import app
from flask import request, response
from random import randint 
@app.route('/number', methods=['GET', 'POST'])
def numsection():
    numsect=random.randrange(0,100)
    return response(numsect)
