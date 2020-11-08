import React, {useState, useEffect} from "react";
import GithubOauth from './GithubOauth';
import AceEditor from 'react-ace';
import Socket from './Socket'
import parse from 'html-react-parser';
import Dropdown from 'react-dropdown';
import { v4 as uuidv4 } from 'uuid';
import 'react-dropdown/style.css';
import "./styles.css"

import "ace-builds/src-noconflict/mode-javascript";
import "ace-builds/src-noconflict/theme-tomorrow_night";
import "ace-builds/src-noconflict/ext-language_tools"

export default function App() {
    const [code, setCode] = useState('')
    const [linter, setLinter] = useState('')
    const [errors, setErrors] = useState('')
    const [selectLinterError, setSelectLinterError] = useState('')
    const [isLoggedIn, setIsLoggedIn] = useState(false)
    const [user, setUser] = useState(null)
    
    useEffect(() => {
        Socket.on('is logged in', (data) => {
            console.log(data)
            setIsLoggedIn(data['logged_in']);
            if (isLoggedIn) {
                setUser(data['user_info'])
            }
        });
        Socket.emit('is logged in');
        
        Socket.on('output', ({linter, output}) => {
            if (linter === 'eslint')
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
            <div className="top">
                 <h1>Codelint</h1>
                 <Dropdown options={["pylint", "eslint"]}
                           onChange={handleDropdown}
                           value={linter}
                           placeholder="Select a linter" />
            </div>
            <div className="div-error">
                <p className="error">{selectLinterError}</p>
            </div>
            <AceEditor
                mode="javascript"
                theme="tomorrow_night"
                onChange={handleChange}
                value={code}
                name="UNIQUE_ID_OF_DIV"
                editorProps={{ $blockScrolling: true }}
                setOptions={{
                  enableBasicAutocompletion: true,
                  enableLiveAutocompletion: true,
                  enableSnippets: true
                }}
            />
            <input type="submit" value="Lint" onClick={handleClick}/>
            <GithubOauth />
            <br />
            <div className="code">
                {errors}
            </div>
        </div>
    );
}

