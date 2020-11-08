# models.py
from app import db
import datetime

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(120))
    
    def __init__(self, user_name):
        self.user_name = user_name

    def __repr__(self):
        return str({
            'username': self.user_name,
        })
    
class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(120))
    time_stamp = db.Column(datetime)
    
    def __init__(self, file_name,time_stamp):
        self.file_name = file_name
        self.time_stamp = time_stamp
    
    def __repr__(self):
        return str({
            'filename': self.file_name, 'time_stamp':self.time_stamp
        })