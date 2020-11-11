import React from "react";
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';
import './top.css'

export default function Top({handleDropdown , linter}) {
    return (
        <div className="top">
             <div className="codelint">
                  <div className="codelint"><h2>CodeLint</h2></div>
                 </div>
                 <div className="dropdown">
                 <Dropdown className="dropdown" options={["pylint", "eslint"]}
                           onChange={handleDropdown}
                           value={linter}
                           placeholder="Select a linter" />
                </div>
        </div>
    )
}