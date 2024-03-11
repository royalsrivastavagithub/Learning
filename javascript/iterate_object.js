const person = {
  name: "royal",
  age: 22,
  "person hobbies": ["piano", "games", "reddit"],
};

for (let key in person) {
  console.log(key, ":", person[key]);
}
console.log(Object.keys(person));
for (let key of Object.keys(person)) {
  console.log(person[key]);
}
