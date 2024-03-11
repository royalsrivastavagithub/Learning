//parameter destructuring

//highly used with objects and react 

const person = 
{
    firstname:"royal",
    gender : "male"
}

function getdetails({firstname,gender})
{
console.log("name:",firstname,"\ngender:",gender);
}

getdetails(person);