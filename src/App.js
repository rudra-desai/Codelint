import './App.css';
function App() {
  return (
    <div className="App">
      <div class="topnav">
        <a class="active" href="#home">Home</a>
        <a href="#news">News</a>
        <a href="#contact">Contact</a>
        <a href="#about">About</a>
        <div className="github">
      <button class="githubbutton" type="button">Link with Github</button> <button type="button">Link with Google</button> 
      </div>
      
      </div>
      <h1>EZLint <select name="Linters" id="Linters"> <option disabled selected value> --Choose a Linter-- </option><option>Pylint</option> <option value="audi">ESLint</option> </select></h1>
<div className="textarea"><textarea className="test" placeholder="Paste code here..." style={{height: "200px", width: "1500px"}}></textarea></div>
<div className="LintButton">
  <button class="button1" type="button">Fix Code</button> 
  <button class="button2" type="button">Lint Now!</button> 
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
  <div className="copyrightstuff">
    <p>Copyright 2020© Joel Gonzalez, Anthony Tudorov, Rudra Desai, Chao-Yang Cheng</p>
  </div>
    </div>
    
  );
}
export default App;
