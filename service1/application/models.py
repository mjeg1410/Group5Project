from application import db
class Fortunes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fortune = db.Column(db.String,nullalbe=False)