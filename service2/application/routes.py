from application import app
from flask import request, Response
from random import randint 
@app.route('/number', methods=['GET', 'POST'])
def random_number():
    lucky_number=random.randrange(0,100)
    return Response(lucky_number)
