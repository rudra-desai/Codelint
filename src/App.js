import React, {useState, useEffect} from "react";
import { render } from "react-dom";
import AceEditor from "react-ace";
import Socket from './Socket'
import "./styles.css";

import "ace-builds/src-noconflict/mode-java";
import "ace-builds/src-noconflict/theme-github";

let socket;

export default function App() {
     useEffect(() => {
         socket = Socket();

         socket.on('test', (data) => {
                console.log(data)
         })

         return () => {
             socket.close();
         };
     }, [])

    const onChange = (newValue) => {
         console.log("change", newValue);
    }


    return (
        <div id="body">
            <AceEditor
                  placeholder=""
                  mode="javascript"
                  theme="monokai"
                  name="blah2"
                  onChange={onChange}
                  fontSize={14}
                  showPrintMargin={true}
                  showGutter={true}
                  highlightActiveLine={true}
                  setOptions={{
                  enableBasicAutocompletion: false,
                  enableLiveAutocompletion: false,
                  enableSnippets: false,
                  showLineNumbers: true,
                  tabSize: 2,
              }}/>
        </div>
    );
}

