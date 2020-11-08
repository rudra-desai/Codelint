import React from "react";
import Socket from './Socket';

export default function GithubOauth() {

    function handleLogin() {
        let state = Math.random().toString();
        Socket.emit('store state', {
            'state': state
        });
        window.location = 'https://github.com/login/oauth/authorize?client_id=862222f107a099fa6750&redirect_uri=' +
            'http://localhost:8083/&state=' + state + '&scope=repo';
    }
    
    return (
      <button onClick={handleLogin}>Github</button>
    );
}