import Header from "./components/Header";
import UserInput from "./components/UserInput";
import Results from "./components/Results";
import { useState } from "react";
function App() {
  const [userInput, setUserInput] = useState({
    initialInvestment: 10000,
    annualInvestment: 1200,
    expectedReturn: 6,
    duration: 10,
  });

const inputIsValid = userInput.duration>=1;

  function handleChange(inputIdentifier, newValue) {
    setUserInput((prevUserInupt) => {
      return {
        ...prevUserInupt,
        [inputIdentifier]: +newValue,
      };
    });
  }

  
  return (
    <>
      <Header></Header>
      <UserInput userInput={userInput} onChange={handleChange}></UserInput>
        {!inputIsValid && (<p className="center">Please enter duration greated than zero.</p>)}
      {inputIsValid && <Results input={userInput}></Results>}
    </>
  );
}

export default App;
