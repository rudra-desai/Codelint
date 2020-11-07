import React, {useState, useEffect} from "react";
import AceEditor from 'react-ace';
import Socket from './Socket'
import Dropdown from 'react-dropdown';
import { v4 as uuidv4 } from 'uuid';
import 'react-dropdown/style.css';
import "./styles.css";

import "ace-builds/src-noconflict/mode-javascript";
import "ace-builds/src-noconflict/theme-tomorrow_night";
import "ace-builds/src-noconflict/ext-language_tools"

let socket;

export default function App() {
    const [code, setCode] = useState('')
    const [linter, setLinter] = useState('')
     useEffect(() => {
         socket = Socket();

         socket.on('test', (data) => {
                console.log(data)
         })

         return () => {
             socket.close();
         };
     }, [])

    const handleChange = (newValue) => {
        setCode(newValue)
    }

    const handleClick = () => {
         socket.emit('lint', {
             'code': code,
             'linter': linter,
             'uuid': uuidv4()
         })
    }

    const handleDropdown = ({value}) => {
        setLinter(value)
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
            <input type="submit" onClick={handleClick}/>
        </div>
    );
}

