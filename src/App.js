import React, {useState, useEffect} from "react";
import Top from './Top'
import Editor from './Editor'
import GithubOauth from './GithubOauth';
import Socket from './Socket'
import parse from 'html-react-parser';
import { v4 as uuidv4 } from 'uuid';
import "./styles.css"
import loadingGif from './loading.gif';

export default function App() {
    const [code, setCode] = useState('')
    const [linter, setLinter] = useState('')
    const [errors, setErrors] = useState('')
    const [selectLinterError, setSelectLinterError] = useState('')
    const [isLoggedIn, setIsLoggedIn] = useState(false)
    const [loading, setLoading] = useState(false)
    const [user, setUser] = useState(null)
    
    useEffect(() => {
        Socket.on('logged in data', (data) => {
            setIsLoggedIn(data['logged_in']);
            if (isLoggedIn) {
                setUser(data['user_info'])
            }
        });

        Socket.emit('is logged in');
        
        Socket.on('output', ({linter, output}) => {
            setLoading(false)
            if (linter === 'eslint')
                setErrors(parse(output))
            if (linter === 'pylint')
                setErrors(parse(output))
        })

        const url = new URL(window.location.href);
        const code = url.searchParams.get('code');
        const state = url.searchParams.get('state');

        if (code !== null && state !== null) {
            window.history.replaceState({}, document.title, "/");
            Socket.emit('auth user', {
                'code': code,
                'state': state
            });
        }
        
        return () => {
            Socket.close();
        };
    }, []);

    const handleChange = (newValue) => {
        setCode(newValue)
    }

    const handleClick = () => {
        if (linter === ''){
            setSelectLinterError('Please select a linter!')
            return;
        }
        setLoading(true)
         Socket.emit('lint', {
             'code': code,
             'linter': linter,
             'uuid': uuidv4()
         })
    }

    const handleDropdown = ({value}) => {
        setLinter(value)
        setSelectLinterError('')
    }

    return (
        <div className="body">

            <div className="github">
                <GithubOauth />
            </div>
            <Top handleDropdown={handleDropdown}
                 linter={linter}
            />

            <div className="div-error">
                <p className="error">{selectLinterError}</p>
            </div>

            <Editor
                handleChange={handleChange}
                code={code}
            />
            <button class="lintbutton" onClick={handleClick}>{loading ? <img src={loadingGif} alt="loading" value="Lint!" /> : "Lint!"}</button>

            <br />
            <div className="code">
                {errors}
            </div>
        </div>
    );
}

