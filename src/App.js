import React, {useState, useEffect} from "react";
import Socket from './Socket'
import "./styles.css";


let socket;

export default function App() {
    const [name, setName] = useState('')
     useEffect(() => {
         setName('EZLint')

         socket = Socket();

         socket.on('test', (data) => {
                console.log(data)
         })

         return () => {
             socket.close();
         };
     }, [])

    return (
        <div id="body">
            <h1>{name}</h1>
        </div>
    );
}
