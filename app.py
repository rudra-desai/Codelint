import os
import flask
import subprocess
import flask_socketio
from flask import request
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
app = flask.Flask(__name__)

database_url = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.app = app

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

@app.route('/')
def main():
    return flask.render_template('index.html')

@socketio.on('connect')
def on_connect():
    print(f"{request.sid} connected")
    socketio.emit('test', {
        'message': 'Server is up!'
    })

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
