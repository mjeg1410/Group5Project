from application import app
from flask import request, Response
from random import randint, random
import string 
@app.route('/charecter', methods=['GET', 'POST'])
def random_charecter():
    lucky_character= ''.join([random.choice(string.ascii_letters) for n in range(3)])
    return Response(lucky_character)
