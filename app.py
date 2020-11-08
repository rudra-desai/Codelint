import os
import re
import flask
import subprocess
import flask_socketio
from flask import request
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
app = flask.Flask(__name__)

# database_url = os.getenv('DATABASE_URL')
# app.config['SQLALCHEMY_DATABASE_URI'] = database_url
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
# db.app = app

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
    filename = data['uuid'] + ('.py' if linter == 'pylint' else '.js')
    file = ''

    # get the current script path.
    here = os.path.dirname(os.path.realpath(__file__))
    subdir = "userfiles"

    filepath = os.path.join(here, subdir, filename)
    file = open(filepath, "w")
    file.write(code)
    file.close()

    if linter == 'eslint':
        result = subprocess.run([linter, '-f', 'html', '--fix', f'./userfiles/{filename}'],
                                stdout=subprocess.PIPE).stdout.decode("utf-8")

        result = result.replace('style="display:none"', 'style="display:table-row"')
        result = re.sub(r'\[\+\].*.js', 'eslint', result)
        socketio.emit('output', {
            'linter': linter,
            'output': result
        }, room=request.sid)

        subprocess.run(['rm', '-r' , f'./userfiles/{filename}'])

if __name__ == '__main__':
    # import models
    # models.db.create_all()
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 3000))
    )
