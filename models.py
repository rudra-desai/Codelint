from settings import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120))
    profile_image = db.Column(db.Stinrg(120))
    sid = db.Column(db.Stinrg(120), unique=True, nullable=False)
    access_token = db.Column(db.String(120), unique=True)
    
    def __init__(self, login, name, email, profile_image, sid, access_token):
        self.login = login
        self.name = name
        self.email = email
        self.profile_image = profile_image
        self.sid = sid
        self.access_token = access_token
        
    def __repr__(self):
        return str({
            'username': self.name, 'login': self.login, 'email': self.email, 'profile_image': self.profile, 'sid': self.sid, 'access_token': self.access_token
        })
    

