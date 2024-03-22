import { useState } from "react";

export default function Player() {
 const [enteredPlayerNAme,setEnteredPlayerName]=useState('');
 const [submitted,setSubmitted]=useState(false);
 function handChange(event){
      setEnteredPlayerName(event.target.value)
 }

 function handleClick(){
setSubmitted(true)
 }
  return (
    <section id="player">
      <h2>Welcome {submitted?enteredPlayerNAme:"unknown"} entity</h2>
      <p>
        <input type="text" onChange={handChange} value={enteredPlayerNAme}/>
        <button onClick={handleClick}>Set Name</button>
      </p>
    </section>
  );
}
