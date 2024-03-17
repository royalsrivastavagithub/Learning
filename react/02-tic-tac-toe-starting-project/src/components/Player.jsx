import {useState} from "react";
export default function Player({ name, symbol }) {
  const [isEditing, setIsEditing]= useState(false);
  function handleEditClick() {
  setIsEditing((editing)=>!editing);
  }
  let playerName = <span className="player-name">{name}</span>;
  let btnCaption = "EDIT";
  if (isEditing) {
    playerName = <input type="text" required value={name}></input>;
    btnCaption = "SAVE";
  }
  return (
    <li>
      <span className="player">
        {playerName}
        <span className="player-Symbol">{symbol}</span>
      </span>
      <button onClick={handleEditClick}>{btnCaption}</button>
    </li>
  );
}
