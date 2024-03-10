//Object.create

const obj1 = {
    username:"royal",
    age : 20
}
const obj2 = Object.create(obj1);
obj2.gender = "male";

console.log(obj2.age);
obj2.age = 22;
console.log(obj2.age);

//in ecmascript documentation
//__proto__===[[prototype]] 
//__proto__ !== prototype

console.log(obj2.__proto__);

/*
obj2.__proto__  create a reference from obj1 
but it first chekc in the new oject 
if not fuond then it goes to reference 
if found it returns.
*/