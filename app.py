import os
import re
import flask
import subprocess
import flask_socketio
import models
from flask import request, session, escape
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from githubOauth import auth_user, get_user_data, get_user_repos, get_user_repo_tree

load_dotenv()
app = flask.Flask(__name__)

database_url = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('APP_SECRET')

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

@socketio.on('is logged in')
def on_is_logged_in():
    if 'user_id' in session:
        user_id = escape(session['user_id'])
        # if user_id in db:
        #     user_info = db call
        #     socketio.emit('is logged in', {'logged_in': True, 'user_info': user_info}, request.sid)
    else:
        socketio.emit('logged in data', {'logged_in': False}, room=request.sid)

@socketio.on('store state')
def on_store_state(data):
    states.add(data['state'])
    
@socketio.on('auth user')
def on_auth_user(data):
    code = data['code']
    state = data['state']
    if state not in states:
        print('state: ', state, ' does not match any waiting states')
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
    linter = data['linter']
    code = data['code']
    filename = data['uuid'] + ('.py' if linter == 'pylint' else '.js')

    # get the current script path.
    here = os.path.dirname(os.path.realpath(__file__))
    subdir = "userfiles"

    filepath = os.path.join(here, subdir, filename)
    file = open(filepath, "w")
    file.write(code)
    file.close()

    if linter == 'eslint':
        result = subprocess.run([linter, '-f', 'html', f'./userfiles/{filename}'],
                                stdout=subprocess.PIPE).stdout.decode("utf-8")

        result = result.replace('style="display:none"', 'style="display:table-row"')
        result = re.sub(r'\[\+\].*.js', 'eslint', result)
        socketio.emit('output', {
            'linter': linter,
            'output': result
        }, room=request.sid)

        subprocess.run(['rm', '-r', f'./userfiles/{filename}'])

if __name__ == '__main__':
    import models
    models.db.create_all()
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 3000))
    )
