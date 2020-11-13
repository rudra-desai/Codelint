import requests
import os
import base64
import models
from settings import db
from flask import request, session
from dotenv import load_dotenv

load_dotenv()
github_id = os.getenv('GITHUB_CLIENT_ID')
github_secret = os.getenv('GITHUB_CLIENT_SECRET')

def log_user_info(user_access_token):
    headers = {
        'Authorization': 'token ' + user_access_token
    }
    user = requests.get('https://api.github.com/user', headers=headers).json()
    login = user['login']
    name = user['name']
    email = user['email']
    profile_image = user['avatar_url']
    model = models.Users(login, name, email, profile_image, request.sid, user_access_token)
    db.session.add(model)
    db.session.commit()
    
def auth_user(code, state):
    params = {
        'client_id': github_id,
        'client_secret': github_secret,
        'code': code,
        'redirect_uri': 'https://b5212afbd02a410697a8708bdded4bf3.vfs.cloud9.us-east-1.amazonaws.com/',
        'state': state
    }
    headers = {
        'Accept': 'application/json'
    }
    r = requests.post('https://github.com/login/oauth/access_token', params=params, headers=headers).json()
    access_token = r['access_token']
    
    log_user_info(access_token)
        
def get_user_data(user_id):
    query = models.Users.query.filter_by(sid=user_id).first()
    return {'login': query.login, 'profile_image': query.profile_image}

def get_user_repos(user_id):
    user_access_token = models.Users.query.filter_by(sid=user_id).first().access_token
    headers = {
        'Authorization': 'token ' + user_access_token,
        'Accept': 'application/vnd.github.v3+json'
    }
    params = {
        'visibility': 'all'
    }
    repo_url = 'https://api.github.com/user/repos'
    repos = requests.get(repo_url, params=params, headers=headers)
    if repos.status_code == 403:
        return {'repos': None, 'error': 'bad github token'}
    
    repos = repos.json()
    return {'repos': [(repo['name'], repo['url']) for repo in repos], 'error': None}
    
def get_user_repo_tree(user_id, repo_url):
    user_access_token = models.Users.query.filter_by(sid=user_id).first().access_token
    headers = {
        'Authorization': 'token ' + user_access_token,
        'Accept': 'application/vnd.github.v3+json'
    }
    repo_url = repo_url + '/commits/master'
    repo = requests.get(repo_url, headers=headers)
    if repo.status_code == 403:
        return {'tree': None, 'error': 'bad github token'}
    repo = repo.json()
    params = {
        'recursive': True
    }
    tree = requests.get(repo['commit']['tree']['url'], params=params, headers=headers)
    if tree.status_code == 403:
        return {'tree': None, 'error': 'bad github token'}
    
    tree = tree.json()
    return {'tree': tree['tree'], 'error': None}

def get_user_file_contents(user_id, content_url):
    user_access_token = models.Users.query.filter_by(sid=user_id).first().access_token
    headers = {
        'Authorization': 'token ' + user_access_token,
        'Accept': 'application/vnd.github.v3+json'
    }
    contents = requests.get(content_url, headers=headers)
    if contents.status_code == 403:
        return {'contents': None, 'error': 'bad github token'}
    
    contents = contents.json()
    if 'content' not in contents:
        return {'contents': None, 'error': 'could not determine contents'}
    else:
        return {'contents': base64.b64decode(contents['content']).decode("utf-8"), 'error': None}