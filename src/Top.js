import React from "react";
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';
import './top.css'

export default function Top({handleDropdown , linter}) {
    return (
        <div className="top">
            <h2>Codelint</h2>
            <Dropdown className="dropdown" options={["pylint", "eslint"]}
                onChange={handleDropdown}
                value={linter}
                placeholder="Select a linter"
            />
        </div>
    )
}