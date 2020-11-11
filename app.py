import os
import flask
import subprocess
import flask_socketio
import models
from os.path import join, dirname
from flask import request, session, escape
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from githubOauth import auth_user, get_user_data, get_user_repos, get_user_repo_tree
from lint import lint_code

dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)
app = flask.Flask(__name__)

database_url = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('APP_SECRET')

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app
db.create_all()
db.session.commit()

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

@socketio.on('is logged in')
def on_is_logged_in():
    if 'user_id' in session:
        user_id = escape(session['user_id'])
        # if user_id in db:
        #     user_info = db call
        #     socketio.emit('is logged in', {'logged_in': True, 'user_info': user_info}, request.sid)
    else:
        socketio.emit('logged in data', {
            'logged_in': False
        }, room=request.sid)

@socketio.on('store state')
def on_store_state(data):
    states.add(data['state'])
    
@socketio.on('auth user')
def on_auth_user(data):
    code = data['code']
    state = data['state']
    if state not in states:
        print(f'state: {state} does not match any waiting states')
    else:
        auth_user(code, state)
        socketio.emit('user data', get_user_data(session['user_id']))
        
@socketio.on('get repos')
def on_get_user_repos():
    socketio.emit('repos', get_user_repos(session['user_id']), request.sid)
    
@socketio.on('get repo tree')
def on_get_user_repo_tree(data):
    socketio.emit('repo tree', get_user_repo_tree(session['user_id'], data['repo_url']), request.sid)

@socketio.on('lint')
def code(data):
    res = lint_code(data)
    socketio.emit('output', res, room=request.sid)
    subprocess.run(['rm', '-r', f'./userfiles/{res["filename"]}'])

if __name__ == '__main__':
    import models
    models.db.create_all()
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 3000))
    )
