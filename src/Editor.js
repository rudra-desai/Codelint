import React from "react";
import AceEditor from 'react-ace';
import './editor.css'
import "ace-builds/src-noconflict/mode-javascript";
import "ace-builds/src-noconflict/theme-tomorrow_night";
import "ace-builds/src-noconflict/ext-language_tools"

export default function Editor({handleChange , code}) {
    return (
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
                name="ace-editor"
                tabSize={10}
            />
    )
}