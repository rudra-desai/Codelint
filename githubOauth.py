import requests
import os
from dotenv import load_dotenv

load_dotenv()
github_id = os.getenv('GITHUB_CLIENT_ID')
github_secret = os.getenv('GITHUB_CLIENT_SECRET')

def get_user_info(user_access_token):
    headers = {
        'Authorization': 'token ' + user_access_token
    }
    user = requests.get('https://api.github.com/user', headers=headers).json()
    login = user['login']
    name = user['name']
    email = user['email']
    profile_image = user['avatar_url']
    print('login: ', login, 'name: ', name, ' email: ', email, ' profile_image: ', profile_image)
    
    headers = {
        'Authorization': 'token ' + user_access_token,
        'Accept': 'application/vnd.github.v3+json'
    }
    params = {
        'visibility': 'all'
    }
    repo_url = 'https://api.github.com/user/repos'
    repos = requests.get(repo_url, params=params, headers=headers).json()
    
    print(login, '\'s repos:')
    repos_names = []
    for repo in repos:
        repos_names.append(repo['name'])
        
    print(repos_names)
    


def get_auth_token(code, state):
    print(github_id)
    params = {
        'client_id': github_id,
        'client_secret': github_secret,
        'code': code,
        'redirect_uri': 'http://localhost:8083/',
        'state': state
    }
    headers = {
        'Accept': 'application/json'
    }
    r = requests.post('https://github.com/login/oauth/access_token', params=params, headers=headers).json()
    print(r)
    access_token = r['access_token']
    scopes = r['scope'].split(',')
    
    get_user_info(access_token)