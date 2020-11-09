import requests
import os
import models
import base64
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
    #to db => {'login': login, 'name': name, 'email': email, 'profile_image': profile_image, 'access_token': access_token, 'sid': request.sid}
    
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
    #from db using user_id => (login, profile_image)
    #return {'login': login, 'profile_image': profile_image}
    pass

def get_user_repos(user_id):
    #user_access_token = lookup from db from user_id
    headers = {
        'Authorization': 'token ' + user_access_token,
        'Accept': 'application/vnd.github.v3+json'
    }
    params = {
        'visibility': 'all'
    }
    repo_url = 'https://api.github.com/user/repos'
    repos = requests.get(repo_url, params=params, headers=headers).json()

    return [(repo['name'], repo['url']) for repo in repos]
    
def get_user_repo_tree(user_id, repo_url):
    #user_access_token = lookup from db from user_id
    headers = {
        'Authorization': 'token ' + user_access_token,
        'Accept': 'application/vnd.github.v3+json'
    }
    repo_url = repo_url + '/commits/master'
    repo = requests.get(repo_url, headers=headers).json()
    params = {
        'recursive': True
    }
    tree = requests.get(repo['commit']['tree']['url'], params=params, headers=headers).json()
    return tree['tree']

def get_user_file_contents(user_id, content_url):
    #user_access_token = lookup from db from user_id
    headers = {
        'Authorization': 'token ' + user_access_token,
        'Accept': 'application/vnd.github.v3+json'
    }
    contents = requests.get(content_url, headers=headers).json()
    if 'content' in contents:
        return base64.b64decode(contents['content'])
    else:
        print('could not determine contents')
        return None