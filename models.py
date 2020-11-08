# models.py
from app import db
from sqlalchemy.orm import relationship
import datetime

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(120))
    historys = relationship("History", backref="Users")
    
    def __init__(self, user_name):
        self.user_name = user_name

    def __repr__(self):
        return str({
            'username': self.user_name,
        })
    
class History(db.Model):
    id = db.Column(db.Integer,db.ForeignKey('users.id'),primary_key=True)
    file_name = db.Column(db.String(120))
    time_stamp = db.Column(datetime)
    users = relationship('Users', foreign_keys='History.id')
    
    def __init__(self, file_name,time_stamp):
        self.file_name = file_name
        self.time_stamp = time_stamp
    
    def __repr__(self):
        return str({
            'filename': self.file_name, 'time_stamp':self.time_stamp
        })