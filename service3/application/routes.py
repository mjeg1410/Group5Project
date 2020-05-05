from application import app
from flask import request, response
from random import randint, random
import string 
@app.route('/charecter', methods=['GET', 'POST'])
def random_charecter():
    lucky_charecter= ''.join([random.choice(string.ascii_letters ) for n in range(3)])
    return response(lucky_charecter)

