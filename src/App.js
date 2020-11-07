import React, {useState, useEffect} from "react";
import { Socket } from './Socket';
import GithubOauth from './GithubOauth';
import "./styles.css";

export default function App() {
    const [name, setName] = useState('');
    
    useEffect(() => {
        setName('EZLint');
        
        Socket.on('test', (data) => {
            console.log(data);
        });
        
        return () => {
            Socket.close();
        };
    }, []);
    
    useEffect(() => {
        let url = window.location.href;
        url = new URL(url);
        let code = url.searchParams.get('code');
        let state = url.searchParams.get('state');
        if (code !== null && state !== null) {
            Socket.emit('auth user', {'code': code, 'state': state});
        }
    }, []);
    

    return (
        <div id="body">
            <h1>{name}</h1>
            <GithubOauth />
        </div>
    );
}
