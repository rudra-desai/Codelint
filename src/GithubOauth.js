import React from "react";
import Socket from './Socket';
import './github.css'
export default function GithubOauth() {

    function handleLogin() {
        let state = Math.random().toString();
        Socket.emit('store state', {
            'state': state
        });
        window.location = 'https://github.com/login/oauth/authorize?client_id=b1cf50b0666d4c956c2e&redirect_uri=' +
            'https://b5212afbd02a410697a8708bdded4bf3.vfs.cloud9.us-east-1.amazonaws.com/&state=' + state + '&scope=repo';
    }
    
    return (
      <button className="gitButton" onClick={handleLogin}>
          <img className="logo" width="20px" height="" src="https://assets.stickpng.com/images/5847f98fcef1014c0b5e48c0.png"></img>
          Link With Github
      </button>
    );
}