import React from "react";
import Socket from './Socket';
import './github.css'
import githubPng from "./github.png"

export default function GithubOauth() {

    function handleLogin() {
        let state = Math.random().toString();
        Socket.emit('store state', {
            'state': state
        });
        window.location = 'https://github.com/login/oauth/authorize?client_id=862222f107a099fa6750&redirect_uri=' +
            'http://localhost:8082/&state=' + state + '&scope=repo';
    }
    
    return (
      <button className="gitButton" onClick={handleLogin}>
          <img className="logo" width="20px" height="" src={githubPng}></img>
          Link With Github
      </button>
    );
}