# models.py
from app import db

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(120))

    def __init__(self, user_name):
        self.user_name = user_name

    def __repr__(self):
        return str({
            'username': self.user_name,
        })

