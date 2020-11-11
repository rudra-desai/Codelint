# models.py
from app import db
from sqlalchemy.orm import relationship
import datetime

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(120))
    name = db.Column(db.String(120))
    email = db.Column(db.String(120))
    profile_image = db.Column(db.Stinrg(120))
    sid = db.Column(db.Stinrg(120))
    headers = db.Column(db.String(120))
    
    def __init__(self, login, name, email, profile, sid, headers):
        self.login = login
        self.name = name
        self.email = email
        self.profile = profile
        self.sid = sid
        self.headers = headers

    def __repr__(self):
        return str({
            'username': self.name, 'login': self.login, 'email': self.email, 'profile_image': self.profile, 'sid': self.sid, 'headers': self.headers
        })
    

