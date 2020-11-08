import os
import flask
import subprocess
import flask_socketio
import requests
from flask import request
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from githubOauth import get_auth_token

load_dotenv()
app = flask.Flask(__name__)

database_url = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.app = app

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

states = set()
@app.route('/')
def main():
    return flask.render_template('index.html')

@socketio.on('connect')
def on_connect():
    print(f"{request.sid} connected")
    socketio.emit('test', {
        'message': 'Server is up!'
    })
    
@socketio.on('store state')
def on_store_state(data):
    states.add(data['state'])
    
@socketio.on('auth user')
def on_auth_user(data):
    code = data['code']
    state = data['state']
    if state not in states:
        print('state: ', state, ' does not match any waiting states')
        return
    else:
        get_auth_token(code, state)
        
@socketio.on('lint')
def code(data):
    linter = data['linter']
    code = data['code']
    file_name = data['uuid']
    file = ''

if __name__ == '__main__':
    import models
    models.db.create_all()
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 3000))
    )