# Codelint - A browser based linter

- To run **frontend**: `npm run dev`
    - Alternatively use `npm run watch` if on AWS cloud9
- To run **backend**: `python app.py`

- To enable Github Oauth create an app at: <https://github.com/settings/applications/new>
    - Set homepage url and callback url to app's root
    - Create client secret
    - Store client id and client secret in .env file as GITHUB\_CLIENT\_ID and GITHUB\_CLIENT\_SECRET respectively
    - Change client id in GithubOauth.js

#### Troubleshooting:
- Change ports as needed (app.py, Socket.js)
