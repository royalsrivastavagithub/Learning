const key = "email";
const person = {
  name: "royal",
  age: 22,
  "person hobbies": ["piano", "games", "reddit"],
};

console.log(person["person hobbies"]);

//if key name have space bracket should be used to call
person[key] = "royalunofficial@gmail.com";
console.log(person.email);
