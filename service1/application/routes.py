from application import app
from application import db
from application.models import Fortunes
from flask import request, response, render_template, redirect,url_for
from random import randint, random
from string import string
@app.route('/home', methods=['GET','POST'])
def fortune():
    api = 'http://localhost:5003'

    tokenadd =  request.get(api + '/merge')
    token = tokenadd.text
    fortunes= ["You will have a terrible day","You will have a mediocre day","You will have a great day"]
    fortuneshown= ("")
    if token[0] == "1":
        fortuneshown = fortunes[0]
    elif token[0] == "9":
        fortuneshown = fortunes[2]
    else:
        fortuneshown = fortunes[1]
    
    return render_template('home.html', title='Home', fortuneshown=fortuneshown)
@app.route('/fortune', methods=['GET','POST'])
def output(fortuneshown):
    db.session.app(fortuneshown)
    db.session.commit()


