import './App.css';
function App() {
  return (
    <div className="App">
      <h1>EZLint <select name="cars" id="cars"> <option disabled selected value> --Choose a Linter-- </option><option>Pylint</option> <option value="audi">ESLint</option> </select></h1>
<div className="textarea"><textarea className="test" placeholder="Paste code here..." style={{height: "200px", width: "1500px"}}></textarea></div>
<div className="LintButton">
  <button type="button">Lint Now!</button> 
  <button type="button">Fix Code</button> 
  </div>
<div className="checkboxes">
  <input type="checkbox" id="whitespace" name="whitespace" value="whitespace"></input>
  <label for="vehicle1"> Whitespace </label>
  </div>
  <div className="checkbox2">
  <input type="checkbox" id="Long Lines" name="Long Lines" value="Long Lines"></input>
  <label for="vehicle1"> Long Lines </label>
  </div>
  <div className="checkbox3">
  <input type="checkbox" id="For/if" name="For/if" value="For/if"></input>
  <label for="vehicle1"> For/if stmts. </label>
  </div>
  <div className="checkbox4">
  <input type="checkbox" id="Semicolons" name="Semicolons" value="Semicolons"></input>
  <label for="vehicle1"> Semicolons </label>
  </div>
  <div className="checkbox5">
  <input type="checkbox" id="Other" name="Other" value="Other"></input>
  <label for="vehicle1"> Other </label>
  </div>
    </div>
    
  );
}
export default App;
