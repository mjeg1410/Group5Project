from application import app
from application import db
from application.models import Fortunes
from flask import request, render_template, redirect,url_for, Response
import requests
from random import randint, random
import string
@app.route('/home', methods=['GET','POST'])
def home():
    
    return render_template('home.html', title='Home')
@app.route('/fortune', methods=['GET','POST'])
def fortune():
    api = 'http://service4:5003'
    tokenadd =  requests.get('http://service4:5003/merge')
    token =tokenadd.text
    fortunes= ["You will have a terrible day","You will have a mediocre day","You will have a great day"]
    if token[0] == "1":
        #fortuneshown =Fortunes(fortune=fortunes[0]) 
        fortuneshown=fortunes[0]
    elif token[0] == "9":
        #fortuneshown = Fortunes(fortune=fortunes[2])
        fortuneshown=fortunes[2]
    else:
        fortuneshown=fortunes[1]
        #fortuneshown = Fortunes(fortune=fortunes[1])
    return Response(str(fortuneshown), mimetype="text/plain")
        #db.session.add(fortuneshown)
        #db.session.commit()
    #return render_template('fortune.html', title='Fortune', fortuneshown=fortuneshown)
def output(fortuneshown):
    db.session.add(fortuneshown)
    db.session.commit()
    return render_template('fortune.html', title='Fortune', fortuneshown=fortuneshown)
